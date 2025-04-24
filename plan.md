# Divided into portions:

1. create a git hub repo for the project
2. find a way to map the mrt map in code

## For Enum method, you can initalise a enum by using:

import Enum
class Season(Enum):
    Pasir_ris = EW1
    Tampines = EW2
    .....
    

## for enums, useful functions include:

Use enums if theres a fixed set of options (eg: on/off)



eg:

class Color(Enum): # init your enums

 	red: str = 'R'

​	green: str = 'G'



! To obtain R/G, print(Color.red.value)

def create_car(color: Color) -> None: 

​	match color: # does a check

​		case Color.red:

​			print("a red car is created")

​		case Color.green:

​			print("a green car is created")



yellow_and_red: Color = Color.yellow | Color.red # stores both colors

Dakota: Color = Color.yellow



if Dakota in yellow_and_red:

​	print("Dakota is either of CCL or NSL")

else:

​	print("the station is not in both CCL and NSL")






- enum (diff py file), linked list, graph



Attempt at using enum to create the library:

​	1. add all stations as enums into the programme

this can be carried out by labelling the stations by its lines and its station number

! come out a better value to give to the stations if possible

eg:

class Station(stations):

​	pasir_ris: station = station.EW1

​	tampines: station = station.EW1 | station.DT32

​	paya_lebar: station = station.EW8 | station.CC9

​	







3. save the timings between each mrt station
- doable with step 2
4. accept user inputs 
- rest api, postman for testing
5. attempt to find the fastest way from inputted station to said station
- topological sort, dijkstra algorithm
6. if possible make it into a telegram bot
- research online 