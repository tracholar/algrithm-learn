function p = Gauss(x, mu, sigma)
    m = length(mu);
    p = 1 / (sqrt(2*pi))^m / sqrt(det(sigma)) * exp(- (x - mu)' / sigma * (x - mu) / 2);
end