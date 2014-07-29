%% read data

f = fopen('iris.data','r');
data = textscan(f,'%f %f %f %f %s','Delimiter',',');
fclose(f);

X = cell2mat(data(1:4));
Y = zeros(length(data{5}),1);
Y(strcmp(data{5},'Iris-setosa'))=0;
Y(strcmp(data{5},'Iris-versicolor'))=1;
Y(strcmp(data{5},'Iris-virginica'))=2;
m = length(X);


%% prepare data
y = zeros(m,1);
y(Y==1) = 1;
y(Y~=1) = -1;

%% train svm
% kernel function: linear quadratic polynomial(polyorder)  rbf(rbf_sigma)
% mlp 
svmStruct = svmtrain(X, y,'kernel_function', 'rbf', 'rbf_sigma',.75 );
group = svmclassify(svmStruct, X);
fprintf('train error is %f\n', 1-mean(group==y));

