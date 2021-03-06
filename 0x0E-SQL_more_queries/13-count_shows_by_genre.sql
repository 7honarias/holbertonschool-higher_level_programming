-- script that lists all shows contined in hbtn_0d_tvshows
SELECT genres.name AS genre, COUNT(genres.id) AS number_of_shows
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres
      ON show_genres.genre_id = genres.id
INNER JOIN tv_shows AS shows
      ON show_genres.genre_id = shows.id
GROUP BY genres.name
ORDER BY number_of_shows DESC; 
