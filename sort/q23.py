n = int(input())
students=[]
for _ in range(n):
    name, korean, english, math = input().split()
    students.append([name, int(korean), int(english), int(math)])


#students.sort()
#students.sort(key = lambda x :x[3], reverse = True)
#students.sort(key = lambda x :x[2], reverse = False)
#students.sort(key = lambda x :x[1], reverse = True)

#또는
students.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))
print(students)

