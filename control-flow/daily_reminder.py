task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()



match priority:
  case "high":
    print(f"Reminder: '{task}' is a {priority} priority task")
  
  case "medium":
    print(f"Reminder: '{task}' is a {priority} priority task")

  case "low":
    print(f"Reminder: '{task}' is a {priority} priority task")

if time_bound == "yes":
  print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
  print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have time")


    
