function [J] = annCostFun(X,Y,theta,lambda)
    Theta1 = reshape(theta(1:20),5,4);
    Theta2 = reshape(theta(21:35),5,3);
    X = [ones(size(X,1),1) X];
    a1 = sigmoid(X * Theta1);
    a1 = [ones(size(a1,1),1) a1];
    a2 = sigmoid(a1 * Theta2);
    J = -sum(sum((Y .* log(a2) + (1-Y) .* log(1-a2)))) + lambda * sum(theta.^2);
    
    

end