function svmStruct = mysvmtrain(X, Y, C)
    if length(X) ~= length(Y)
        fprintf('err');
    end
    
    m = length(X);
    svmStruct = struct('a',zeros(m,1),'b',0, 'X', X, 'Y', Y);

    maxiter = 1000;
    epsilon = 1e-4;
    
    alpha = zeros(m,1);
    b = 0;
    iter = 0;
    passes = 0;
    numpasses = 10;
    while iter < maxiter && passes < numpasses
        alphaChanged = 0;
        for i=1:m
            % out loop
            ei = g(alpha, b, X, Y, X(i,:)) - Y(i);
            if ((alpha(i)<C) && (ei<-epsilon)) || ((alpha(i)>0) && (ei>epsilon))
            % inner loop
                j = i;
                while j == i
                    j = randi(m);
                end
                ej = g(alpha, b, X, Y, X(j,:)) - Y(j);
                
                % inner update
                ai = alpha(i);
                aj = alpha(j);
                
                L = 0;
                H = C;
                
                if Y(i) == Y(j)
                    L = max(0, ai + aj - C);
                    H = min(C, ai + aj);
                else
                    L = max(0, aj - ai);
                    H = min(C, aj - ai + C);
                end
                
                if abs(H - L) < epsilon
                    continue;
                end
                
                eta = X(i)' * X(i) + X(j)' * X(j) - 2 * X(i)' * X(j);
                newaj = aj + Y(j) * (ei - ej) / eta;
                
                if newaj > H
                    newaj = H;
                elseif newaj < L
                    newaj = L;
                end
                        
                if abs(aj - newaj)<epsilon
                    continue;
                end
                
                alpha(j) = newaj;
                newai = alpha(i) + Y(i) * Y(j) * (alpha(j) - newaj);
                alpha(i) = newai;
                
                
                % update b
                Kii = X(i)' * X(i);
                Kjj = X(j)' * X(j);
                Kij = X(i)' * X(j);
                
                bi = -ei + b - Y(i) * Kii * (newai - ai) - Y(j) * Kij * (newaj - aj);
                bj = -ej + b - Y(j) * Kjj * (newaj - aj) - Y(i) * Kij * (newai - ai);
                b = (bi + bj)/2;
                
                if newai > 0 && newai < C
                    b = bi;
                end
                if newaj > 0 && newaj < C
                    b = bi;
                end
                
                alphaChanged = alphaChanged + 1;
                
            end
        end
        
        % fprintf('iter%d: %f\n',iter,b);
        iter = iter + 1;
        
        if alphaChanged == 0
            passes = passes + 1;
        else
            passes = 0;
        end
    end

    svmStruct.a = alpha;
    svmStruct.b = b;
end

function y =g(alpha,b, X, Y, x)
    y = (alpha .* Y)' * (X * x(:)) + b;
end