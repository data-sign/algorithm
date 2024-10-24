-- 코드를 작성해주세요
-- 1. 대장균의 크기 내림차순 2. quentile 
SELECT ID, 
    CASE  
        WHEN PERCENT<= 0.25 THEN "CRITICAL" 
        WHEN PERCENT<= 0.5 THEN "HIGH"
        WHEN PERCENT<= 0.75 THEN "MEDIUM"
    ELSE "LOW" END AS COLONY_NAME
    FROM 
        (SELECT ID, SIZE_OF_COLONY, RANK() OVER(ORDER BY SIZE_OF_COLONY DESC)/TOTAL.CNT AS PERCENT
        FROM ECOLI_DATA A
        CROSS JOIN (SELECT COUNT(*) AS CNT FROM ECOLI_DATA) AS TOTAL) B
ORDER BY ID