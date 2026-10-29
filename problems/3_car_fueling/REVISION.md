# Car Fueling

- **Problem Number**: #084
- **Difficulty**: Medium
- **Topic**: Greedy
- **Pattern**: Farthest Reachable Station (Greedy Leapfrog)
- **LeetCode Equivalent**: [LC 134: Gas Station](https://leetcode.com/problems/gas-station/)

## Active recall
To travel distance d with tank capacity m, what is the minimum number of refueling stops needed?

## Core idea
Add start (0) and destination (d) to stops array. Maintain currentStop = 0 and refills = 0. While currentStop < numStops: lastStop = currentStop. While currentStop < numStops and stops[currentStop + 1] - stops[lastStop] <= m: advance currentStop. If currentStop == lastStop: the next stop is unreachable (gap > m), return -1. If currentStop < destination: refills++.

## Hints
- **Hint 1**: Always drive as far as possible on the current tank before refueling.
- **Hint 2**: Refuel at the farthest reachable gas station.

## Pattern
**Pattern**: Farthest Reachable Station (Greedy Leapfrog)
Use when: Greedy problems require efficient traversal or optimal sub-structure.

## Trick
If you cannot advance at least one station forward from your last refueling stop, the destination is unreachable -> return -1.

## Complexity
Time: O(N) where N is number of gas stations. Space: O(1) auxiliary space.

## Edge cases
- Destination reachable without stops: returns 0.
- Gap between any two adjacent stations > m: returns -1.
- Refueling at the final stop is unnecessary.
