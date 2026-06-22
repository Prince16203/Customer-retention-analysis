SELECT 
    ROUND(AVG(age), 1) as avg_age,
    gender,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(previous_purchases), 1) as avg_previous_purchases,
    ROUND(AVG(review_rating), 2) as avg_rating,
    COUNT(*) as total_customers
FROM customer
WHERE value_tier = 'High'
    AND promo_dependency_score = 0
    AND satisfaction_flag = 1
GROUP BY gender
ORDER BY total_customers DESC;