from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

robotArm.speed = 4
for i in range(9):
    robotArm.moveRight()

for i in range(5):
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for i in range(2):
        robotArm.moveLeft()
robotArm.wait()