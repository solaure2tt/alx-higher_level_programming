-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
--     Each record should display: <TV Show genre> - <Number of shows linked to this genre>
--     First column must be called genre
--     Second column must be called number_of_shows
--     Don’t display a genre that doesn’t have any shows linked
--     Results must be sorted in descending order by the number of shows linked
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT tg.name as genre, count(*) as number_of_shows
FROM tv_genres as tg INNER JOIN tv_show_genres as tvg
    ON tg.id = tvg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
