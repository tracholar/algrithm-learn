
%% read data

f = fopen('iris.data','r');
data = textscan(f,'%f %f %f %f %s','Delimiter',',');
fclose(f);

X = cell2mat(data(1:4));
Y = zeros(length(data{5}),1);
Y(strcmp(data{5},'Iris-setosa'))=0;
Y(strcmp(data{5},'Iris-versicolor'))=1;
Y(strcmp(data{5},'Iris-virginica'))=2;
m = length(X);

%% visualize data
plot_X = X(:,1);
plot_Y = X(:,2);
figure;
plot(plot_X(Y==0),plot_Y(Y==0),'r.',plot_X(Y==1),plot_Y(Y==1),'g.',plot_X(Y==2),plot_Y(Y==2),'b.');

%% prepare data
y = zeros(m,1);
y(Y==1) = 1;
y(Y~=1) = -1;



%% solve the quadratic programming, no slack variables
w = zeros(size(X,2),1);
b = 0;
theta = [w;b];

% quadprog argument
H = eye(length(theta));
H(end,end) = 0;

f = zeros(length(theta),1);
% f(end) = 1;

A = -diag(y)*[X ones(m,1)];
B = -ones(m,1);

options = optimset('Algorithm','interior-point-convex','Display','iter','MaxIter',150);
theta = quadprog(H,f,A,B,[],[],[],[],[],options);
w = theta(1:end-1);
b = theta(end);

%% train error
fprintf('%f\n',[w;b]);
fprintf('train error is %.3f\n', 1-mean(sign(X*w+b)==y));

%% solve the quadratic programming with slack variables
w = zeros(size(X,2),1);
b = 0;
epsilon = zeros(m,1);
theta = [w(:); b; epsilon(:)];

H = eye(length(theta));
H(length(w)+1:end,length(w)+1:end) = 0;

f = zeros(size(theta));
f(size(w,2)+2:end) = 4;

A = [-diag(y)*[X ones(m,1)],-eye(m);
     zeros(m,size(X,2)+1), -eye(m) ];
B = [-ones(m,1); zeros(m,1)];
theta = quadprog(H,f,A,B,[],[],[],[],[],options);

w = theta(1:length(w));
b = theta(length(w)+1);
epsilon = theta(end-m+1:end);

%% train error
fprintf('%f\n',[w;b]);
pred = sign(X*w+b);
fprintf('train error is %.3f\n', 1-mean(pred==y));

hold on;
plot(plot_X(pred==1),plot_Y(pred==1),'ro',plot_X(pred==-1),plot_Y(pred==-1),'ko');
hold off;