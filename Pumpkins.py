from movement import board_area

### Plant pumpkins
def pumpkins_basic():
	
	for i in range(get_world_size()):
		for ii in range(get_world_size()):
			
			if can_harvest():
				harvest()
				
			if get_ground_type() == Grounds.Grassland:
				till()
				plant(Entities.Pumpkin)
				
			elif get_ground_type() == Grounds.Soil:
				plant(Entities.Pumpkin)
					
			move(North)
				
		move(East)
			
### Plants one large pumkin
def pumpkins_adv():
	
	memory = 0
	
	for i in range(get_world_size()):
		for ii in range(get_world_size()):
			
			#if pumpkin is already there:
			if get_entity_type() == Entities.Pumpkin:
				memory = memory + 1
				quick_print(memory)
				
				#if memory = x * y, harvest big pumpkin
				if memory == board_area():
					harvest()
					memory = 0
				
			#if ground is soil without pumkin:
			elif get_ground_type() == Grounds.Soil:
				harvest()
				plant(Entities.Pumpkin)
				
			#if ground isn't soild (and therefore no pumpkin)
			elif get_ground_type() == Grounds.Grassland:
				till()
				plant(Entities.Pumpkin)
				
			
			move(North)
		move(East)
	