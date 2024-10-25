# pracitce with dictionaries

from collections import defaultdict
student_map = defaultdict(list)

grades = [3.2, 3.4, 3.6]
student_map["Alex"].append(grades[0])
student_map["Michael"].append(grades[1])
student_map["Nathan"].append(grades[2])

student_list = student_map.values()

print("KEYS AND VALUES")
for x, y in student_map.items():
    print(x, y)
    
print("\nKEYS")
for x in student_map:
    print(x)

print("\nVALUES")
for x in student_list:
    print(x)