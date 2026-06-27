-- Identify top 10 liquid tickers based on average trading volume (2017-2025)
SELECT 
    SYMBOL,
    COUNT(DATE) AS total_trading_days,
    ROUND(AVG(VOLUME), 0) AS avg_daily_volume,
    ROUND(MAX(HIGH) - MIN(LOW), 2) AS absolute_9yr_spread
FROM 
    psx_historical_market
GROUP BY 
    SYMBOL
HAVING 
    total_trading_days > 100 -- Filters out short-term or delisted symbols
ORDER BY 
    avg_daily_volume DESC
LIMIT 10;
