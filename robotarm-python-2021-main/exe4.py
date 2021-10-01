from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.grab()
for i in range(2):
    robotArm.moveRight()
robotArm.drop()

for i in range(2):
    robotArm.moveLeft()
robotArm.grab()

for i in range(2):
    robotArm.moveRight()
robotArm.drop()

for i in range(2):
    robotArm.moveLeft()
robotArm.grab()

for i in range(1):
    robotArm.moveRight()
robotArm.drop()

for i in range(1):
    robotArm.moveRight()
robotArm.grab()

for i in range(1):
    robotArm.moveLeft()
robotArm.drop()

for i in range(1):
    robotArm.moveRight()
robotArm.grab()

for i in range(1):
    robotArm.moveLeft()
robotArm.drop()

robotArm.wait()