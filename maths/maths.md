# CP Mathematics Reference & Inventory

## 1. Vectors & Equilibrium (Sum Invariants)
- **Status**: Understood / Practised
- **Prerequisites**: 2D/3D Cartesian axes, basic vector components (x, y, z)
- **Core Intuition**: When forces act across independent dimensions (X, Y, Z), equilibrium exists IF AND ONLY IF each dimension independently equals 0. You cannot combine axes into one scalar sum.
- **Click Example**: 3D Tug-of-war: Pulling forward (+X) balances pulling backward (-X). But if someone pulls upward (+Z), horizontal balance won't stop you from flying up. Balance on one axis never fixes imbalance on another.
- **Formula**: `sum(x) == 0 and sum(y) == 0 and sum(z) == 0`
- **Trap**: Summing `(x + y + z)` together. Example: `(-1, 1, 0)` sums to 0, but is NOT in equilibrium.
- **Problem**: CF 69A (Young Physicist)

---

## 2. Manhattan Distance & Grid Centers
- **Status**: Understood / Practised
- **Prerequisites**: Absolute value |x|, 1D number line distance, 0-indexing vs 1-indexing
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
- **Status**: Understood / Practised
- **Prerequisites**: Bubble sort swap mechanism, permutations, contiguous subarrays
- **Core Intuition**: If you can reverse any subarray of length at most $k$, and $k \ge 2$, you have the power to swap ANY two adjacent elements ($k=2$). By Bubble Sort principles, adjacent swaps are sufficient to reach ANY permutation of an array.
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
- **Status**: Understood / Practised
- **Prerequisites**: Consecutive difference array a[i] - a[i-1], finding maximums
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
- **Status**: Understood / Practised
- **Prerequisites**: Pattern matching, substring search ('...' in s)
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
- **Status**: Understood / Practised
- **Prerequisites**: Modulo operator (%), division remainder theorem n = 3q + r
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
- **Status**: Understood / Practised
- **Prerequisites**: 0-indexed bounds, invariant tracking under constrained operations
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
- **Status**: Understood / Practised
- **Prerequisites**: Pigeonhole principle, frequency counting / hash map
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
- **Status**: Understood / Practised
- **Prerequisites**: Powers of 2 (2^k), exponential vs linear scale
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
- **Status**: Understood / Practised
- **Prerequisites**: Subsegment definition, mode / frequency
- **Core Intuition**: When a condition must hold on "at least one contiguous subsegment", test the smallest possible valid subsegment (length 1).
- **The Click Insight**: The 1-Element Subsegment: For $k$ to be the most frequent element, choose the subsegment $[k]$ of length 1. In $[k]$, $k$ has frequency 1 and every other number has frequency 0, so $k$ is trivially the winner. Thus, k is achievable if and only if $k$ exists anywhere in the array.
- **Formulas**:
  - `if k in a: "YES" else: "NO"`
- **Traps**:
  - Overcomplicating with sliding windows or hash maps when length 1 is always optimal.
- **Problem**: CF 1878A (How Much Does Daytona Cost?)

---

## 11. Zero-Sum Invariant (Conservation of Game Totals)
- **Status**: Understood / Practised
- **Prerequisites**: Symmetric binary interactions (+X and -X)
- **Core Intuition**: In closed exchange systems where every interaction gives $+X$ to one entity and $-X$ to another, the grand total across all participants is strictly 0.
- **The Click Insight**: Goals scored by team A are goals conceded by team B. Net efficiency change across the match is $(X - Y) + (Y - X) = 0$. Hence, the sum of all $n$ teams' efficiencies is strictly $0$. The missing team's value is simply `-sum(given)`.
- **Formulas**:
  - `missing = -sum(a)`
- **Traps**:
  - Simulating tournament games or tracking wins/losses.
- **Problem**: CF 1877A (Goals of Victory)

---

## 12. Concentric Grid Layers & Border Distance Invariant
- **Status**: Understood / Practised
- **Prerequisites**: 2D grid coordinates, distance to 4 boundaries
- **Core Intuition**: In an $N \times M$ grid, concentric layers or depth from perimeter are defined by the distance to the CLOSEST border: $\min(r, N - 1 - r, c, M - 1 - c)$.
- **The Click Insight**: Archery Target Rings: The 4 distances to the borders for cell $(r, c)$ are top ($r$), bottom ($9 - r$), left ($c$), right ($9 - c$). Point value is $1 + \min(r, 9 - r, c, 9 - c)$ in $O(1)$ without any 2D flood fill.
- **Formulas**:
  - `points = 1 + min(r, 9 - r, c, 9 - c)`
- **Traps**:
  - Precomputing arrays or running 2D BFS when $O(1)$ border distance gives the layer directly.
- **Problem**: CF 1873C (Target Practice)

---

## 13. Zero-Product Property & Distance to Origin
- **Status**: Understood / Practised
- **Prerequisites**: Zero-product rule ($a \times b = 0 \iff a = 0 \text{ or } b = 0$), absolute value $|x|$ on 1D line
- **Core Intuition**: A product of $N$ numbers is $0$ if and only if at least ONE element is $0$. To minimize $+1/-1$ steps to reach $0$, find the single element closest to $0$ (minimum absolute value).
- **The Click Insight**: Number Line Distance: The cost to reduce $x$ to $0$ using $+1/-1$ operations is strictly $|x|$. We only need ONE number to become $0$ to zero out the entire product. Therefore, $\text{min\_ops} = \min(|x| \text{ for } x \in a)$.
- **Formulas**:
  - $A_1 \times A_2 \times \dots \times A_N = 0 \iff \exists i \text{ such that } A_i = 0$
  - $\text{Cost to reduce } x \text{ to } 0 = |x|$
  - $\text{Minimum Operations} = \min(|x| \text{ for } x \in a)$
- **Traps**:
  - Looking for $\min(a)$ instead of $\min(|x|)$.
  - Using a `while` loop when $|x|$ gives the step count directly in $O(1)$.
- **Problem**: CF 1866A (Ambitious Kid)

---

## 14. Constructive Monotonic Stepping Stones
- **Status**: Understood / Practised
- **Prerequisites**: Inequality comparisons ($x \le y$ vs $x > y$), sequence reconstruction
- **Core Intuition**: When filtering elements by non-decreasing order ($a_i \ge a_{i-1}$), any downward step ($b_i < b_{i-1}$) would cause $b_i$ to be dropped. To force $b_i$ to be kept, insert a stepping-stone duplicate of $b_i$ right before it so that $b_i \ge b_i$ is satisfied.
- **The Click Insight**: Repairing a Drop: In $b = [4, 6, 3]$, going $6 \to 3$ is a drop ($3 < 6$). Inserting an extra $3$ produces $a = [4, 6, 3, 3]$. Under the filter rule, $4$ is kept, $6 \ge 4$ is kept, the first $3 < 6$ is dropped, and the second $3 \ge 3$ is kept! The reconstructed sequence exactly matches $b$.
- **Formulas**:
  - Start $a = [b[0]]$
  - For $i$ from $1$ to $\text{len}(b)-1$:
    - If $b_i \ge b_{i-1}$: `a.append(b[i])`
    - Else: `a.append(b[i]); a.append(b[i])`
- **Traps**:
  - Trying to find the original sequence uniquely instead of constructing any valid sequence within $2n$ length.
  - Printing Python list directly `print(a)` instead of space-separated integers `print(*a)`.
- **Problem**: CF 1862B (Sequence Game)

---

## 15. Strict Supremum Partition & Divisibility Invariant
- **Status**: Understood / Practised
- **Prerequisites**: Divisibility definition, size-order property ($y > x \implies y \nmid x$)
- **Core Intuition**: A strictly larger positive integer can NEVER divide a strictly smaller positive integer.
- **The Click Insight**: Isolating the Maximum: Put all copies of $\max(a)$ into array $c$, and all strictly smaller elements into array $b$. Since every element in $c$ is strictly greater than every element in $b$, no element of $c$ can ever divide any element of $b$. If $\min(a) == \max(a)$, impossible to partition $\implies -1$.
- **Formulas**:
  - If $\min(a) == \max(a)$: `return -1`
  - $c = [x \text{ for } x \in a \text{ if } x == \max(a)]$
  - $b = [x \text{ for } x \in a \text{ if } x \ne \max(a)]$
- **Traps**:
  - Putting only one copy of $\max(a)$ into $c$ when there are duplicates.
  - Confusing divisibility direction ($c_j \nmid b_i$).
- **Problem**: CF 1859A (United We Stand)

---

## 16. Combinatorial Games & Shared Pool Parity Reduction
- **Status**: Understood / Practised
- **Prerequisites**: Game theory normal play convention, parity (odd vs even)
- **Core Intuition**: When two players have private moves ($a, b$) and a shared pool of moves ($c$), optimal play exhausts the shared pool first to deny moves to the opponent.
- **The Click Insight**: Shared Pool Tie-Breaker: Alternating through $c$ shared buttons: if $c$ is odd, First player takes the last shared button, forcing Second player to burn private moves first (First wins if $a \ge b$). If $c$ is even, Second player takes the last shared button, forcing First to burn private moves first (First wins if $a > b$).
- **Formulas**:
  - If $c \pmod 2 == 1$: First wins iff $a \ge b$
  - If $c \pmod 2 == 0$: First wins iff $a > b$
  - Equivalent 1-liner: First wins iff $a + (c \pmod 2) > b$
- **Traps**:
  - Assuming players burn private moves first.
  - Summing all buttons without separating private from shared pools.
- **Problem**: CF 1858A (Buttons)

---

## 17. Parity Conservation of Partitions (Sum Parity Invariant)
- **Status**: Understood / Practised
- **Prerequisites**: Even/odd addition rules ($\text{even}+\text{even}=\text{even}$, $\text{odd}+\text{odd}=\text{even}$, $\text{even}+\text{odd}=\text{odd}$)
- **Core Intuition**: $\text{Total Sum} = \text{Part}_1 + \text{Part}_2$. Two partitions have the exact same parity (both even or both odd) if and only if their sum is strictly EVEN.
- **The Click Insight**: Coloring Red and Blue: If both sub-sums are even, sum is even. If both are odd, sum is odd + odd = even. Therefore, a valid coloring exists if and only if $\text{sum}(a) \pmod 2 == 0$. If total sum is odd, it is mathematically impossible to split into two numbers of the same parity.
- **Formulas**:
  - If `sum(a) % 2 == 0`: `"YES"`
  - Else: `"NO"`
- **Traps**:
  - Trying to simulate subset colorings with recursion/knapsack when sum parity gives the answer in $O(N)$.
- **Problem**: CF 1857A (Array Coloring)

---

## 18. Relative Convergence Rate & Integer Midpoint Ceiling
- **Status**: Understood / Practised
- **Prerequisites**: Integer division, relative speed of two converging points ($v_{rel} = 1 - (-1) = 2$), monotonicity check.
- **Core Intuition**: An array is unsorted as soon as there exists ANY pair of adjacent elements where $a[i] > a[i+1]$. By picking an index $i$, adding 1 to $a[1 \dots i]$ and subtracting 1 from $a[i+1 \dots n]$, the gap $(a[i+1] - a[i])$ decreases by exactly 2 in each operation.
- **The Click Insight**: To break sorted order fastest, target the adjacent pair with the minimum non-negative difference $d = a[i+1] - a[i]$. Each operation shrinks $d$ by 2. We need $a[i] > a[i+1]$, meaning $d$ must become strictly negative ($\le -1$). The number of operations needed is $\lfloor d / 2 floor + 1$. If the array is already not sorted, 0 operations are required.
- **Formulas**:
  - If array is already unsorted ($a[i] > a[i+1]$ for some $i$): $\text{ans} = 0$
  - Otherwise: $\text{ans} = \min_{1 \le i < n} \left( \lfloor \frac{a[i+1] - a[i]}{2} \rfloor + 1 \right)$
- **Traps**:
  - Overlooking that the array might already be unsorted initially (answer is 0).
  - Checking non-adjacent pairs: adjacent pairs always provide the tightest gap and fastest inversion.
- **Problem**: CF 1853A (Desorting)
