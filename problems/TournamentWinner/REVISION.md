# Tournament Winner

- **Problem Number**: #046
- **Difficulty**: Easy
- **Topic**: Arrays & Hashing
- **Pattern**: Hash Map Score Tallying & Running Best
- **LeetCode Equivalent**: [LC 2284: Sender With Largest Word Count](https://leetcode.com/problems/sender-with-largest-word-count/)

## Active recall
In a round-robin tournament where 1 indicates home team win and 0 away team win (3 points per win), how do you determine the tournament winner?

## Core idea
Maintain a hash table of scores and track currentBestTeam initialized to empty string. For each match i with [homeTeam, awayTeam] and result results[i]: winningTeam = (results[i] == 1) ? homeTeam : awayTeam. scores[winningTeam] += 3. If scores[winningTeam] > scores[currentBestTeam], update currentBestTeam = winningTeam. Return currentBestTeam.

## Hints
- **Hint 1**: Translate each match result into the name of the winning team.
- **Hint 2**: Update scores in a hash map and maintain the leader on the fly to avoid a second pass.

## Pattern
**Pattern**: Hash Map Score Tallying & Running Best
Use when: Arrays & Hashing problems require efficient traversal or optimal sub-structure.

## Trick
Tracking currentBestTeam on the fly avoids scanning the entire scores map at the end.

## Complexity
Time: O(N) where N is number of competitions. Space: O(K) where K is number of unique teams.

## Edge cases
- Single competition.
- Ensure points are awarded to awayTeam when result == 0.
