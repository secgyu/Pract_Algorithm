angle1 = input()
angle2 = input()
angle3 = input()

if int(angle1) == 60 and int(angle2) == 60 and int(angle3) == 60:
    print('Equilateral')
elif int(angle1) + int(angle2) + int(angle3) == 180 and int(angle1) == int(angle2) or int(angle2) == int(angle3) or int(angle1) == int(angle3):
    print('Isosceles')
elif int(angle1) + int(angle2) + int(angle3) == 180 and int(angle1) != int(angle2) and int(angle2) != int(angle3) and int(angle1) != int(angle3):
    print('Scalene')
elif int(angle1) + int(angle2) + int(angle3) != 180:
    print('Error')
