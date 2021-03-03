-- script that uses the htbtn_0d_tvshows
SELECT genres.name AS name
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres
      ON show_genres.genre_id = genres.id
INNER JOIN tv_shows AS shows
      ON show_genres.show_id = shows.id
WHERE shows.title = "Dexter"
ORDER BY name ASC;
