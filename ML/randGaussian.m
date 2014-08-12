function x = randGaussian(mu, sigma, n)
%% 产生高斯随即向量
m = length(mu);
x = repmat(mu(:)', n, 1) + randn(n,m) * chol(sigma);
end