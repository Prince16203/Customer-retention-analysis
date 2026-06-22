SELECT 
    value_tier,
    COUNT(*) as total_customers,
    ROUND(AVG(previous_purchases), 1) as avg_previous_purchases,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(review_rating), 2) as avg_rating,
    ROUND(AVG(promo_dependency_score), 2) as avg_promo_dependency,
    ROUND(AVG(subscription_status) * 100, 1) as pct_subscribed
FROM customer
GROUP BY value_tier
ORDER BY FIELD(value_tier, 'High', 'Mid', 'Low');