import math
import random

# Activation function and its derivative
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def sigmoid_derivative(output):
    # If output = sigmoid(z), then derivative is output * (1 - output)
    return output * (1 - output)

def train_xor(inputs, targets):
    # Seed random for reproducibility
    random.seed(42)

    # 1. Initialize Weights and Biases randomly
    # Hidden Layer (2 neurons, each with 2 inputs)
    w_h11, w_h12, b_h1 = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)
    w_h21, w_h22, b_h2 = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)

    # Output Layer (1 neuron with 2 inputs from hidden layer)
    w_o1, w_o2, b_o = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)

    learning_rate = 0.5  # Higher learning rate helps MLPs converge faster
    epochs = 20000

    for epoch in range(epochs):
        for i in range(len(inputs)):
            x1, x2 = inputs[i]
            target = targets[i]

            # --- FORWARD PASS ---
            # Hidden Layer Outputs
            out_h1 = sigmoid(x1 * w_h11 + x2 * w_h12 + b_h1)
            out_h2 = sigmoid(x1 * w_h21 + x2 * w_h22 + b_h2)

            # Final Output
            final_output = sigmoid(out_h1 * w_o1 + out_h2 * w_o2 + b_o)

            # --- BACKPROPAGATION ---
            # 1. Error at Output Layer
            error_output = target - final_output
            delta_output = error_output * sigmoid_derivative(final_output)

            # 2. Error at Hidden Layer (Backpropagating the delta)
            error_h1 = delta_output * w_o1
            delta_h1 = error_h1 * sigmoid_derivative(out_h1)

            error_h2 = delta_output * w_o2
            delta_h2 = error_h2 * sigmoid_derivative(out_h2)

            # --- WEIGHT UPDATES ---
            # Update Output Layer
            w_o1 += learning_rate * delta_output * out_h1
            w_o2 += learning_rate * delta_output * out_h2
            b_o  += learning_rate * delta_output

            # Update Hidden Layer 1
            w_h11 += learning_rate * delta_h1 * x1
            w_h12 += learning_rate * delta_h1 * x2
            b_h1  += learning_rate * delta_h1

            # Update Hidden Layer 2
            w_h21 += learning_rate * delta_h2 * x1
            w_h22 += learning_rate * delta_h2 * x2
            b_h2  += learning_rate * delta_h2

    return w_h11, w_h12, b_h1, w_h21, w_h22, b_h2, w_o1, w_o2, b_o

# Dataset
inputs = [[0,0], [0,1], [1,0], [1,1]]
XOR_out = [0, 1, 1, 0]

# Train the network
w_h11, w_h12, b_h1, w_h21, w_h22, b_h2, w_o1, w_o2, b_o = train_xor(inputs, XOR_out)

# Testing the trained network
print("XOR Gate Results:")
print("-" * 20)
for i in range(len(inputs)):
    x1, x2 = inputs[i]

    # Forward pass logic for validation
    out_h1 = sigmoid(x1 * w_h11 + x2 * w_h12 + b_h1)
    out_h2 = sigmoid(x1 * w_h21 + x2 * w_h22 + b_h2)
    final_output = sigmoid(out_h1 * w_o1 + out_h2 * w_o2 + b_o)

    print(f"{x1} XOR {x2} = {round(final_output)}  (Raw probability: {final_output:.4f})")