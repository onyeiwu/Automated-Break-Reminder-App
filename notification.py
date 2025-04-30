import time 
from plyer import notification

#Create a function to send a notification
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Notification App',  # Set the app name
        app_icon= r"C:\Users\hp\Alert\green_technology_pWJ_icon.ico",  # Provide the correct path to your icon file
        timeout=10  # Notification will be visible for 10 seconds
    )
if __name__ == "__main__":
    # Set the title and message for the notification
    # You can also use input() to get user input for title and message
    title = input("Enter the title of the notification: ")
    message = input("Enter the message of the notification: ")
    interval_minutes = int(input("Enter the interval in minutes: "))
    number_of_times = int(input("Enter the number of times to send the notification: "))
    
    # Convert minutes to seconds
    interval_seconds = interval_minutes * 60  # Convert minutes to seconds
    
    # Loop to send the notification at the specified interval
    for i in range(number_of_times):
        send_notification(title, message)
        print(f"Notification {i + 1} sent!")
        time.sleep(interval_seconds)  # Wait for the specified interval before sending the next notification
        
    print("All notifications sent!")
# This script sends a notification at a specified interval and for a specified number of times.