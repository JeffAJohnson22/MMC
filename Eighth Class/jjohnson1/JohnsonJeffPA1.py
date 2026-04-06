"""
Project #1: Machine Learning vs Deep Learning
Name: Jeff Johnson
Date: 03/23/2026
"""

import time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score
import matplotlib.pyplot as plt

housing_data = fetch_california_housing()
X_raw = housing_data.data
y_raw = housing_data.target

threshold = np.percentile(y_raw, 70)
y_binary = (y_raw > threshold).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X_raw, y_binary, test_size=0.2, random_state=42, stratify=y_binary
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train_t = torch.tensor(X_train, dtype=torch.float32)
X_test_t = torch.tensor(X_test,  dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

BATCH_ML = 64
BATCH_DL = 128
EPOCHS = 20
LEARNING_RATE = 0.002

train_dataset = TensorDataset(X_train_t, y_train_t)
loader_ml = DataLoader(train_dataset, batch_size=BATCH_ML, shuffle=True)
loader_dl = DataLoader(train_dataset, batch_size=BATCH_DL, shuffle=True)

input_dim = X_train_t.shape[1]

class LogisticRegressionML(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.layer = nn.Linear(input_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(self.layer(x))

class DeepMLP(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

def train_model(model, loader, lr=LEARNING_RATE, epochs=EPOCHS):
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    train_losses = []
    start_train = time.time()

    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0
        for X_batch, y_batch in loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        train_losses.append(epoch_loss / len(loader))

    train_time = time.time() - start_train
    return train_losses, train_time

def evaluate_model(model, X_tensor, y_true_np):
    model.eval()

    start_inf = time.time()
    with torch.no_grad():
        outputs = model(X_tensor)
    latency_ms = ((time.time() - start_inf) / len(X_tensor)) * 1000

    y_probs = outputs.squeeze().numpy()
    y_pred = [1 if p >= 0.5 else 0 for p in y_probs]

    acc = accuracy_score(y_true_np, y_pred)
    auc = roc_auc_score(y_true_np, y_probs)

    return latency_ms, acc, auc


print("Fetching California Housing data...")
print("Running ML Benchmark (Logistic Regression)...")
ml_model = LogisticRegressionML(input_dim)
ml_losses, ml_train_time = train_model(ml_model, loader_ml)

print("Running DL Benchmark (Deep MLP)...")
dl_model = DeepMLP(input_dim)
dl_losses, dl_train_time = train_model(dl_model, loader_dl)

ml_latency, ml_acc, ml_auc = evaluate_model(ml_model, X_test_t, y_test)
dl_latency, dl_acc, dl_auc = evaluate_model(dl_model, X_test_t, y_test)

ml_params = sum(p.numel() for p in ml_model.parameters() if p.requires_grad)
dl_params = sum(p.numel() for p in dl_model.parameters() if p.requires_grad)

BAR = "========================================"
print()
print(BAR)
print()
print("MODEL COMPARISON RESULTS")
print()
print(BAR)
print(f"{'':20} {'Traditional ML':>15} {'Deep Learning':>15}")
print(f"{'Train Time (s)':<20} {ml_train_time:>15.5f} {dl_train_time:>15.5f}")
print(f"{'Inf. Latency (ms)':<20} {ml_latency:>15.5f} {dl_latency:>15.5f}")
print(f"{'Params':<20} {float(ml_params):>15.5f} {float(dl_params):>15.5f}")
print(f"{'Accuracy':<20} {ml_acc:>15.5f} {dl_acc:>15.5f}")
print(f"{'AUC-ROC':<20} {ml_auc:>15.5f} {dl_auc:>15.5f}")
print(BAR)
print()

epochs_range = range(1, EPOCHS + 1)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Convergence Comparison
ax1 = axes[0]
ax1.plot(epochs_range, ml_losses, label="Logistic Regression (ML)",
         color="red", marker="o", markersize=4)
ax1.plot(epochs_range, dl_losses, label="Deep MLP (DL)",
         color="orange", marker="s", markersize=4)
ax1.set_title("Convergence Comparison")
ax1.set_xlabel("Epoch")
ax1.set_ylabel("BCE Loss")
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.5)

# Predictive Performance
ax2 = axes[1]
labels = ["Logistic Regression (ML)", "Deep MLP (DL)"]
acc_vals = [ml_acc, dl_acc]
auc_vals = [ml_auc, dl_auc]
x = np.arange(len(labels))
bar_w = 0.35

ax2.bar(x - bar_w / 2, acc_vals, bar_w, label="Accuracy", color=["red", "orange"])
ax2.bar(x + bar_w / 2, auc_vals, bar_w, label="AUC-ROC",  color=["red", "orange"], alpha=0.55)
ax2.set_title("Predictive Performance")
ax2.set_xlabel("Model Type")
ax2.set_ylabel("Score")
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylim(0, 1.1)
ax2.legend()
ax2.grid(True, axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
