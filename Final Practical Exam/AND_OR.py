import math 

def sigmoid(z):
    return 1/(1+math.exp(-z))

def train(inputs,targets):
    w1,w2,b = 0.5,0.5,0.1
    learning_rate = 0.01
    for epoch in range(10000):
        for i in range(len(inputs)):
            x1,x2 = inputs[i]
            output = sigmoid(w1*x1 + w2*x2 + b)
            error = targets[i] - output
            w1 = w1 + (learning_rate*error*x1)
            w2 = w2 + (learning_rate*error*x2)
            b = b + (learning_rate*error)
    return w1,w2,b

inputs = [[0,0],[0,1],[1,0],[1,1]] 
AND_output = [0,0,0,1]
OR_output = [0,1,1,1]

print("AND Gate")
w1,w2,b = train(inputs,AND_output)
for i in range(len(inputs)):
    x1,x2 = inputs[i]
    print(f"{x1} AND {x2} = {round(sigmoid(w1*x1 + w2*x2 + b))}")

print("OR Gate")
w1,w2,b = train(inputs,OR_output)
for i in range(len(inputs)):
    x1,x2 = inputs[i]
    print(f"{x1} OR {x2} = {round(sigmoid(w1*x1 + w2*x2 + b))}")
