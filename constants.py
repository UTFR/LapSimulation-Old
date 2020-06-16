"""
Constants.py
"""


WEIGHT_DIST = .5 #static weight dist 50-50%
COG_HEIGHT = 0.27 #center of gravity height
WHEEL_BASE = 1.6 #base area of the wheel
FRONTAL_AREA = 1.25#0.98 area of the front of the car (used for aero)
MASS = 251.45 #mass of car
LAT_TIRE = 1.6 #coefficient of friction
LONG_TIRE = 1 #coefficient of frinction
WHEEL_RADIUS = 0.229
AERO_BALANCE = 0.5 #balance between front and back of the car due to aero
BRAKE_BIAS = 0.7 #ratio of braking force between front and rear brakes
CL = 2.5 #this is also called CL
CD = 0.8 #drag coefficient --> 1.3

AIR_DENSITY = 1.225
G = 9.81

GEAR_RATIOS = [2.071,1.6250,1.3330,1.1200,.9630,7.7605]

TORQUE_CURVE = [[3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500],
                #[27.4, 31.68, 35.99, 40.27, 44.5, 47.09, 46.08, 43.81, 41.53, 39.26, 36.98, 34.72, 32.44, 30.17, 27.89, 25.62]]
                [40.27, 40.27, 40.27, 40.27, 44.5, 47.09, 46.08, 43.81, 41.53, 39.26, 36.98, 34.72, 32.44, 30.17, 27.89, 25.62]]
                #car starts slipping at around 4000 rpm. when it starts slipping that means 

                #how to launch a manual transmission car:
                #1. rev the engine to some rpm (low torque engine --> higher rpm)
                #2. there is now difference between clutch rpm and flywheel rpm
                #3. You release the clutch (smoothly)
                #4. by doing this the torque that the engine would be applying at that high 
                # 	rpm is now being immediatly applied to the wheels, at any lower speed
                # 	the clutch is making you lose rotational speed but b/c of newtons law, the force of the engine
                #	has to be reacted to, so torque is the same
                #	THE CLUTCH IS SLIPPING NOT THE WHEEL

#radius, length, time
DATA_CORNER = [[26, 33, 24, 29, 20, 14, 35, 35, 24, 22, 19, 31, 30, 27, 35, 22, 35, 31, 25, 25, 27],
               [22, 6, 55, 8, 13, 2, 20, 6, 65, 9, 14, 13, 11, 14, 12, 10, 5, 5, 10, 10, 36],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#radius, length, time
DATA_STRAIGHT = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				 [15, 116, 46, 22, 97, 41, 28, 13, 15, 9, 81, 5, 3, 98, 38, 94, 6, 9, 7, 12],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


