'''
This first function uses the valutes given by the user to determine how to pokemon should move
If the pokemon moves north, the rows decrease as the top of the frame is 0
To prevent pokemon going out of frame the nested if statement is used
'''
def move_pokemon(row, column, directions, steps):
    directions = directions.upper()
    if directions == 'N':
        row = row - steps
        if row < 0:
            row = 0
            
    elif directions == 'S':
        row = row + steps
        if row > 150:
            row = 150
            
    elif directions == 'W':
        column = column - steps
        if column < 0:
            column = 0
            
    elif directions == 'E':
        column = column + steps
        if column > 150:
            column = 150
            
    coordinates = (row, column)
    return coordinates

'''
This second function calculates the fight encounters
It first determines that water types are an instant win, and move it 1 direction
The it determines the moves for ground types. Since ground types lose and make you move 10 steps/
I use if else statements to determine the direction it has to move 10 in
The last else statement accomodates for errors, so if neither W or G is entered, then no pokemon is printed
'''
def fight(name, ptype, directions, coordinates, fightrecord):
    ptype = ptype.upper()
    if ptype == 'W':
        fightrecord.append("Win")
        coordinates = move_pokemon(coordinates[0], coordinates[1], directions, 1)
        print("{} wins and moves to {}".format(name, coordinates))
    
    elif ptype == 'G':
        fightrecord.append('Lose')
        
        if directions == 'N':
            coordinates = move_pokemon(coordinates[0], coordinates[1], "S", 10)
            print("{} runs away to {}".format(name, coordinates))
        
        elif directions == 'S':
            coordinates = move_pokemon(coordinates[0], coordinates[1], "N", 10)
            print("{} runs away to {}".format(name, coordinates))
        
        elif directions == 'W':
            coordinates = move_pokemon(coordinates[0], coordinates[1], "E", 10)
            print("{} runs away to {}".format(name, coordinates))

        elif directions == 'E':
            coordinates = move_pokemon(coordinates[0], coordinates[1], "W", 10)
            print("{} runs away to {}".format(name, coordinates))
       
        else: 
            coordinates = move_pokemon(coordinates[0], coordinates[1], directions, 10)
            print("{} runs away to {}".format(name, coordinates))
    else:
        fightrecord.append("No Pokemon")
    
    return coordinates
    

turns = int(input('How many turns? => '))
print(turns)
name = input('What is the name of your pikachu? => ')
name = name.strip()
print(name)

freq = int(input('How often do we see a Pokemon (turns)? => '))
print(freq)

position = (75, 75) #The initial position the pokemon starts at
fightrecord = []

print()
print("Starting simulation, turn 0 {} at (75, 75)".format(name))

"""
The while loop keeps the game running until the amount of turns is reached
In the loop the program prompts the user for directions, and the type of pokemon
"""

i = 0
while i < turns:
    
    i += 1
    directions = input("What direction does {} walk? => ".format(name))
    directions = directions.strip()
    print(directions)
    
    directions = directions.upper()
    position = move_pokemon(position[0], position[1], directions, 5)
    

    if i % freq == 0: #if i is divisble by the frequency it means that pika faces an opponent that round and the round is a multiple of the frequency
        if i != 0:
            temp = str(i)
            print("Turn {}, {} at {}".format(temp, name, position))
            ptype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
            ptype = ptype.strip()
            print(ptype)

#uses the fight function to determine the new position of the pokemon
            position = fight(name, ptype, directions, position, fightrecord)

print ('{} ends up at {}, Record: {}'.format(name, position, fightrecord))