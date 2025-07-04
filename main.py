#Purpose: Control logic for the game

# Known isses #
#- *very manual*

# To-do #
#- Create automatic item level adjustment
#- Automatically work towards unlocks

from grass import grass
from tree import trees
from carrot import carrots
from Pumpkins import pumpkins_adv


from movement import move_to_start
from inputs import input_quantity

move_to_start()

while True:
	#grass()
	#trees()
	#carrots()
	#pumpkins_basic()
	pumpkins_adv()


def brain(target_num):
	return null

#Collect array of current item counts at time of call
def get_current_num():

	#Initialise array
	current = []

	#Add each item to new array index
	current[0] = num_items(Items.Hay)
	current[1] = num_items(Items.Wood)
	current[2] = num_items(Items.Carrot)
	current[3] = num_items(Items.Pumpkin)
	#current[4] = num_items() #Future expansion
	
	#Return array
	return current