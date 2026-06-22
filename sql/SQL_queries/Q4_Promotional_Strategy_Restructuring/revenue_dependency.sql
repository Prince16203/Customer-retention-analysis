SELECT 
    promo_dependency_score,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(SUM(purchase_amount_usd), 0) as total_revenue,
    ROUND(SUM(purchase_amount_usd) * 100.0 / 
        (SELECT SUM(purchase_amount_usd) FROM customer), 1) as pct_of_total_revenue
FROM customer
GROUP BY promo_dependency_score
ORDER BY promo_dependency_score;