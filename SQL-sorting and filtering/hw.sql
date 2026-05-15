-- This query summarizes sales performance by category
SELECT 
    category,
    COUNT(order_id) AS total_orders,        -- Count number of records
    AVG(price) AS average_item_price,      -- Calculate average
    SUM(price * quantity) AS total_revenue  -- Calculate total sum
FROM 
    sales_data
WHERE 
    status = 'Completed'                   -- 1. Filter raw rows BEFORE grouping
GROUP BY 
    category                               -- 2. Group data into buckets
HAVING 
    SUM(price * quantity) > 500            -- 3. Filter groups AFTER aggregation
ORDER BY 
    total_revenue DESC;                    -- 4. Sort the final result set
