WITH UnbannedTrips AS (
    SELECT
        t.request_at,
        t.status
    FROM Trips t
    JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
    JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
),
DailyTotals AS (
    SELECT
        request_at AS Day,
        COUNT(*) AS total_requests,
        SUM(CASE WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END) AS cancelled_requests
    FROM UnbannedTrips
    GROUP BY request_at
)
SELECT
    Day,
    ROUND(cancelled_requests / total_requests, 2) AS `Cancellation Rate`
FROM DailyTotals;
