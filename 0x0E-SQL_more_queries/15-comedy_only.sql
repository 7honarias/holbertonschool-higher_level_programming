-- script that lists all comedy shows
SELECT shows.title AS title
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres
      ON show_genres.genre_id = genres.id
INNER JOIN tv_shows AS shows
      ON show_genres.show_id = shows.id
WHERE genres.name = "Comedy"
ORDER BY title ASC;
