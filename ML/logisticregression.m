%% read data

f = fopen('iris.data','r');
data = textscan(f,'%f %f %f %f %s','Delimiter',',');
fclose(f);

X = cell2mat(data(1:4));
y = strcmp(data{5},'Iris-virginica');


%% split data
m = length(y);
rnd_idx = randperm(m);
trainX = X(rnd_idx(1:40),:);
trainY = y(rnd_idx(1:40));
testX  = X(rnd_idx(41:m),:);
testY = y(rnd_idx(41:m));


%% train

X = [ones(size(trainX,1),1) trainX];
Y = trainY;
costJ = @(t)( -1/length(Y)*(Y' * log(sigmoid(X*t)) +(1-Y') * log(1-sigmoid(X*t))));
theta0 = zeros(size(X,2), 1);

options = optimset('MaxIter',10,'Display','iter');
[theta, minJ]= fminunc(costJ, theta0, options);

%% Test

w = [ones(size(testX,1),1) testX] * theta;
plot(w,testY,'+');
hold on;
plot(w,sigmoid(w),'r.');
hold off;
mean((w>0) == testY)
theta
