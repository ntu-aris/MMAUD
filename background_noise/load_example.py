"""Inspect an original MMAUD background-noise array without modifying it."""
import argparse
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("path", help="Path to a downloaded .npy file")
args = parser.parse_args()
array = np.load(args.path, allow_pickle=False)
if array.ndim != 2 or array.shape[1] != 4 or array.dtype != np.float32:
    raise ValueError(f"Unexpected array format: {array.shape}, {array.dtype}")
print(f"shape={array.shape}, dtype={array.dtype}")
if array.size == 0:
    print("Empty source array; skip this file when building a batch.")
else:
    print(f"min={array.min():.6f}, max={array.max():.6f}, finite={np.isfinite(array).all()}")
