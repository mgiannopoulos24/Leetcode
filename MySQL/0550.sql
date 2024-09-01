WITH FirstLogin AS (
    -- Step 1: Find the first login date for each player
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
NextDayLogin AS (
    -- Step 2: Find the date immediately after the first login date where the player logged in again
    SELECT f.player_id
    FROM FirstLogin f
    JOIN Activity a
    ON f.player_id = a.player_id
    AND a.event_date = DATE_ADD(f.first_login_date, INTERVAL 1 DAY)
),
TotalPlayers AS (
    -- Step 3: Count total number of unique players
    SELECT COUNT(DISTINCT player_id) AS total_players
    FROM FirstLogin
),
PlayersWithNextDayLogin AS (
    -- Step 4: Count the number of players who logged in the day after their first login
    SELECT COUNT(DISTINCT player_id) AS players_with_next_day_login
    FROM NextDayLogin
)
-- Step 5: Calculate the fraction and round it to 2 decimal places
SELECT ROUND(p.players_with_next_day_login / t.total_players, 2) AS fraction
FROM TotalPlayers t, PlayersWithNextDayLogin p;
