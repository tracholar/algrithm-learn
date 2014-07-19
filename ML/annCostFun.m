function [J] = annCostFun(X,Y,Theta1,Theta2)
    X = [ones(size(X,1),1) X];
    a1 = sigmoid(X * Theta1);
    a1 = [ones(size(a1,1),1) a1];
    a2 = sigmoid(a1 * Theta2);
    J = -sum(sum((Y .* log(a2) + (1-Y) .* log(1-a2))));
    

end