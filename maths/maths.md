# CP Mathematics Reference

## 1. Vectors & Equilibrium (Sum Invariants)
- **Core Intuition**: When forces act across independent dimensions (X, Y, Z), equilibrium exists IF AND ONLY IF each dimension independently equals 0. You cannot combine axes into one scalar sum.
- **Click Example**: 3D Tug-of-war. Pulling forward (+X) balances pulling backward (-X). But if someone pulls upward (+Z), horizontal balance won't stop you from flying up. Balance on one axis never fixes imbalance on another.
- **Formula**: `sum(x) == 0 and sum(y) == 0 and sum(z) == 0`
- **Trap**: Summing `(x + y + z)` together. Example: `(-1, 1, 0)` sums to 0, but is NOT in equilibrium.
- **Problem**: CF 69A (Young Physicist)

---

## 2. Manhattan Distance & Grid Centers
- **Core Intuition**: Grid movement (Up, Down, Left, Right) is orthogonal. The 2D matrix splits into two independent 1D number lines: row moves and column moves.
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
- **Core Intuition**: If you can reverse any subarray of length at most $k$, and $k \ge 2$, you have the power to swap ANY two adjacent elements ($k=2$). By Bubble Sort principles, adjacent swaps can sort ANY array in the world.
- **The Click Insight**: You don't need to actually simulate the sorting. $k$ is your "spatula size". With $k \ge 2$ you can swap neighbors and sort anything (always YES). With $k = 1$, flipping 1 element changes nothing (stuck!), so it's YES only if already sorted.
- **Formulas**:
  - If $k \ge 2$: Always `"YES"`
  - If $k == 1$: `"YES"` only if `all(a[i] <= a[i+1] for i in range(n-1))`
- **Traps**:
  - Overcomplicating by trying to actually simulate subarray reversals.
  - Confusing $k$ (subarray flip limit) with the size of the whole array $n$.
- **Problem**: CF 1903A (Halloumi Boxes)

---

## 4. Worst-Case Bottleneck & Turnaround Distances
- **Core Intuition**: When a resource (gas tank) fully refills at discrete checkpoints, the required capacity is determined solely by the single largest gap (the bottleneck) between consecutive refills.
- **The Click Insight**: A destination without a refill requires a round-trip stretch: from the last station to destination and back. That stretch is doubled: $2 \times (x - a[-1])$. The tank must be at least as large as the worst-case stretch on the entire road.
- **Formulas**:
  - Start gap: $a[0] - 0 = a[0]$
  - Between stations: $a[i] - a[i - 1]$ for $i \in [1, n-1]$
  - Turnaround gap: $2 \times (x - a[-1])$
  - Required Capacity: $\max(\text{all gaps})$
- **Traps**:
  - Forgetting to double the final stretch: there is no station at destination $x$.
  - Off-by-one errors when computing differences.
- **Problem**: CF 1901A (Line Trip)

---

## 5. Infinite Generator Invariant (Classification vs Simulation)
- **Core Intuition**: When an operation allows unlimited free actions once an activation pattern is met, do not simulate the process. Classify whether the pattern exists.
- **The Click Insight**: Minecraft Infinite Water Source: 3 consecutive dots `...` allow 2 coins to trigger infinite free refills (answer is always 2). Without `...`, you must pay 1 coin for every single dot.
- **Formulas**:
  - If `"..."` in `s`: `return 2`
  - Else: `return s.count(".")`
- **Traps**:
  - Simulating neighbor lookups instead of binary condition matching.
- **Problem**: CF 1900A (Cover in Water)

---

## 6. Modular Game Symmetries (Immediate Win vs Symmetric Stall)
- **Core Intuition**: In turn-based games where players add or subtract 1 to reach a target multiple, check if the first player is already adjacent to a winning target.
- **The Click Insight**: If $n$ is not a multiple of 3, it is only 1 step away from one. Vanya wins immediately on move 1 (`First`). If $n$ is already a multiple of 3, Vanya must leave it, and Vova can mirror or undo moves to keep Vanya from winning (`Second`).
- **Formulas**:
  - If `n % 3 != 0`: `"First"`
  - Else: `"Second"`
- **Traps**:
  - Simulating 10 turns.
- **Problem**: CF 1899A (Game with Integers)

---

## 7. Permutation Invariants & Frozen Indices (Jagged Swaps)
- **Core Intuition**: When constrained swaps are allowed infinitely many times, find which position CAN NEVER be modified (the frozen invariant). In a permutation of $1 \dots n$, the first position must contain $1$.
- **The Click Insight**: Swaps only occur at indices $i$ with neighbors ($i \ge 1$ in 0-indexing). Index 0 is NEVER touched. If $a[0] \neq 1$, $1$ can never reach the front, so sorting is impossible (`NO`). If $a[0] == 1$, all larger values can bubble rightwards over peaks (`YES`).
- **Formulas**:
  - If `a[0] == 1`: `"YES"`
  - Else: `"NO"`
- **Traps**:
  - Writing complex peak-detection simulation loops instead of checking index 0 reachability.
- **Problem**: CF 1896A (Jagged Swaps)

---

## 8. Alternating Parity & Pigeonhole Count Balance
- **Core Intuition**: An array with constant adjacent sums ($a[i] + a[i+1] == k$) requires elements to repeat every two steps ($a[i] == a[i+2]$). Thus, the array must alternate between at most two distinct values: $[X, Y, X, Y, \dots]$.
- **The Click Insight**: Seating Boys and Girls: To alternate strictly without two boys or two girls touching, either their counts are equal ($|c_1 - c_2| == 0$) or one count has at most 1 extra to cover both ends ($|c_1 - c_2| == 1$). If difference $\ge 2$, by Pigeonhole Principle two identical elements must touch.
- **Formulas**:
  - If `len(distinct) == 1`: `"YES"`
  - If `len(distinct) == 2 and abs(c1 - c2) <= 1`: `"YES"`
  - Else: `"NO"`
- **Traps**:
  - Checking `a[i] == a[i+2]` on the input directly without rearranging.
  - Using dictionary keys as indices (e.g. `seen[0]`) instead of `seen.values()`.
- **Problem**: CF 1890A (Doremy's Paint 3)

---

## 9. Exponential Doubling & Bounded Search
- **Core Intuition**: When a string doubles at each step ($x = x + x$), its length grows exponentially ($2^k$). For small limits ($n, m \le 25$), at most 5 or 6 doublings are possible before the string exceeds the target length plus overlap.
- **The Click Insight**: In just 5 steps, 1 character grows to 32 characters, and 6 steps to 64. If $s$ does not appear within 6 doublings, it will never appear.
- **Formulas**:
  - Loop at most 6 times: check `if s in x`, then `x = x + x`
  - If found: `return step`
  - Else: `return -1`
- **Traps**:
  - `sys.stdin.readline` keeps `\n`! Always use `.strip()` when reading strings.
- **Problem**: CF 1881A (Don't Try to Count)

---

## 10. Extremal Principle / Minimal Subsegment Reduction
- **Core Intuition**: When a condition must hold on "at least one contiguous subsegment", test the smallest possible valid subsegment (length 1).
- **The Click Insight**: The 1-Element Subsegment: For $k$ to be the most frequent element, choose the subsegment $[k]$ of length 1. In $[k]$, $k$ has frequency 1 and every other number has frequency 0, so $k$ is trivially the winner. Thus, possible iff $k$ is in the array.
- **Formulas**:
  - `if k in a: "YES" else: "NO"`
- **Traps**:
  - Overcomplicating with sliding windows or hash maps when length 1 is always optimal.
- **Problem**: CF 1878A (How Much Does Daytona Cost?)
