# Task 1 - installation check
# Installed all (in terminal): Anaconda3, PyTorch (pip install torch), TensorFlow (pip install tensorflow), VSCode, PyCharm

import sys
import importlib

print("python version:", sys.version.split()[0])
print()

libs = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "torch", "tensorflow", "nltk"]

for name in libs:
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, "__version__", "unknown version")
        print(f"[ok]      {name} {version}")
    except ImportError:
        print(f"[missing] {name}  -> pip install {name}")