SELECT
    Score,
    (
        SELECT COUNT(*)
        FROM (
            SELECT DISTINCT Score AS s
            FROM Scores
        ) AS tmp
        WHERE s >= Scores.Score
    ) AS `Rank`
FROM Scores
ORDER BY Score DESC;