# https://leetcode.com/problems/invalid-tweets
# 09.07.2026


SELECT tweet_id FROM Tweets
WHERE CHAR_LENGTH(content) > 15
