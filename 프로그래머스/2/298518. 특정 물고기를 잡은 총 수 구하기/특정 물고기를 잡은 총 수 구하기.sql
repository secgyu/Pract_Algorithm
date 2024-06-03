SELECT (SELECT COUNT(*)
        FROM fish_info
        WHERE fish_type IN (SELECT fish_type
                            FROM fish_name_info
                            WHERE fish_name = 'SNAPPER')
       ) +
       (SELECT COUNT(*)
        FROM fish_info
        WHERE fish_type IN (SELECT fish_type
                            FROM fish_name_info
                            WHERE fish_name = 'BASS')
       ) AS FISH_COUNT;
