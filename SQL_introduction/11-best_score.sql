-- Script that lists all records a score >= 10  of the table second_table of the database hbtn_0c_0.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;