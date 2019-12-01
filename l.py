from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor= LineSensor(27)

left_sensor.when_line = function_name_to_call
left_sensor.when_no_line = other_function_name_to_call


#from gpiozero import Robot, LineSensor
#from time import sleep

#robot = Robot(left=(7, 8), right=(9, 10))
#left_sensor = LineSensor(17)
#right_sensor= LineSensor(27)

while True:
	left_detect  = int(left_sensor.value)
	right_detect = int(right_sensor.value)
	print(left_detect, right_detect)
