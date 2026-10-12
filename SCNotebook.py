import sys
import tensorflow as tf

# ADDED: verify VS Code is using our WSL Python rather than Windows Python
print("Python:", sys.executable)

# ADDED: verify the TensorFlow environment
print("TensorFlow:", tf.__version__)

# ADDED: verify that the RTX 5070 is visible to this notebook kernel
print("GPUs:", tf.config.list_physical_devices("GPU"))