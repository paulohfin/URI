select products.name, providers.name 
from providers 

INNER JOIN products 

on products.id_providers = providers.id 
WHERE providers.name = 'Ajax SA';