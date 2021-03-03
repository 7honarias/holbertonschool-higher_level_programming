-- script that lists all shows contained
SELECT shows.title, show_genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
     ON show_genres.genre_id = shows.id
WHERE show_genres.genre_id IS NULL
ORDER BY shows.title ASC;
