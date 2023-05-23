import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')


def print_info(restaurants):
    print(restaurants[0])
    address = restaurants[3]
    address = address.split("+")
    for i in range(len(address)):
        print(' ' * 4, address[i])
        
    score = restaurants[6]
    avg = sum(score)/len(score)
    if avg >= 0 and avg <= 2:
        print('This restaurant is rated bad, based on {} reviews'.format(len(score)))
    elif avg > 2 and avg <= 3:
        print('This restaurant is rated average, based on {} reviews'.format(len(score)))
    elif avg > 3 and avg <= 4:
        print('This restaurant is rated above average, based on {} reviews'.format(len(score)))
    elif avg > 4 and avg <= 5:
        print('This restaurant is rated very good, based on {} reviews'.format(len(score)))
    print()
     

restaurants = lab05_util.read_yelp('yelp.txt')

id_input = int(input('Enter a number (1 to 155) => '))

if id_input <= 155 and id_input > 0:
    print_info(restaurants[id_input-1])
else:
    print("ERROR\nPlease enter a number between 1 to 155")