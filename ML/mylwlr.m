function mylwlr()
%% read data
data = load('abalone.txt');


X = data(:,1:end-1);
Y = data(:,end);
sigma = corr(X);
[V D] = eig(sigma);
m = length(X);
Z = (X - ones(m,1) * mean(X)) * V;


%% regression
XX = [ones(m,1) X];
W = inv(kener(XX, XX)) * kener(XX, ones(m,1) * Y');



end


function kij = kener(xi, xj)
    sigma = 1;
    kij = exp(-(xi - xj) * (xi - xj)' / 2 / sigma^2);
end