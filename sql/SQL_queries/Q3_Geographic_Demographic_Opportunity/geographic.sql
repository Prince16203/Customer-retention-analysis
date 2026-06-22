SELECT 
    location,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(promo_dependency_score), 2) as avg_promo_dependency,
    ROUND(AVG(previous_purchases), 1) as avg_previous_purchases,
    ROUND(SUM(purchase_amount_usd), 0) as total_revenue
FROM customer
GROUP BY location
ORDER BY avg_spend DESC, avg_promo_dependency ASC
LIMIT 15;