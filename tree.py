### Plants trees and a bit of grass
def trees():
	
	#Loop across board
	for i in range (get_world_size()):
		for ii in range (get_world_size()):
			
			#if tree or grass is harvestable
			if can_harvest():
				harvest()
				
				if (get_pos_x() % 2 == 0): #if x is odd...
					if (get_pos_y() % 2 == 0): #and y is odd, plant a tree
						plant(Entities.Tree)
						
				else: #if x is even...
					if (get_pos_y() % 2 != 0): #and y is even, plant tree
						plant(Entities.Tree)
							
				move(North) #Move north after harvest and planting
				
			elif get_ground_type() == Grounds.Soil: #if soil needs to be converted so grass can grow
				till()
				move(North)
			else:
				use_item(Items.Water)
				move(North) #Move north if no harvest occurs
				
		move(East) #Move east at top of board