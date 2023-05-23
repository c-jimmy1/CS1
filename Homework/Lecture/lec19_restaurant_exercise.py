'''
Demonstration example to build a list of Restaurant objects from the
Yelp data we worked with in Lecture 19.
'''

from Restaurant import Restaurant

def convert_input_to_restaurant(line):
    '''
    Parse the Yelp input data to create a Restaurant object.
    '''
    m = line.strip().split("|")
    name = m[0]
    latitude = float(m[1])
    longitude = float(m[2])
    address = m[3].split('+')   # creates a list of the address lines
    url = m[4]
    restaurant_type = m[5]
    reviews = []
    for r in m[6:]:
        reviews.append(int(r))
    return Restaurant(name, latitude, longitude, address, url, \
                          restaurant_type, reviews )

def build_restaurant_list( file_name ):
    '''
    Assuming the Yelp data is in the form of one line per restaurant,
    read each line, create a restaurant object from each, and form a
    list of these objects.  Return the list.
    '''
    restaurants = []
    for line in open(file_name):
        restaurants.append(convert_input_to_restaurant(line))
    return restaurants
    
if __name__ == "__main__":
    file_name = 'yelp.txt'
    restaurants = build_restaurant_list( file_name )
    num_restaurants = len(restaurants)

    lists = []
    for restaurant in restaurants:
        if restaurant.average_review() > 3 and restaurant.address[1].startswith('Troy') and (restaurant.category == 'American (New)' or restaurant.category == 'American (Traditional)'):
            lists.append(restaurant.name)
    
    lists = sorted(lists)
    for restaurant in lists:
        print(restaurant)