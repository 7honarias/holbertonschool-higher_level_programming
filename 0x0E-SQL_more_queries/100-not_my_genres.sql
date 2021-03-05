-- script that uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show Dexter
SELECT DISTINCT g.name AS name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
      ON sg.genre_id = g.id
WHERE sg.genre_id NOT IN
      (SELECT sg.genre_id
       FROM tv_show_genres AS sg
       INNER JOIN tv_shows AS s
       ON sg.show_id = s.id
       WHERE s.title = "DEXTER")
ORDER BY name ASC;
