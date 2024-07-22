
from movement_functions import Movement
## direction is always a 3 element dictionary with xy, yz and xz angle in this respective order
## Y passes through eyes of drone, X is perpendicular to Y and lies on plane of drone, Z is height

class Find():
	def pollen_in_frame(): ## Finds pollen from still picture @Geethika and @Tavish
		return {"xy": 1, "yz":2, "xz":3}
	def stream_camera(): ## Robotics later
		return pollen_in_frame():

	def move_to_identified_flower(direction_of_flower):
		if direction_of_flower["xy"] <= config["threshold_of_feasible_detection_angle"]:
			Movement.rotate(direction_of_flower["xy"])
		else:
			print("Object is oriented on xy plane")
			if direction_of_flower["yz"] < config["line_of_attack_angle"] - config["line_of_attack_angle_error"]: ## drone is too low
				absolute_motion([0, 90, 0])
			elif direction_of_flower["yz"] > config["line_of_attack_angle"] + config["line_of_attack_angle_error"]:
				absolute_motion([0, 270, 0])
			elif direction_of_flower["yz"] > config["line_of_attack_angle"] - config["line_of_attack_angle_error"] and direction_of_flower["yz"] < config["line_of_attack_angle"] + config["line_of_attack_angle_error"]:
				print("Drone is on line of line of attack")
				move(direction_of_flower)
				print("WE'RE MOVING TOWARDS FLOWER")
				
