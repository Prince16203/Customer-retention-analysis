SELECT 
    gender,
    value_tier,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(promo_dependency_score), 2) as avg_promo_dependency
FROM customer
GROUP BY gender, value_tier
ORDER BY gender, FIELD(value_tier, 'High', 'Mid', 'Low');
ORDER BY gender, FIELD(value_tier, 'High', 'Mid', 'Low');