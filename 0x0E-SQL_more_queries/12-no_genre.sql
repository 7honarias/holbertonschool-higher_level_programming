-- script that lists all shows contained
SELECT shows.title, genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
      ON genres.show_id = shows.id
WHERE genres.genre_id IS NULL
ORDER BY shows.title ASC;
