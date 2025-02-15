from datetime import datetime, timedelta

def calculate_attendance_hours(current_date, last_date, goal_attendance, current_attendance, total_class_hours_per_week):
    # Convert date strings to datetime objects
    current_date = datetime.strptime(current_date, '%Y-%m-%d')
    last_date = datetime.strptime(last_date, '%Y-%m-%d')
    
    # Calculate the total number of days and weeks in the period
    total_days = (last_date - current_date).days + 1
    total_weeks = total_days / 7

    # Calculate the total number of hours required for the goal attendance
    goal_total_hours = goal_attendance * total_weeks * total_class_hours_per_week

    # Calculate the total number of hours attended based on the current attendance percentage
    current_total_hours = current_attendance * total_weeks * total_class_hours_per_week

    # Calculate the remaining hours needed to reach the goal attendance
    remaining_hours_needed = goal_total_hours - current_total_hours

    # Calculate the remaining weeks
    remaining_weeks = total_days / 7

    # Calculate the required hours per week to reach the goal attendance
    if remaining_weeks > 0:
        required_hours_per_week = remaining_hours_needed / remaining_weeks
        if required_hours_per_week > total_class_hours_per_week:
            return "Unable to reach", None
        bunk_hours_per_week = total_class_hours_per_week - required_hours_per_week
        return required_hours_per_week, bunk_hours_per_week
    else:
        return "Unable to reach", None

# User input
current_date = input("Enter the current date (YYYY-MM-DD): ")
last_date = input("Enter the last date (YYYY-MM-DD): ")
goal_attendance = float(input("Enter the goal attendance percentage (as a decimal, e.g., 0.85 for 85%): "))
current_attendance = float(input("Enter the current attendance percentage (as a decimal, e.g., 0.75 for 75%): "))
total_class_hours_per_week = float(input("Enter the total number of class hours per week: "))

# Calculate required hours per week to reach the goal attendance and bunk hours per week
required_hours_per_week, bunk_hours_per_week = calculate_attendance_hours(current_date, last_date, goal_attendance, current_attendance, total_class_hours_per_week)

if required_hours_per_week == "Unable to reach":
    print("Unable to reach the goal attendance.")
else:
    print(f"Required hours per week to reach the goal attendance: {required_hours_per_week}")
    print(f"Hours you can bunk per week and still reach the goal attendance: {bunk_hours_per_week}")
