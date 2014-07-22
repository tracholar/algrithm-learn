function [J,grad] = annBPObj(X,Y,theta, lambda)
    Theta1 = reshape(theta(1:20),5,4);
    Theta2 = reshape(theta(21:35),5,3);
    X = [ones(size(X,1),1) X];
    z2 = X * Theta1;
    a2 = sigmoid(z2);
    a2 = [ones(size(a2,1),1) a2];
    z3 = a2 * Theta2;
    a3 = sigmoid(z3);
    J = -sum(sum((Y .* log(a3) + (1-Y) .* log(1-a3)))) + lambda/2 * (sum(theta.^2) - sum(Theta1(1,:).^2) - sum(Theta2(1,:).^2)) ;
    
    %% caculate the gradient of J using BP algorithm
    N = size(theta,1);
    grad = zeros(N,1);
    
    
    d3 = a3 - Y;
    d2 = d3 *Theta2' .* (1-a2) .* a2;
    
    t1 = Theta1;
    t2 = Theta2;
    t1(1,:) = 0;
    t2(1,:) = 0;
    g2 = a2' * d3 + lambda*t2;
    g1 = X' * d2(:,2:end) + lambda*t1;
    
    grad(:) = [g1(:);g2(:)];
    

end