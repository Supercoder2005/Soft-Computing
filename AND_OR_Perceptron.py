import math

input = [[0,0],[0,1],[1,0],[1,1]]
AND_out = [0,0,0,1]
OR_out = [0,1,1,1]

# Activation function
def sigmoid(z):
    return 1/(1+math.exp(-z))

def training(input,target):
    # initialize the parameters : weights & bias 
    w1,w2,b = 0.5,0.5,0.1
    learning_rate = 0.1
    for epoch in range(10000):
        for i in range(len(input)):
            x1,x2 = input[i]
            output = sigmoid(w1*x1 + w2*x2 + b)
            error = target[i] - output 
            w1 = w1 + (learning_rate*error*x1)
            w2 = w2 + (learning_rate*error*x2)
            b = b + (learning_rate*error)
    return w1,w2,b 

# AND Gate
print("--------AND----------")
w1,w2,b = training(input,AND_out)
for i in range(len(input)):
    x1,x2 = input[i]
    print(f"{x1} AND {x2} = {round(sigmoid(w1*x1 + w2*x2 +b))}")

# OR gate 
print("-----------OR-----------")
w1,w2,b = training(input,OR_out)
for i in range(len(input)):
    x1,x2 = input[i]
    print(f"{x1} OR {x2} = {round(sigmoid(w1*x1 + w2*x2 +b))}")