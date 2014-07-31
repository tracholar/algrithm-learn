function ret = stumpClassify(data, idx, threshVal, threshIneq)
    ret = ones(length(data), 1);
    Y = data(:, idx);
    if strcmp(threshIneq , 'lt')
        ret(Y <= threshVal) = -1;
    else
        ret(Y > threshVal) = -1;
    end

end