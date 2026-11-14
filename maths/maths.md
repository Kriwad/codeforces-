# CP Mathematics Reference

## 1. Vectors & Equilibrium (Sum Invariants)
- **Core Intuition**: When forces act across independent dimensions (X, Y, Z), equilibrium exists IF AND ONLY IF each dimension independently equals 0. You cannot combine axes into one scalar sum.
- **Click Example**: 3D Tug-of-war. Pulling forward (+X) balances pulling backward (-X). But if someone pulls upward (+Z), horizontal balance won't stop you from flying up. Balance on one axis never fixes imbalance on another.
- **Formula**: `sum(x) == 0 and sum(y) == 0 and sum(z) == 0`
- **Trap**: Summing `(x + y + z)` together. Example: `(-1, 1, 0)` sums to 0, but is NOT in equilibrium.
- **Problem**: CF 69A (Young Physicist)

---

## 2. Manhattan Distance & Grid Geometry
- **Core Intuition**: On a grid with only Up, Down, Left, Right movement, the shortest path between `(r1, c1)` and `(r2, c2)` is the horizontal steps plus vertical steps.
- **Click Example**: City Blocks. You cannot walk diagonally through buildings. To go from 1st Ave & 2nd St to 4th Ave & 6th St, you walk 3 avenues across, then 4 streets up. Total = `|1 - 4| + |2 - 6| = 3 + 4 = 7`.
- **Formula**: `Distance = |r1 - r2| + |c1 - c2|`. Center of 5x5 grid (1-indexed): `|r - 3| + |c - 3|`.
- **Trap**: Using Euclidean `sqrt((r1-r2)^2 + (c1-c2)^2)`. Diagonal steps take 2 moves on a grid, not $\sqrt{2}$.
- **Problem**: CF 263A (Beautiful Matrix)
