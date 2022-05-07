# This program calculates average

print("Average program!")

# (total_grades)/number_of_grades
print("first we will get the total points you got")
total_points_got = []
number_of_grades_wanted = int(input("how may grades are you going to input? \nType Here: "))
for n in range(number_of_grades_wanted):
    points_you_got = float(input("Type your points here: "))
    total_points_got.append(points_you_got)
print("total points is: ", sum(total_points_got))
sum_total_points_got = sum(total_points_got)

print("now we will get the total points possible")
total_points = []
for n in range(number_of_grades_wanted):
    points_you_can_get = float(input("Type the max points here: "))
    total_points.append(points_you_can_get)
print("total point you can get is: ", sum(total_points))
sum_total_points = sum(total_points)
average = float((sum_total_points_got/sum_total_points)*100)
print("your average is: ", average, "%")

input("ok?")
exit()