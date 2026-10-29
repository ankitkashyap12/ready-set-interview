package arrays;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Ankit Kashyap on 27-08-2023
 */
public class TournamentWinner {

    public String tournamentWinnerBrute(
            ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results
    ) {
        // Write your code here.
        Map<String, Integer> scoreMap = new HashMap<>();
        String maxScoreTeam = null;
        int currentMaxScore = 0;
        for (int i = 0; i < results.size(); i++) {
            ArrayList<String> teams = competitions.get(i);
            String team1 = teams.get(0);
            String team2 = teams.get(1);
            int winner = results.get(i);
            int team1Score = 0;
            int team2Score = 0;
            if (winner == 0) //2nd team won
                team2Score = 3;
            if (winner == 1) //1st team won
                team1Score = 3;
            if (!scoreMap.containsKey(team1))
                scoreMap.put(team1, team1Score);
            else
                scoreMap.put(team1, scoreMap.get(team1) + team1Score);
            if (!scoreMap.containsKey(team2))
                scoreMap.put(team2, team2Score);
            else
                scoreMap.put(team2, scoreMap.get(team2) + team2Score);
            int totalScore1 = scoreMap.get(team1);
            int totalScore2 = scoreMap.get(team2);
            if (totalScore1 > totalScore2 && totalScore1 > currentMaxScore) {
                currentMaxScore = totalScore1;
                maxScoreTeam = team1;
            } else if (totalScore2 > totalScore1 && totalScore2 > currentMaxScore) {
                currentMaxScore = totalScore2;
                maxScoreTeam = team2;
            }
        }
        return maxScoreTeam;
    }

    public String tournamentWinnerBetter(
            ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results
    ) {
        // Write your code here.
        String currentBestTeam=null;
        int maxScore = 0;
        Map<String,Integer> scoreMap= new HashMap<>();
        for(int i=0;i<results.size();i++){
            int res = results.get(i);
            String winningTeam = competitions.get(i).get(res==0?1:0);
            int oldScoreOfWinner = scoreMap.containsKey(winningTeam)?scoreMap.get(winningTeam):0;
            int newScore=oldScoreOfWinner+3;
            if(newScore > maxScore){
                maxScore=newScore;
                currentBestTeam=winningTeam;
            }
            scoreMap.put(winningTeam,newScore);
        }
        return currentBestTeam;
    }
}
