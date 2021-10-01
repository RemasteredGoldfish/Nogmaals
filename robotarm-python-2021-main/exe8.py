from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

robotArm.speed = 4
robotArm.moveRight()

for i in range(7):
    for i in range(8):
        robotArm.grab()
        robotArm.moveRight()
    for i in range(8):
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()