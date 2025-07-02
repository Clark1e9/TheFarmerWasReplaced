#Purpose: Control logic for the game

# Known isses #
#- *very manual*

# To-do #
#- Create automatic item level adjustment
#- Automatically work towards unlocks

from grass import grass
from tree import trees
from carrot import carrots
#from Pumpkins import pumpkins_basic
from Pumpkins import pumpkins_adv


from movement import move_to_start

move_to_start()

while True:
	#grass()
	#trees()
	#carrots()
	#pumpkins_basic()
	pumpkins_adv()