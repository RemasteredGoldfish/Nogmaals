from RobotArm import RobotArm

robotArm = RobotArm()

robotArm.speed = 3

robotArm.randomLevel(1,7)
for movement in range (9):
    robotArm.grab()
    color = robotArm.scan()
    if color in ['white','red','green','blue','yellow']:            
        [robotArm.moveRight() for movement in range (9)]          
        robotArm.drop()
        [robotArm.moveLeft() for movement in range (9)]
    else:                                                               
        robotArm.wait()

robotArm.wait()