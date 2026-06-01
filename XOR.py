import math 
import random 

input = [[0,0],[0,1],[1,0],[1,1]]
XOR_out = [0,1,1,0]

# Activation function
def sigmoid(z):
    return 1/(1+math.exp(-z))

# Derivative of sigmoid function
def derivative_sigmoid(sigma):
    return sigma*(1-sigma)

# train the MLP --> There are two input nodes x1,x2 ; two hidden nodes h1,h2 ; one output node o
# from x1 -> h1 : weight w1, from x2 -> h1 : weight w2
# from x1 -> h2 : weight w3, from x2 -> h2 : weight w4
# from h1 -> o : weight w5, from h2 -> o : weight w6 
# biases b1(for h1), b2(for h2), b3(for o)

def training(input,target):
    # initialize the weights and biases randomly 
    random.seed(42)
    w1,w2,b1 = random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)
    w3,w4,b2 = random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)
    w5,w6,b3 = random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)
    learning_rate = 0.5

    for epoch in range(20000):
        for i in range(len(input)):
            x1,x2 = input[i]

            # Forward Propagation
            # 1. Output of hidden layer nodes h1, h2
            h1 = sigmoid(w1*x1 + w2*x2 + b1)
            h2 = sigmoid(w3*x1 + w4*x2 + b2)
            # 2. Final Output of output layer node o 
            o = sigmoid(w5*h1 + w6*h2 + b3)

            # Error Calculation 
            error = target[i] - o 

            # Delta calculation -- Back Propagation
            # 1. Delta of final output 
            delta_o = error*derivative_sigmoid(o)
            # 2. Delta of hidden layer's output
            delta_h1 = delta_o*derivative_sigmoid(h1)
            delta_h2 = delta_o*derivative_sigmoid(h2)

            # Weights and bias update
            w1 = w1 + (learning_rate*delta_h1*x1)
            w2 = w2 + (learning_rate*delta_h1*x1)
            b1 = b1 + (learning_rate*delta_h1)

            w3 = w3 + (learning_rate*delta_h2*x2)
            w4 = w4 + (learning_rate*delta_h2*x2)
            b2 = b2 + (learning_rate*delta_h2)

            w5 = w5 + (learning_rate*delta_o*h1)
            w6 = w6 + (learning_rate*delta_o*h2)
            b3 = b3 + (learning_rate*delta_o)
    return w1,w2,b1,w3,w4,b2,w5,w6,b3

w1,w2,b1,w3,w4,b2,w5,w6,b3 = training(input,XOR_out)
for i in range(len(input)):
    x1,x2 = input[i]
    h1 = sigmoid(w1*x1 + w2*x2 + b1)
    h2 = sigmoid(w3*x1 + w4*x2 + b2)
    print(f"{x1} XOR {x2} = {round(sigmoid(w5*h1 + w6*h2 + b3))}")




