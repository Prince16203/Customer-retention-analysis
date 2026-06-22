SELECT 
    category,
    season,
    COUNT(*) as count,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend
FROM customer
WHERE value_tier = 'High'
    AND promo_dependency_score = 0
    AND satisfaction_flag = 1
GROUP BY category, season
ORDER BY count DESC;