%% simulate EM algorithm 
% three coin


pa = 0.3;
pb = 0.1;
pc = 0.5;

% generate n result
n = 1000000;
Y = zeros(n,1);
for i=1:n
    if rand() < pa    % Coin B
        if rand() < pb  
            Y(i) = 1;
        else
            Y(i) = 0;
        end
    else
        if rand() < pc
            Y(i) = 1;
        else
            Y(i) = 0;
        end
    end
end



% EM algorithm
maxIter = 10;
pai = 0.2;  % estimate pa pb pc value
pbi = 0.1;
pci = 0.2;
for i = 1:maxIter
    mu = pai * pbi .^ Y .* (1 - pbi) .^ (1-Y) ./ (pai * pbi .^ Y .* (1 - pbi) .^ (1-Y) + (1-pai) * pci .^ Y .* (1 - pci) .^ (1-Y));
    pai = mean(mu);
    pbi = sum(mu .* Y) / sum(mu);
    pci = sum((1-mu) .* Y) / sum(1-mu);
    fprintf('%d: pa = %f, pb = %f, pc = %f\n', i, pai, pbi, pci);
end
