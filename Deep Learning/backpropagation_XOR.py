import math 

inputs = [[0,0],[0,1],[1,0],[1,1]]
XOR_out = [0,1,1,0]

# define the activation function
def sigmoid(z):
    return 1/(1+math.exp(-z))

# initializing the weights and biases
w1,w2,w3,w4 = 0.5,0.2,0.8,0.1
w5,w6 = 0.2,0.6
b1,b2,b3 = 0.1,0.1,0.1
learning_rate = 0.5
    
# training of the parameters
for epoch in range(100000):
    for i in range(len(inputs)):
        x1,x2 = inputs[i]
        
        # output of each layer
        h1 = sigmoid(x1*w1 + x2*w2 + b1)
        h2 = sigmoid(x1*w3 + x2*w4 +b2)
        o = sigmoid(h1*w5 + h2*w6 +b3)

        # final output
        error = XOR_out[i] - o 

        # delta of final output
        delta_o = error*o*(1-o)
        
        # delta of hidden layers
        delta_h1 = delta_o*w5*h1*(1-h1)
        delta_h2 = delta_o*w6*h2*(1-h2)

        # update the weights and bias
        w1 = w1+(learning_rate*delta_h1*x1)
        w2 = w2+(learning_rate*delta_h1*x1)
        b1 = b1+(learning_rate*delta_h1)

        w3 = w3+(learning_rate*delta_h2*x2)
        w4 = w4+(learning_rate*delta_h2*x2)
        b2 = b2+(learning_rate*delta_h2)

        w5 = w5+(learning_rate*delta_o*h1)
        w6 = w6+(learning_rate*delta_o*h2)
        b3 = b3+(learning_rate*delta_o)

for i in range(len(inputs)):
    x1,x2 = inputs[i]
    h1 = sigmoid(w1*x1 + w2*x2 + b1)
    h2 = sigmoid(w3*x1 + w4*x2 + b2)
    print(f"{x1}XOR{x2} = {round(sigmoid(h1*w5 + h2*w6 +b3))}")
