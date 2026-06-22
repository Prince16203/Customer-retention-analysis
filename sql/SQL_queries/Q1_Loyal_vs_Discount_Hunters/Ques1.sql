SELECT 
    CASE 
        WHEN previous_purchases >= 25 AND promo_dependency_score = 0 THEN 'Genuinely Loyal'
        WHEN previous_purchases >= 25 AND promo_dependency_score = 2 THEN 'Promo Loyal'
        WHEN previous_purchases < 25 AND promo_dependency_score = 2 THEN 'Discount Hunter'
        ELSE 'New/Inactive'
    END AS customer_segment,
    COUNT(*) as total_customers,
    ROUND(AVG(purchase_amount_usd), 2) as avg_spend,
    ROUND(AVG(review_rating), 2) as avg_rating
FROM customer
GROUP BY customer_segment;