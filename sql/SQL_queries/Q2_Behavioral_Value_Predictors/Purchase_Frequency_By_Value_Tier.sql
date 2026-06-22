SELECT 
    value_tier,
    frequency_of_purchases,
    COUNT(*) as count,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend
FROM customer
GROUP BY value_tier, frequency_of_purchases
ORDER BY value_tier, count DESC;