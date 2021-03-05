-- script that lists all shows without the genre
-- Comedy in the database
SELECT shows.title AS title
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres
      ON show_genres.genre_id = genres.id
INNER JOIN tv_shows AS shows
      ON show_genres.show_id = shows.id
WHERE genres.name != "Comedy"
GROUP BY title
ORDER BY title ASC;
