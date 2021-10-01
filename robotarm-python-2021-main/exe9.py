from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.speed = 3


for i in range(4):
    robotArm.grab()
    for i in range(1,6):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(4):
        robotArm.moveLeft()
for i in range(4):
    robotArm.moveLeft()
    robotArm.grab()






robotArm.wait()