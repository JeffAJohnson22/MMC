"""
Project #7: The Neural Thermostat Agent 
Name: Jeff Johnson
Date: 02/28/2026
"""

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
        return 1 / (1 + np.exp(-z))

    def predict(self, x1, x2):
        z = (x1 * self.w1) + (x2 * self.w2) + self.bias
        return self.sigmoid(z)

    def train(self, X, y, epochs=2000):
        losses = []
        for epoch in range(epochs):
            total_loss = 0
            for i in range(len(X)):
                x1, x2 = X[i]
                target = y[i]
                prob = self.predict(x1, x2)
                error = prob - target
                self.w1 -= self.learning_rate * error * x1
                self.w2 -= self.learning_rate * error * x2
                self.bias -= self.learning_rate * error
                total_loss += (error ** 2)
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