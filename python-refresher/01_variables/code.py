x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)

name = "Rolf"
greeting = "Hello, {}"
withname = greeting.format(name)
print(withname)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"Your house is {square_meters:.2f} square meters")

user_age = int(input("Enter your age: "))
age_in_months = user_age * 12

print(f"Your age in months is {age_in_months}")

day_of_week = input("What day of the week is it today? ")
if day_of_week == "Monday":
    print("Have a great start of your week")

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


def hello():
    print("Hello world")


hello()


def user_age_in_seconds():
    user_age = int(input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is equals to: {age_seconds:,} seconds.")


user_age_in_seconds()
