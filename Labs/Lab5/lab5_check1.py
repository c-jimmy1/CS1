import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')


def print_info(restaurants):
    print(restaurants[0])
    address = restaurants[3]
    address = address.split("+")
    for i in range(len(address)):
        print(' ' * 4, address[i])
        
    score = restaurants[6]
    print("Average score: {:.2f}".format(sum(score)/len(score)))
    print()
     
restaurants = lab05_util.read_yelp('yelp.txt')


print_info(restaurants[0])
print_info(restaurants[4])
print_info(restaurants[42])
    