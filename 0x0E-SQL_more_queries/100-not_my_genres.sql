-- script that uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show Dexter
SELECT genres.name AS name
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres
      ON show_genres.genre_id = genres.id
WHERE show_genres.genre_id NOT IN
      (SELECT show_genres.id FROM tv_show_genres AS show_genres
       INNER JOIN tv_shows AS shows
       ON show_genres.show_id = shows.id
       WHERE shows.title != "Dexter")
ORDER BY name ASC;
