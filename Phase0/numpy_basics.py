"""
Phase 0 — Topic 2: NumPy
Date: 2026-08-03 (rewritten — original had unverified/unprinted TODO section)
Author: Atomeo

KEY MENTAL MODEL:
    Stop thinking in loops. NumPy operations run on compiled C code under the hood.
    A vectorized operation on a 1M-element array is 10-100x faster than a Python loop.
    The goal: think in arrays, not elements.

RULE ENFORCED IN THIS FILE: every operation prints or asserts its own result.
No line exists here that you have to trust blindly.
"""

import numpy as np


# =============================================================================
# SECTION 1: Array Creation
# =============================================================================

array1 = np.array([1, 2, 3, 4])
print("array1:", array1, array1.dtype)          # int64 — inferred from int literals

array2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("array2:\n", array2)

array3 = np.zeros(3)
print("zeros:", array3, array3.dtype)            # float64 — see note in docstring above

array4 = np.ones(3)
print("ones:", array4, array4.dtype)

array5 = np.identity(3)
print("identity:\n", array5)

array6 = np.arange(0, 10)
assert list(array6) == list(range(10)), "arange mismatch"
print("arange:", array6)

array7 = np.linspace(0, 10, 5)
assert np.allclose(array7, [0.0, 2.5, 5.0, 7.5, 10.0]), "linspace mismatch"
print("linspace:", array7)


# =============================================================================
# SECTION 2: Indexing & Slicing
# =============================================================================

sliced = array2[::2]
assert np.array_equal(sliced, np.array([[1, 2, 3], [7, 8, 9]]))
print("slice [::2]:\n", sliced)


# =============================================================================
# SECTION 3: Array Metadata
# =============================================================================

print("shape:", array2.shape)   # (3, 3)
print("dtype:", array2.dtype)   # int64
print("ndim:", array2.ndim)     # 2
print("size:", array2.size)     # 9


# =============================================================================
# SECTION 4: Reshape, Flatten, Ravel — and proving view vs copy
# =============================================================================

reshaped = array2.reshape(1, 9)
print("reshaped:", reshaped)

flat_copy = array2.flatten()
flat_view = array2.ravel()

# Proof that flatten() is a copy and ravel() is a view:
flat_copy[0] = 999
flat_view[0] = -1
print("after mutating both — original array2 (only ravel's edit should show):\n", array2)
# Expect: top-left element is -1 (ravel mutated original), NOT 999 (flatten did not)
assert array2[0, 0] == -1, "ravel should be a view — original should have changed"
assert flat_copy[0] == 999 and array2[0, 0] != 999, "flatten should be a copy — original should NOT reflect this"

# reset for the rest of the file
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# =============================================================================
# SECTION 5: Vectorization
# =============================================================================

result = array1 + 10
assert list(result) == [11, 12, 13, 14]
print("vectorized +10:", result)


# =============================================================================
# SECTION 6: Broadcasting
# =============================================================================

col_bias = np.array([1, 2, 3])
broadcasted = array2 + col_bias
# Rule: NumPy aligns shapes from the right. (3,3) + (3,) -> the (3,) is
# treated as a row and repeated down every row of the (3,3) array.
expected = np.array([[2, 4, 6], [5, 7, 9], [8, 10, 12]])
assert np.array_equal(broadcasted, expected)
print("broadcast result:\n", broadcasted)


# =============================================================================
# SECTION 7: Boolean Indexing
# =============================================================================

gt5 = array2[array2 > 5]
even = array2[array2 % 2 == 0]
assert list(gt5) == [6, 7, 8, 9]
assert list(even) == [2, 4, 6, 8]
print("elements > 5:", gt5)
print("even elements:", even)


# =============================================================================
# SECTION 8: Axis Operations
# =============================================================================

col_sums = array2.sum(axis=0)   # collapse ROWS -> one value per column
row_sums = array2.sum(axis=1)   # collapse COLUMNS -> one value per row
assert list(col_sums) == [12, 15, 18]
assert list(row_sums) == [6, 15, 24]
print("sum axis=0 (per column):", col_sums)
print("sum axis=1 (per row):", row_sums)


# =============================================================================
# SECTION 9: Memory Layout
# =============================================================================

array_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')  # row-major (default)
array_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')  # column-major
print("C-order flags:", array_c.flags['C_CONTIGUOUS'], array_c.flags['F_CONTIGUOUS'])
print("F-order flags:", array_f.flags['C_CONTIGUOUS'], array_f.flags['F_CONTIGUOUS'])
assert array_c.flags['C_CONTIGUOUS'] and not array_c.flags['F_CONTIGUOUS']
assert array_f.flags['F_CONTIGUOUS'] and not array_f.flags['C_CONTIGUOUS']
# Why it matters: iterating along the wrong axis for a given layout causes
# cache misses (jumping around memory instead of reading sequentially) — slow code.


if __name__ == "__main__":
    print("\nAll assertions passed — every claim in this file is verified, not assumed.")
