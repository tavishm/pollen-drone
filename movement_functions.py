import math
import random
from pollen_config import config
import time



class Motor:
    def yaw(xy_angle)
    def motor_fl(thrust): 
        time.sleep(config["time_of_single_motion"])
        return None
    def motor_fr(thrust): 
        time.sleep(config["time_of_single_motion"])
        return None
    def motor_bl(thrust): 
        time.sleep(config["time_of_single_motion"])
        return None
    def motor_br(thrust): 
        time.sleep(config["time_of_single_motion"])
        return None


class Movement:
    def _init_(self, x=0, y=0, direction=0):
        #self.position = (x, y)
        self.direction = []  # Direction in degrees, 0 means facing east, is a list with 3 elements for x-y, y-z and x-z plane
        self.is_moving = False
    
    def move(self, direction): ## CAUSES MOTION FOR delta T time
        self.is_moving = True

        print("Robotic pollinator started moving.")

    
    def rotate(self, xy_angle):
        Motor.yaw(xy_angle)
        print("Rotating by ", xy_angle)

    def stop(self):
        self.is_moving = False
        print("Robotic pollinator stopped moving.")
    
    def absolute_motion(self, direction): ## moves 1 unit in direction
        print("moving in ", direction)

        ## MOTION ALONG Z AXIS
        xy_z_theta = math.acos()

    def search_for_flower(self, search_area):
        if self.is_moving:
            flower_x = random.uniform(search_area[0], search_area[2])
            flower_y = random.uniform(search_area[1], search_area[3])
            self.flower_position = (flower_x, flower_y)
            print(f"Flower detected at position {self.flower_position}")
            self.move_towards_flower()
        else:
            print("The robotic pollinator is not moving. Start it first.")
    
    def move_towards_flower(self):
        if self.is_moving and hasattr(self, 'flower_position'):
            fx, fy = self.flower_position
            x, y = self.position
            dx = fx - x
            dy = fy - y
            distance = math.sqrt(dx*2 + dy*2)
            if distance > 0:
                self.direction = math.degrees(math.atan2(dy, dx))
                self.move(distance)
                print(f"Moved towards the flower at {self.flower_position}")
            else:
                print("Already at the flower position.")
        else:
            print("Either the robot is not moving or the flower position is not set.")


   def pt_len(point, plane='all'):
        if plane=='all':
            return math.sqrt(point["x"]^2 + point["y"]^2 + point["z"]^2)

        if plane=='xy':
            return math.sqrt(point["x"]^2 + point["y"]^2)

        if plane=='yz':
            return math.sqrt(point["y"]^2 + point["z"]^2)

        if plane=='xz':
            return math.sqrt(point["x"]^2 + point["z"]^2)


    def get_coordinates_of_direction(direction):
        ## rotation about xy plane
        point = {"y": 1, "x":0, "z":0}

        point["y"] = pt_len(point plane='xy')*math.cos(direction["xy"])
        point["x"] = pt_len(point, plane='xy')*math.sin(direction["xy"])

        ## rotation about yz plane
        point["y"] = pt_len(point, plane='yz')*math.cos(direction["yz"])
        point["z"] = pt_len(point, plane='yz')*math.sin(direction["yz"])

        ## rotation about xz plane
        point["x"] = pt_len(point, plane='xz')*math.sin(direction["xz"])
        point["z"] = pt_len(point, plane='xz')*math.cos(direction["xz"])

