WITH buys AS (
    SELECT 
        stock_name, 
        operation_day, 
        price,
        ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS buy_seq
    FROM 
        Stocks
    WHERE 
        operation = 'Buy'
),
sells AS (
    SELECT 
        stock_name, 
        operation_day, 
        price,
        ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS sell_seq
    FROM 
        Stocks
    WHERE 
        operation = 'Sell'
)
SELECT 
    b.stock_name,
    SUM(s.price - b.price) AS capital_gain_loss
FROM
    buys b
JOIN
    sells s
    ON b.stock_name = s.stock_name 
    AND b.buy_seq = s.sell_seq
GROUP BY
    b.stock_name;
