SELECT user_id
FROM   (SELECT user_id,
               signup_date,
               action_date
        FROM   emails AS em
               inner join texts AS txt
                       ON txt.email_id = txt.email_id
        WHERE  txt.signup_action = 'Confirmed') AS tiktok
WHERE  signup_date + interval '1' day = action_date; 