-- script that lists all shows and all genres
SELECT shows.title AS title, genres.name AS name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
     ON show_genres.show_id = shows.id
LEFT JOIN tv_genres AS genres
     ON show_genres.genre_id = genres.id
ORDER BY title ASC, name ASC;
