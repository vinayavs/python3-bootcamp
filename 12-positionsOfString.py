# DISPLAY ALL POSITIONS OF SUBSTRING FOR GIVEN STRING
s=input("Enter main string:")
subs=input("Enter sub string:")
flag = True
pos = 0
l = len(s)
while True:
    pos = s.find(subs, pos, l)
    if pos == -1:
        # print('Break executed')
        break
    print("Position Found at :",pos)
    flag = True
    pos += 1
if flag == False:
    print('Position Not Found')