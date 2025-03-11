select movies.id, movies.name
from movies
INNER JOIN
prices
on movies.id_prices = prices.id
where value < 2