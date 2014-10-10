function [idx, C] = mykmeans(X, k)
    [n, m] = size(X);
    idx = zeros(n,1);
    C = X(randi([1,n],k,1), :);
    Cold = C;
    
%     fprintf('%f ', C);
%     fprintf('\n');
        
    maxIter = 100;
    for iter = 1:maxIter
        for i=1:n
            minj = 1;
            dj = norm(X(i,:) - C(1,:));

            for j=2:k
                d = norm(X(i,:) - C(j,:));
                if d < dj
                    dj = d;
                    minj = j;
                end
            end

            idx(i) = minj;
        end
        
        Cold = C;
        for j=1:k
            if sum(idx==j) == 0
                continue;
            end
            C(j,:) = mean(X(idx==j, :));
        end
        
%         fprintf('%f ', C);
%         fprintf('\n');
        if norm(Cold - C) < 1e-6
            break;
        end
        
    end
end