function Y = mysvmclassify(svmStruct, data)
    alpha = svmStruct.a;
    b = svmStruct.b;
    X = svmStruct.X;
    label = svmStruct.Y;
    
    S = (alpha .* label)' * X * data' + b;
    Y = zeros(length(data),1);
    Y(S>0) = 1;
    Y(S<=0) = -1;
end