"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Motor

MAX_Speed = 1

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

L1 = robot.getDevice('R1')
R1 = robot.getDevice('L1')
R2 = robot.getDevice('R2')
R3 = robot.getDevice('R3')

L1.setPosition(float(0.0))
R1.setPosition(float(0.0))
R2.setPosition(float(0.0))
R3.setVelocity(float(0.0))


L1.setVelocity(MAX_Speed)
R1.setVelocity(MAX_Speed)
R2.setVelocity(MAX_Speed)
R3.setVelocity(MAX_Speed)

i=0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    L1.setPosition(float(i))
    R1.setPosition(float(i))
    R2.setPosition(float(i))
    R3.setPosition(float(i))
    i = i+1 
    pass

# Enter here exit cleanup code.
