SELECT 
    value_tier,
    payment_method,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY value_tier), 1) as pct
FROM customer
GROUP BY value_tier, payment_method
ORDER BY value_tier, count DESC;