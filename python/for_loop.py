# frutes = ["apple", "banana", "cherry"]
# for i in frutes:
#     print(i)
#/////////////////////////////////////////////////////////////
# this method use to change input to list and string to number
student_hights = input().split()
print(student_hights)
for n in  range(0,len(student_hights)):
    student_hights[n] = int(student_hights[n])
    print(student_hights)

avg = 0
for x in student_hights:
    avg += student_hights

average = avg/len(student_hights)
print("Average height is : ", average)