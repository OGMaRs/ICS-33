import datetime 

"""class Bedroom: # how to make a class
    "Represents each bedroom"
    def __init__(self, number):
        self.number = number
        
    def getNumber(self):
        return self.number"""
    #Remove and change first few commands to store in reservations
    

class Reservation:
    def __init__(self, room_number, arrival_date, departure_date, name, reservation_number):
        self.room_number = room_number
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.name = name
        self.reservation_number = reservation_number

def open_text(file:str):
    infile = open(file)
    file = infile.read()
    file = file.split('\n')
    infile.close()
    return file


def print_bedrooms(bedrooms:list):
        print ('Number of bedrooms in service: ', len(bedrooms))
        print ('------------------------------------')
        for bedroom in bedrooms:
            print (bedroom.getNumber())

def add_bedroom(bedrooms:list, number:int):
    #fix this
        newBedroom = Bedroom(number)
        bedrooms.append(newBedroom)

def remove_bedroom(bedrooms:list, number:int):
    #this too
        for bedroom in bedrooms:
            if bedroom.getNumber() == number:
                bedrooms.remove(bedroom)
                return
        message = ("Sorry, can't delete room " + str(number) + "; it is not in service now")           
        print (message)

#def add_reservation(reservations:list, number:int):

def reserve_list(number):
    print('Number of reservations: {}'.format((number)))
    print('No. Rm. Arrive      Depart     Guest')
    print('--------------------------------------')
    for x in number:
        print(' {0:3} {1:3} {2:10} {3:10} {4:20}'.format(x, number, Reservation[x].arrival_date, Reservation[x].departure_date, Reservation[x].name))

    
"""def STAGE_INPUT(file):
    bedrooms_list = []

    infile = open(file)
    file = infile.read()
    file = file.split('\n')
    infile.close()
    
    #STAGE_INPUT = open_text('BandB.txt')
    
    for line in file: # splitting a strng into a list
        strippedLine = line.lstrip()
        command = strippedLine[0:2].lower()
        newInput = strippedLine[2:].lstrip()
    
        if command == 'pl':
            print (newInput)
        elif command == 'bl':
            print_bedrooms(bedrooms_list)
        elif command == 'ab':
            add_bedroom(bedrooms_list, int(newInput))
        elif command == 'bd':
            remove_bedroom(bedrooms_list, int(newInput))


STAGE_INPUT('BandB.txt')
print (' ')
print (' ')
STAGE_INPUT('BandB2.txt')"""




bedrooms_list = []
reservations_list = []
reservation_number = 0

STAGE_2 = open_text('BandB3.txt')

for line in STAGE_2:
    strippedLine = line.lstrip()
    command = strippedLine[0:2].lower()
    newInput = strippedLine[2:].lstrip()
    
    if command == 'pl':
        print (newInput)
    elif command == 'bl':
        print_bedrooms(bedrooms_list)
    elif command == 'ab':
        add_bedroom(bedrooms_list, int(newInput))
    elif command == 'bd':
        remove_bedroom(bedrooms_list, int(newInput))
    elif command == 'nr':
        reservation_parts = newInput.split(' ')
        reservation_parts = [x for x in reservation_parts if x]
        room_number = int(reservation_parts[0])
        arrival_date = reservation_parts[1]
        departure_date = reservation_parts[2]
        name = (' ').join(reservation_parts[3:]) # join name back together bc you dont want a list since you split it earlier
        reservation_number = reservation_number + 1

        new_reservation = Reservation(room_number, arrival_date, departure_date, name, reservation_number)
        reservations_list.append(new_reservation)

        confirmation_message = ('Reserving room ' + str(room_number) + ' for ' + name + ' -- Confirmation #' + str(reservation_number))
        confirmation_message2 = ('    ' + '(arriving ' + arrival_date + ', departing ' + departure_date + ')')

    elif command == 'rl':
        reserve_list(reservation_number)
        
        print (confirmation_message)
        print (confirmation_message2)            
    
        
                                 
        
