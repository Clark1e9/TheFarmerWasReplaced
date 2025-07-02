#Purpose: Plants and harvests a whole board of carrots

# Known isses #
#- 

# To-do #
#- refactor check for blank tile in else block

def carrots():
	 
	for i in range (get_world_size()):
		for ii in range (get_world_size()):
			
			if can_harvest():
				harvest()

				if get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)

				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
			
			else:
				if get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)

				use_item(Items.Water)
				quick_print("I used water!")
				
			move(North)
			
		move(East)