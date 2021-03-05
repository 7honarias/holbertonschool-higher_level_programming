-- script that lists all shows without the genre
-- Comedy in the database
SELECT DISTINCT s.title AS title
FROM tv_shows AS s
WHERE s.title NOT IN
      (SELECT s.title AS title
       FROM tv_genres AS g
       INNER JOIN tv_show_genres AS sg
       ON sg.genre_id = g.id
       INNER JOIN tv_shows AS s
       ON sg.show_id = s.id
       WHERE g.name = "Comedy")
ORDER BY title ASC;
