from typing import Union

per : Union[int, float] = int(input("Enter Your Percentage: "))
grade: Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"        
else:
    grade = "Fail"

print(f"Dear Students your percentage is {per} now your calcualted grade is:\t {grade}")
print(grade)