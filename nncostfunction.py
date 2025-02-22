import numpy as np
from sigmoid import *
import scipy.io as scio


def nn_cost_function(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lmd):
    # Reshape nn_params back into the parameters theta1 and theta2, the weight 2-D arrays
    # for our two layer neural network
    theta1 = nn_params[:hidden_layer_size * (input_layer_size + 1)].reshape(hidden_layer_size, input_layer_size + 1)
    theta2 = nn_params[hidden_layer_size * (input_layer_size + 1):].reshape(num_labels, hidden_layer_size + 1)

    # Useful value
    m = y.size

    # You need to return the following variables correctly
    cost = 0
    theta1_grad = np.zeros(theta1.shape)  # 25 x 401
    theta2_grad = np.zeros(theta2.shape)  # 10 x 26

    # ===================== Your Code Here =====================
    # Instructions : You should complete the code by working thru the
    #                following parts
    
    # Part 1 : Feedforward the neural network and return the cost in the
    #          variable cost. After implementing Part 1, you can verify that your
    #          cost function computation is correct by running ex4.py
    
    # Part 2: Implement the backpropagation algorithm to compute the gradients
    #         theta1_grad and theta2_grad. You should return the partial derivatives of
    #         the cost function with respect to theta1 and theta2 in theta1_grad and
    #         theta2_grad, respectively. After implementing Part 2, you can check
    #         that your implementation is correct by running checkNNGradients
    
    #         Note: The vector y passed into the function is a vector of labels
    #               containing values from 1..K. You need to map this vector into a
    #               binary vector of 1's and 0's to be used with the neural network
    #               cost function.
    
    #         Hint: We recommend implementing backpropagation using a for-loop
    #               over the training examples if you are implementing it for the
    #               first time.
    
    # Part 3: Implement regularization with the cost function and gradients.
    
    #         Hint: You can implement this around the code for
    #               backpropagation. That is, you can compute the gradients for
    #               the regularization separately and then add them to theta1_grad
    #               and theta2_grad from Part 2.
    

    Y = np.zeros((m, num_labels))
    for i in range(m):
        Y[i, y[i] - 1] = 1

    a1 = np.c_[np.ones(m), X]
    a2 = np.c_[np.ones(m), sigmoid(np.dot(a1, theta1.T))]
    h = sigmoid(np.dot(a2, theta2.T))

    reg_theta1 = theta1[:, 1:] # 25 * 400
    reg_theta2 = theta2[:, 1:] # 10 * 25

    cost = np.sum(-Y * np.log(h) - np.subtract(1, Y) * np.log(np.subtract(1, h))) / m \
            + lmd *(np.sum(np.dot(reg_theta1, reg_theta1.T)) + (np.sum(np.dot(reg_theta2, reg_theta2.T)))) / (2 * m)


    sigma3 = h - Y
    sigma2 = np.dot(sigma3, theta2) * a2 * (np.subtract(1, a2))
    sigma2 = sigma2[:, 1:]
    
    detal1 = np.dot( a1.T, sigma2)
    detal2 = np.dot(a2.T, sigma3)

    theta1_grad = (lmd/m) * theta1.T + detal1 / m
    theta2_grad = (lmd/m) * theta2.T + detal2 / m 

    # ====================================================================================
    # Unroll gradients
    grad = np.concatenate([theta1_grad.flatten(), theta2_grad.flatten()])

    return cost, grad

data = scio.loadmat("ex4data1.mat")
Y = data['y']
X= data['X']
theta = scio.loadmat("ex4weights.mat")
theta1 = theta['Theta1'][:, 1:]
print(X[0].shape)
x = np.c_[np.ones(Y.size), X]
print(x[0])
print(x[0].shape)

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test)  = mnist.load_data()

print(x_test.shape)
print(x_test[0])