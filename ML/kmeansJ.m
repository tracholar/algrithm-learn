function J = kmeansJ(X, idx, C)
    [n, m] = size(X);
    [k, ~] = size(C);
    J = 0;
    for i=1:k
        J = J + norm(bsxfun(@minus,X(idx==i,:),C(i,:)));
    end
    J = J / sqrt(n);
end