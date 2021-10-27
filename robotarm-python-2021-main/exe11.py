from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3

moveL = 8
for movement in range (9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        [robotArm.moveRight() for movement in range (9)] 
        robotArm.drop()
        [robotArm.moveLeft() for movement in range (moveL)]
    else:
        robotArm.drop()
        robotArm.moveRight()
        moveL = moveL - 1