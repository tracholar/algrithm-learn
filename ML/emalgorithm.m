%% EM algorithm for GMM
% 
% 

% generate data
mu1 = [1; -1];
sigma1 = [1 0.5; 0.5 1];

mu2 = [2; 2];
sigma2 = [4 1; 1 4];

X = zeros(200,2);
X(1:100,:) = randGaussian(mu1, sigma1, 100);
X(101:end,:) = randGaussian(mu2, sigma2, 100);

% visualize data
figure;
plot(X(1:100,1), X(1:100,2), 'b.');
hold on;
plot(X(101:200,1), X(101:200,2), 'r.');
hold off;

% EM algorithm
w1 = 0.5;
w2 = 0.5;
mu1 = rand(2, 1);
mu2 = rand(2,1);
sigma1 = eye(2);
sigma2 = eye(2);

maxIter = 10;
gama = zeros(200, 1);
for i = 1:maxIter
    t1 = 0;
    t2 = 0;
    for j = 1:200
        gama(j) = Gauss(X(j,:)', mu1, sigma1) > Gauss(X(j,:)', mu2, sigma2);
    end
    
    w1 = sum(gama) / length(gama);
    w2 = 1 - w2;
    
    sigma1 = (X' - repmat(mu1, 1, 200)) * diag(gama) * (X' - repmat(mu1, 1, 200))' / sum(gama);
    sigma2 = (X' - repmat(mu2, 1, 200)) * diag(1 - gama) * (X' - repmat(mu2, 1, 200))' / sum(1-gama);
    
    mu1 = X' * gama / sum(gama);
    mu2 = X' * (1 - gama) / sum(1-gama);
end

hold on;
plot(mu1(1), mu1(2), 'b+');
plot(mu2(1), mu2(2), 'r+');

plot(X(gama==1,1), X(gama==1,2), 'bo');
plot(X(gama==0,1), X(gama==0,2), 'ro');

hold off;

mean(gama ~= [ones(100,1); zeros(100,1)])