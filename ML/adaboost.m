
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

%% boost
D = ones(m, 1) / m;
[bestStump, minError, bestClass] = buildStump(X, y, D);

% weekClass = struct('bestStump',{},'minError',{}, 'bestClass',{},'alpha',{});
clear weekClass;
aggClass = zeros(m,1);
for i = 1:14000
    [bestStump, minError, bestClass] = buildStump(X, y, D);
    alpha = 0.5 * log10((1 - minError) / max(minError, 1e-6));
    bestStump.alpha = alpha;
    weekClass(i) = struct(bestStump);
    expon = -1 * alpha * y .* bestClass;
    D = D .* exp(expon);
    D = D / sum(D);
    
    aggClass = aggClass + alpha * bestClass;
    errorRate = 1 - mean(sign(aggClass) == y);
    if errorRate < 1e-4
        break;
    end
    
end

errorRate