function [J, grad] = annObj(X,Y,theta, lambda)
    J = annCostFun(X,Y,theta,lambda);
    epsilon = 1e-6;
    N = size(theta,1);
    grad = zeros(N,1);
    dt = zeros(size(theta));
    for i=1:N
        dt(:) = zeros(size(theta));
        dt(i) = epsilon;
        J1 = annCostFun(X,Y,theta+dt,lambda);
        J2 = annCostFun(X,Y,theta-dt,lambda);
        grad(i) = (J1-J2)/2/epsilon;
    
    end

end