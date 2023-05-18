--  script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
--     Each record should display: tv_shows.title - tv_show_genres.genre_id
--     Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tvs.title, tvg.genre_id
FROM tv_shows as tvs LEFT JOIN tv_show_genres as tvg
     ON tvs.id = tvg.show_id
WHERE tvg.show_id IS NULL
ORDER BY tvs.title, tvg.genre_id;
