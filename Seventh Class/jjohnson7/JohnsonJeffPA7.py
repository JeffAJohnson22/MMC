"""
Project #7: The Neural Thermostat Agent 
Name: Jeff Johnson
Date: 02/28/2026
"""

# Objective:
# You are building the “brain” of a Smart Home Thermostat. The agent’s goal is to decide whether to turn the Air Conditioning ON (1) or OFF (0) based on two environmental factors:

#     Indoor Temperature (scaled 0-1)
#     Number of People in the room (scaled 0-1)

# Your task is to manually implement a single-neuron neural network (Perceptron) from scratch that acts as an intelligent decision-maker.

# You are provided with the NeuralThermostat class skeleton. Your job is to complete three main methods:

#     sigmoid(z)
#         Implement the sigmoid activation function: σ(z) = 1 / (1 + e^-z)
#         Maps the raw weighted input to a value between 0 and 1, representing confidence in whether the AC should be ON.
#     predict(x1, x2)
#         Implement the forward pass: compute the weighted sum z = x1*w1 + x2*w2 + bias, then pass it through the sigmoid.
#         Returns a probability between 0 and 1 for the AC being ON.
#     train(X, y, epochs)
#         Implement gradient descent to adjust w1, w2, and bias based on prediction errors.
#         For each training example:
#             Compute the predicted probability (predict)
#             Calculate error as (prediction - target)
#             Update weights and bias:
#             w1 -= learning_rate * error * x1
#             w2 -= learning_rate * error * x2
#             bias -= learning_rate * error
#         Track the mean squared error (MSE) per epoch in a list called losses.

import numpy as np

import matplotlib.pyplot as plt


class NeuralThermostat:
    def __init__(self):

        # Initializing with fixed values for reproducible results in solution
        # In practice, np.random.randn() is used.
        self.w1 = 0.5
        self.w2 = -0.2
        self.bias = 0.0
        self.learning_rate = 0.5 # Higher learning rate for faster convergence on small data

      
    def sigmoid(self, z):

        # TASK 1: Implement the Sigmoid Activation Function
        # Formula: 1 / (1 + e^-z)
        # Hint: Use np.exp(-z) for the exponential part
        pass 

    

    def predict(self, x1, x2):
        # TASK 2: Implement the Feedforward Pass
        # 1. Calculate Z using the formula: (x1 * w1) + (x2 * w2) + b
        # 2. Pass Z through your sigmoid function and return the result
        pass

 

    def train(self, X, y, epochs=2000):
        losses = []
        for epoch in range(epochs):
            total_loss = 0
            for i in range(len(X)):
                x1, x2 = X[i]
                target = y[i]
                # --- TASK 3: THE TRAINING ENGINE ---
                # 1. Get the current prediction (Call your predict function)
                # prob = ...
                # 2. Calculate the Error (The difference between prediction and target)
                # error = ...
                # 3. Update the weights and bias (Gradient Descent)
                # Formula: Weight = Weight - (Learning_Rate * Error * Input)
                # self.w1 = ...
                # self.w2 = ...
                # self.bias = ... (Hint: The 'input' for bias is always 1)
                # 4. Record the Squared Error for the loss chart
                # total_loss += (error ** 2)
                pass 
            # Keep track of the average loss for this epoch
            losses.append(total_loss / len(X))
        return losses
# Features: [Temperature (0-1), PeopleCount (0-1)]
# Targets: 1 (AC On), 0 (AC Off)
X_train = np.array([
    [0.1, 0.1], # Cold & Empty -> Off (0)
    [0.9, 0.2], # Hot & Few people -> On (1)
    [0.5, 0.8], # Warm & Crowded -> On (1)
    [0.2, 0.9]  # Cold & Crowded -> Off (0)
])

y_train = np.array([0, 1, 1, 0])

# --- EXECUTION ---

agent = NeuralThermostat()

print("--- Before Training ---")
print(f"Initial Weights: w1={agent.w1:.2f}, w2={agent.w2:.2f}, b={agent.bias:.2f}")

# Test prediction for [Hot, Few People]
initial_pred = agent.predict(0.9, 0.2)
print(f"Prediction for [0.9, 0.2]: {initial_pred if initial_pred is not None else 'No Output Yet'}")

# Train the agent
print("\nTraining in progress...")
history = agent.train(X_train, y_train)
print("\n--- After Training ---")
print(f"Final Weights: w1={agent.w1:.2f}, w2={agent.w2:.2f}, b={agent.bias:.2f}")
final_pred = agent.predict(0.9, 0.2)
print(f"Prediction for [0.9, 0.2]: {final_pred if final_pred is not None else 'No Output Yet'}")

 if history:
    plt.figure(figsize=(10, 5))
    plt.plot(history, color='blue', linewidth=2)
    plt.title("Neural Agent Learning Curve", fontsize=14)
    plt.xlabel("Epochs", fontsize=12)
    plt.ylabel("Mean Squared Error (Loss)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()