%% read data

f = fopen('iris.data','r');
data = textscan(f,'%f %f %f %f %s','Delimiter',',');
fclose(f);

X = cell2mat(data(1:4));
Y = zeros(length(data{5}),3);
Y(:,1) = strcmp(data{5},'Iris-setosa');
Y(:,2) = strcmp(data{5},'Iris-versicolor');
Y(:,3) = strcmp(data{5},'Iris-virginica');


%% split data
m = length(Y);
rnd_idx = randperm(m);
train_number = 100;
trainX = X(rnd_idx(1:train_number),:);
trainY = Y(rnd_idx(1:train_number),:);
testX  = X(rnd_idx(train_number+1:m),:);
testY = Y(rnd_idx(train_number+1:m),:);


%% train ANN
%   4 - 4 - 3
input_number = 4;
hidden_layer_number = 4;
output_number = 4;
Theta1 = zeros(input_number+1, hidden_layer_number)-0.5;
Theta2 = zeros(hidden_layer_number+1,output_number)-0.5;

init_theta = [Theta1(:); Theta2(:)];
lambda = 0.01;

maxIter = 1:500;
trainErrors = zeros(size(maxIter));
testErrors = zeros(size(maxIter));

theta = init_theta;

options = optimset('MaxIter',500,'GradObj','on','Display','iter');
[theta, minJ] = fminunc(@(t)(annBPObj(t,input_number,hidden_layer_number,output_number,X,X,lambda)),theta,options);
Theta1 = reshape(theta(1:(input_number+1) * hidden_layer_number),input_number+1, hidden_layer_number);
Theta2 = reshape(theta((input_number+1) * hidden_layer_number+1:end),hidden_layer_number+1,output_number);

%% train error
pred = annPredict(trainX,Theta1,Theta2);
ty = zeros(length(pred),1);
ty(trainY(:,1)==1) = 1;
ty(trainY(:,2)==1) = 2;
ty(trainY(:,3)==1) = 3;
train_errors = 1 - mean(ty==pred)

%% test error
pred = annPredict(testX,Theta1,Theta2);
ty = zeros(length(pred),1);
ty(testY(:,1)==1) = 1;
ty(testY(:,2)==1) = 2;
ty(testY(:,3)==1) = 3;
test_errors = 1 - mean(ty==pred)


