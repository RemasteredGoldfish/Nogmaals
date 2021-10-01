from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

robotArm.speed = 2
#for i in range(4):
    #for i in range():
        #robotArm.grab()
        #robotArm.moveRight()
    #robotArm.drop()
    #for i in range(8):
        #robotArm.moveLeft()
    #for i in range(7):
        #robotArm.grab()
        #robotArm.moveRight()
for i in range(1):
    for i in range(9):
        robotArm.grab()
        robotArm.moveRight()

    for i in range(8):
        for i in range(1):
            robotArm.drop()
            robotArm.moveLeft()



robotArm.wait() 