-- script that lists all shows contained in the 
SELECT shows.title, tv_show_genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
ON genres.genre_id = shows.id
ORDER BY shows.title ASC, genres.genre_id ASC;
