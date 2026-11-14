# CP Mathematics Reference

## 1. Vectors & Equilibrium (Sum Invariants)
- **Core Intuition**: When forces act across independent dimensions (X, Y, Z), equilibrium exists IF AND ONLY IF each dimension independently equals 0. You cannot combine axes into one scalar sum.
- **Click Example**: 3D Tug-of-war. Pulling forward (+X) balances pulling backward (-X). But if someone pulls upward (+Z), horizontal balance won't stop you from flying up. Balance on one axis never fixes imbalance on another.
- **Formula**: `sum(x) == 0 and sum(y) == 0 and sum(z) == 0`
- **Trap**: Summing `(x + y + z)` together. Example: `(-1, 1, 0)` sums to 0, but is NOT in equilibrium.
- **Problem**: CF 69A (Young Physicist)

---

## 2. Manhattan Distance & Grid Centers
- **Core Intuition**: Grid movement (Up, Down, Left, Right) is orthogonal. The 2D matrix splits into two completely independent 1D number lines: row moves and column moves.
- **The Click Insight**: The distance formula is simply `|current_point - target_point|`. Bringing any item to the matrix center is not a 2D puzzle—it is simply finding the middle coordinates `(mid_r, mid_c)` and deducting: `|r - mid_r| + |c - mid_c|`.
- **Formulas**:
  - General Manhattan Distance: `Distance = |r1 - r2| + |c1 - c2|`
  - 1-indexed Center of $N \times M$ grid: `mid_r = (N + 1) // 2`, `mid_c = (M + 1) // 2`
  - 0-indexed Center of $N \times M$ grid: `mid_r = N // 2`, `mid_c = M // 2`
  - For $5 \times 5$ Grid (1-indexed): Center is `(3, 3)` $\to$ `Moves = |r - 3| + |c - 3|`
- **Traps**:
  - Index Mismatch: Deducting from `(3, 3)` when loops run `0` to `4`. If loops are 0-indexed, deduct from `(2, 2)` or add `+1` to row and col.
  - Forgetting absolute value: Distance is always positive; always use `abs()`.
- **Problem**: CF 263A (Beautiful Matrix)

---

## 3. Bubble Sort Invariance (Neighbor Swaps)
- **Core Intuition**: If you can reverse any subarray of length at most $k$, and $k \ge 2$, you can swap ANY two adjacent elements ($k=2$). By Bubble Sort principles, adjacent swaps can sort ANY array in the world.
- **The Click Insight**: You don't need to actually simulate the sorting. $k$ is your "spatula size". With $k \ge 2$ you can swap neighbors and sort anything (always YES). With $k = 1$, flipping 1 element changes nothing (stuck!), so it's YES only if already sorted.
- **Formulas**:
  - If $k \ge 2$: Always `"YES"`
  - If $k == 1$: `"YES"` only if `all(a[i] <= a[i+1] for i in range(n-1))`
- **Traps**:
  - Overcomplicating by trying to actually simulate subarray reversals.
  - Confusing $k$ (subarray flip limit) with the size of the whole array $n$.
- **Problem**: CF 1903A (Halloumi Boxes)
