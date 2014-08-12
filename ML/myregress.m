data = load('abalone.txt');


X = data(:,1:end-1);
Y = data(:,end);
sigma = corr(X);
[V D] = eig(sigma);
m = length(X);
Z = (X - ones(m,1) * mean(X)) * V;


% figure;
% plot(Z(:,1), Y, '.');

XX = [ones(m,1) X];
W = inv(XX' * XX) * XX' * Y;

pred = XX * W;

figure;
plot(Z(:,1), Y, 'b.', Z(:,1), pred, 'r.', Z(:,1),Y - pred, 'g.');

