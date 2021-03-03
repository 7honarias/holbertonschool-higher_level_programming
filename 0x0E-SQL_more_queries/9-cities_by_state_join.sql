-- script that lists all cities contained
SELECT cities.id, cities.name, states.name 
FROM cities INNER JOIN states ON cities.state_id=states.id;
