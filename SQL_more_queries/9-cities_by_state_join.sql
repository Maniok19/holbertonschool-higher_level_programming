-- Wabwabalooda do wapwapwapwa johnny tu nous manques
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;