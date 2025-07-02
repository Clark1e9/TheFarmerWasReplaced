def carrots():
	
	for i in range (get_world_size()):
		for ii in range (get_world_size()):
			
			if can_harvest():
				harvest()
				
			if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
			elif get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)
			else:
				use_item(Items.Water)
				
			move(North)
			
		move(East)