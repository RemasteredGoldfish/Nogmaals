from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

robotArm.grab()

for i in range(9):
    robotArm.moveRight()
robotArm.drop()

for u in range(5):
    robotArm.moveLeft()
robotArm.grab()

for p in range(6):
    robotArm.moveRight()
robotArm.drop()

for r in range(2):
    robotArm.moveLeft()
robotArm.grab()

for u in range(2):
    robotArm.moveRight()
robotArm.drop()

robotArm.wait()