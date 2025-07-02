while True:
	for i in range (get_world_size()):
		for ii in range (get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
			elif get_ground_type() == Grounds.Soil:
				till()
				move(North)
			else:
				move(North)
		move(East)