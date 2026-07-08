# https://leetcode.com/problems/article-views-i/
# 08.07.2026


SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;
