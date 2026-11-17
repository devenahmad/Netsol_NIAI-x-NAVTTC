# Task 42 - pandas installation (pip install pandas)
# this script checks that it's installed and working.

try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. run:  pip install pandas")
    raise SystemExit

print("pandas is installed, version", pd.__version__)

mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2],
}
myvar = pd.DataFrame(mydataset)
print(myvar)

import numpy as np
print("numpy version", np.__version__)