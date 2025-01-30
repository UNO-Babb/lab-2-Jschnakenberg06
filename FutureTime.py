#FutureTime.py
#Name:Jonas Schnakeneberg
#Date:1/30/2025
#Assignment:Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later
  print("Future Time Calculator")

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  

  #Calculate the time after the user-supplied time has passed.
  # Getting curent time from system, storing to variable
  now = datetime.datetime.now()
  currentMinute = (now.minute)
  currentHour = (now.hour - 6) % 24


  #Do not use any if statements in calculating the time.
  # Ask user for input
  moreMins = int(input("Enter minutes to add: "))
  moreHours= int(input("Enter hours to add: "))

  #Output the future time in standard format "HH:MM"
  # Calculate the New Time
  extraHours = (currentMinute + moreMins) // 60
  futureHours = (currentHour + moreHours + extraHours) % 24
  futureMinutes = (currentMinute + moreMins) % 60
  

  print("Future Time: " + str(futureHours) + ":" + str(futureMinutes))
  print(futureMinutes)
  print(futureHours)



if __name__ == '__main__':
  main()
