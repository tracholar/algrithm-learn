Jerr = zeros(9,1);
for k = 2:10
    [idx0, C0] = mykmeans(X,k);
    J0 = kmeansJ(X, idx0, C0);

    for i=1:50
        [idx, C] = mykmeans(X,k);
        J = kmeansJ(X, idx, C);
        if J < J0
            J0 = J;
            idx0 = idx;
            C0 = C;
        end
    end

    Jerr(k-1) = J0;
end
close all;
figure;
plot(2:10,Jerr,'.-');