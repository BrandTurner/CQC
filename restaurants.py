def read_restaurant(file):
	""" (file) -> (dict, dict, dict)

	Return a tuple of three dictionaries based on the information in the file:

	- a dict of {restaurant_name: rating%}
	- a dict of {price: list of restaurant names}
	- a dict of {cuisine: list of restaurant names}
	"""

	name_to_rating = {}
	price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
	cuisine_to_names = {}