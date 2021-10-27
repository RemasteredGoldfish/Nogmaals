from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

robotArm.speed = 3
moveRight = 9
moveLeft = 8
for movement in range (5):
    robotArm.grab()
    [robotArm.moveRight() for movement in range (moveRight)]
    robotArm.drop() 
    [robotArm.moveLeft() for movement in range (moveLeft)]
    moveRight = moveRight -2
    moveLeft = moveLeft -2
robotArm.wait()