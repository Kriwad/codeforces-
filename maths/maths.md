# 📐 The Competitive Programming Math Vault

Welcome to your personalized Math Vault. Every mathematical technique, concept, or trick we learn during our journey will be documented here with its core intuition, the exact "click" example that made it make sense, and quick reference formulas.

---

## 📑 Table of Contents
1. [Vectors & Equilibrium (Sum Invariants)](#1-vectors--equilibrium-sum-invariants)
2. [Manhattan Distance & Grid Geometry](#2-manhattan-distance--grid-geometry)
3. *(Upcoming: Parity & Invariance)*
4. *(Upcoming: Modular Arithmetic & Negative Modulo)*
5. *(Upcoming: Divisibility, Primes & GCD)*
6. *(Upcoming: Bitwise Arithmetic & XOR Magic)*

---

## 1. Vectors & Equilibrium (Sum Invariants)

- **Core Intuition**: When multiple independent forces or dimensions are given, an equilibrium (or total balance) occurs **if and only if** each dimension independently cancels out to zero. You never combine $X, Y, Z$ into a single scalar sum; you evaluate each axis separately.
- **The "Click" Example**: 
  - Think of a tug-of-war in 3D: If someone pulls you forward (+x) and someone pulls you up (+z), pulling backward (-x) balances the horizontal pull, but you will still fly upward unless someone pulls you down (-z). Balance along one axis does not compensate for imbalance on another.
- **Key Formula / Rule**:
  $$\sum_{i=1}^n x_i = 0 \quad \text{AND} \quad \sum_{i=1}^n y_i = 0 \quad \text{AND} \quad \sum_{i=1}^n z_i = 0$$
- **Common Traps**: Summing $(x_i + y_i + z_i)$ into a single total—$(-1, 1, 0)$ would give a sum of 0, but the particle is NOT in equilibrium!
- **Encountered In**: [Young Physicist (CF 69A)](file:///c:/Users/khati/Downloads/Codeforces/new_start/1youngphysicist.py)

---

## 2. Manhattan Distance & Grid Geometry

- **Core Intuition**: On a strict grid where you can only move **Up, Down, Left, Right** (no diagonal shortcuts like Euclidean $\sqrt{\Delta x^2 + \Delta y^2}$), the minimum number of steps between $(r_1, c_1)$ and $(r_2, c_2)$ is simply the horizontal steps plus the vertical steps.
- **The "Click" Example**: 
  - Walking in Manhattan/city blocks: You cannot walk through buildings diagonally. To go from 1st Ave & 2nd St to 4th Ave & 6th St, you walk 3 avenues east, then 4 streets north. Total moves = $|1 - 4| + |2 - 6| = 3 + 4 = 7$.
- **Key Formula**:
  $$\text{Distance} = |r_1 - r_2| + |c_1 - c_2|$$
- **Targeting Center of a $5 \times 5$ Grid** (1-indexed center is at $(3, 3)$):
  $$\text{Steps} = |r - 3| + |c - 3|$$
- **Encountered In**: Beautiful Matrix (CF 263A)

---
*(More topics will be added here systematically as we tackle problems together!)*
