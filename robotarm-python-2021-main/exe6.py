from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

for i in range(7):
    robotArm.moveRight()

for i in range(8):
    for i in range(1):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
    for i in range(2):
        robotArm.moveLeft()
robotArm.wait()