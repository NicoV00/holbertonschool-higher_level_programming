-- Lists cities contained in database
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = state_id;