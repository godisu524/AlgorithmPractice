n =int(input())
grades={}
for i in range(n):
    name,grade = map(str,input().split())
    grades[name]=int(grade)

grades = {k: v for k, v in sorted(grades.items(), key=lambda item: item[1])}
grade = {k:v for k,v in sorted(grades.items(),key= lambda item:item[1])}
print(items)
for i in items:
    print(i[0])

print(grades)
print(grade)
