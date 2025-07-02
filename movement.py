### Moves drone to 0,0
def move_to_start():
	while True:
		if get_pos_x() != 0:
			move (West)
			
		if get_pos_y() != 0:
			move(South)
			
		if get_pos_x() == 0 and get_pos_y() == 0:
			break
			
def board_area():
	size = get_world_size() ** 2
	return size
		