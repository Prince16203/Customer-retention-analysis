SELECT 
    value_tier,
    promo_dependency_score,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(previous_purchases), 1) as avg_previous_purchases
FROM customer
GROUP BY value_tier, promo_dependency_score
ORDER BY FIELD(value_tier, 'High', 'Mid', 'Low'), promo_dependency_score;