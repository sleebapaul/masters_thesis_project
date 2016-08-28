%% ANN Training and Prediction - Thesis Project M. Tech 2016 - Sleeba Paul

clear ; close all; clc;

%% Initializing Parameters 
input_layer_size  = 5;  % For Input features 
hidden_layer_size = 50;   % 40 hidden units
num_labels = 5;          % 4 labels (States of Operation)
load('ex4data.mat');   % Loading the Features and Labels
num_points = length(X);
split_point = round(num_points*0.7);
seq = randperm(num_points);
X_train = X(seq(1:split_point),:);
Y_train = y(seq(1:split_point));
X_test = X(seq(split_point+1:end),:);
Y_test = y(seq(split_point+1:end));

fprintf('\nInitializing Neural Network Parameters ...\n')

initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

% Unroll parameters to pass to the advanced optimization techniques (fmincg) in MATLAB 
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

%%Training NN

fprintf('\nTraining Neural Network... \n')

%MaxIter can be increased to improve the accuracy and better parameter training
options = optimset('MaxIter', 200);

lambda = 0; % Useful for Over-Fitting situations. For current data its not needed.

% Create "short hand" for the cost function to be minimized
costFunction = @(p) nnCostFunction(p,input_layer_size,hidden_layer_size,num_labels, X_train, Y_train, lambda);

% Now, costFunction is a function that takes in only one argument (the neural network parameters)
[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)),hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end),num_labels, (hidden_layer_size + 1));

fprintf('Program paused. Press enter to continue.\n');
pause;


%% Visualize Weights 
fprintf('\nVisualizing Neural Network... \n')
fprintf ('\n Theta1 : \n');
disp(Theta1);
fprintf ('\n Theta2 : \n');
disp(Theta2);

%% Implement Predict 
%  After training the neural network, it can be used to predict the labels and compute the training set accuracy.
pred = predict(Theta1, Theta2,X_test);
disp(pred);
fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == Y_test)) * 100);


