-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
--    If a show doesn’t have a genre, display NULL in the genre column
--    Each record should display: tv_shows.title - tv_genres.name
--    Results must be sorted in ascending order by the show title and genre name
--    You can use only one SELECT statement
--    The database name will be passed as an argument of the mysql command
SELECT tvs.title, tg.name
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvg
    ON tvs.id = tvg.show_id
LEFT JOIN tv_genres AS tg
    ON tg.id = tvg.genre_id
ORDER BY tvs.title, tg.name;
