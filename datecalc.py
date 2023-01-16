import datetime
def date_calculator():
  # Print the menu
  print('1. Add days to a date')
  print('2. Subtract days from a date')
  print('3. Calculate the difference between two dates')
  print('4. Quit')
  # Get the user's selection
  choice = int(input('Enter your choice: '))
  # Perform the selected operation
  if choice == 1:
    # Get the date and number of days to add
    date = input('Enter a date (YYYY-MM-DD): ')
    days = int(input('Enter the number of days to add: '))
    # Convert the date to a datetime object
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    # Add the specified number of days to the date
    result = date + datetime.timedelta(days=days)
    # Print the result
    print(f'\n{days} days added to {date.strftime("%Y-%m-%d")} is {result.strftime("%Y-%m-%d")}\n')
  elif choice == 2:
    # Get the date and number of days to subtract
    date = input('Enter a date (YYYY-MM-DD): ')
    days = int(input('Enter the number of days to subtract: '))
    # Convert the date to a datetime object
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    # Subtract the specified number of days from the date
    result = date - datetime.timedelta(days=days)
    # Print the result
    print(f'\n{days} days subtracted from {date.strftime("%y-%m-%d")} is {result.strftime("%Y-%m-%d")}\n')
  elif choice == 3:
    # Get the two dates
    date1 = input('Enter the first date (YYYY-MM-DD): ')
    date2 = input('Enter the second date (YYYY-MM-DD): ')
    # Convert the dates to datetime objects
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    # Calculate the difference between the dates
    difference = date2 - date1
    # Print the result
    print(f'\nThe difference between {date1.strftime("%Y-%m-%d")} and {date2.strftime("%Y-%m-%d")} is {difference.days} days\n')
  elif choice == 4:
    # Quit the program
    exit(1)
    return False
  else:
    print('Invalid choice')
# Run the date calculator
while True:
  date_calculator()
