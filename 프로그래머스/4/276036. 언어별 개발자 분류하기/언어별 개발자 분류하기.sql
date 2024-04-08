-- 코드를 작성해주세요
WITH TMP AS (
    SELECT CASE WHEN ID IN ( SELECT DISTINCT(ID) 
                             FROM DEVELOPERS D, SKILLCODES S 
                             WHERE (D.SKILL_CODE & S.CODE) > 0
                                AND SKILL_CODE & (SELECT S.CODE FROM SKILLCODES S WHERE NAME = 'Python') > 0
                                AND S.CATEGORY = 'Front End'
                             GROUP BY ID
                           ) THEN 'A'
                WHEN ID IN ( SELECT DISTINCT(ID)
                             FROM DEVELOPERS D, SKILLCODES S 
                             WHERE (D.SKILL_CODE & S.CODE) > 0
                                AND S.NAME = 'C#'
                             GROUP BY ID
                           ) THEN 'B'
                WHEN ID IN ( SELECT DISTINCT(ID)
                             FROM DEVELOPERS D, SKILLCODES S 
                             WHERE (D.SKILL_CODE & S.CODE) > 0
                                AND S.CATEGORY = 'Front End'
                             GROUP BY ID
                           ) THEN 'C'
            END GRADE
        ,ID
        ,EMAIL
    FROM DEVELOPERS D
    GROUP BY ID, EMAIL
)
SELECT *
FROM TMP
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;