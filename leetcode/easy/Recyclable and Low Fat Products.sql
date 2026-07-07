# https://leetcode.com/problems/recyclable-and-low-fat-products/
# 07.07.2026


SELECT product_id
FROM Products
WHERE low_fats = "Y" AND recyclable = "Y";
