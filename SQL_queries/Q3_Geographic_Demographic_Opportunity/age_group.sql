SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END as age_group,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(promo_dependency_score), 2) as avg_promo_dependency,
    ROUND(AVG(previous_purchases), 1) as avg_previous_purchases
FROM customer
GROUP BY age_group
ORDER BY avg_spend DESC;