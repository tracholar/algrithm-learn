%% RIDGEREGRESSION
% ridge regression
% See also RIDGE
%
% hehe
% 
% Copyright 1993-2008 The MathWorks, Inc.
data = load('abalone.txt');

X = data(:,1:end-1);
Y = data(:,end);
sigma = corr(X);
[V D] = eig(sigma);
m = length(X);
Z = (X - ones(m,1) * mean(X)) * V;


%% regression
XX = [ones(m,1) X];

d = size(XX,2);
lambda = 2;
w = (XX' * XX + lambda * eye(d)) \ XX' * Y;

w