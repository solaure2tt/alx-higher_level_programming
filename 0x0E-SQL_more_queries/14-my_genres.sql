-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
--     The tv_shows table contains only one record where title = Dexter (but the id can be different)
--     Each record should display: tv_genres.name
--     Results must be sorted in ascending order by the genre name
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tg.name
FROM tv_genres as tg
INNER JOIN tv_show_genres as tvg
     ON tg.id = tvg.genre_id
INNER JOIN tv_shows as tvs
     ON tvs.id = tvg.show_id
WHERE tvs.title = 'Dexter'
ORDER BY tg.name;
