### Plants grass across the whole board
def grass():
	
	for i in range (get_world_size()):
		for ii in range (get_world_size()):
			
			if can_harvest():
				harvest()
				
			elif get_ground_type() == Grounds.Soil:
				till()
				
			move(North)
			
		move(East)