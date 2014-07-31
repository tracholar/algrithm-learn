function [bestStump, minError, bestClass] = buildStump(data, label, D)
    [m , n] = size(data);
    bestStump = {};
    bestClass = zeros(m,1);
    minError = inf;
    numSteps = 10;
    for i = 1:n
        rangemin = min(data(:,i));
        rangemax = max(data(:,i));
        stepSize = (rangemax - rangemin) / numSteps;
        
        for j = 0:numSteps
            threshVal = rangemin + j * stepSize;
            for inequal = {'lt', 'gt'}
                %% for each classifier
                pred = stumpClassify(data, i, threshVal, inequal);
                
                errors = ones(m, 1);
                errors(pred == label) = 0;
                weightedError = D' * errors;
                
%                 fprintf('min errror: %f\n', weightedError);
                if weightedError < minError
                    minError = weightedError;
                    bestClass = pred;
                    bestStump.idx = i;
                    bestStump.threshVal = threshVal;
                    bestStump.ineq = inequal;
                end
            end
        end
        
    end

end