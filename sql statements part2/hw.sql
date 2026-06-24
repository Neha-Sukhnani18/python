SELECT 
    team_name,
    COUNT(player_id) AS total_players_drafted,
    COUNT(DISTINCT college) AS unique_colleges_represented,
    AVG(pick_number) AS average_draft_pick,
    MIN(pick_number) AS highest_pick_number,
    MAX(pick_number) AS lowest_pick_number
FROM 
    Draft
GROUP BY 
    team_name
ORDER BY 
    total_players_drafted DESC, 
    average_draft_pick ASC;
