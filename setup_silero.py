import torch

print("⏳ Downloading Silero punctuation model...")

# This downloads the model once and saves it to ~/.cache/torch/hub
torch.hub.load('snakers4/silero-models', 'silero_te')

print("✅ Silero punctuation model is now cached and ready to use!")