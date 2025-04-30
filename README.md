# Automated Break Reminder App
This Python script is a simple yet powerful tool for sending desktop notifications.  
Designed with beginners in mind, it leverages the `plyer` library to create customizable reminders.  
Users can define the notification title, message, interval, and repetition count, making it perfect for managing tasks, breaks, or daily routines.

---

##  Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)
- [Use Case Ideas](#use-case-ideas)
- [License](#license)


## Features  
- Simple input-based UI (no GUI needed)
- Sends customizable notifications with a title and message.  
- Allows users to specify the interval (in minutes) and the number of notifications.  
- Uses the `plyer` library for cross-platform notification support.
- Cross-platform compatibility (Windows, macOS, Linux)  
- Built entirely in Python — great for beginners


## Requirements  
- Python 3.x  
- `plyer` library  

## Installation  
1. Install Python from [python.org](https://www.python.org/).  
2. Install the `plyer` library by running:  
    ```bash  
    pip install plyer  
    ```  

## Program Code
```python
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
```

## Usage  
1. Save the script to a file, e.g., `notification_app.py`.  
2. Ensure you have an icon file (e.g., `green_technology_pWJ_icon.ico`) at the specified path:  
    ```
    C:\Users\hp\Alert\green_technology_pWJ_icon.ico  
    ```  
3. Run the script:  
    ```bash  
    python notification_app.py  
    ```  
4. Follow the prompts to:  
    - Enter the notification title.  
    - Enter the notification message.  
    - Specify the interval (in minutes).  
    - Specify the number of notifications.  

## Example  
```plaintext  
Enter the title of the notification: Reminder  
Enter the message of the notification: Take a break!  
Enter the interval in minutes: 30  
Enter the number of times to send the notification: 3  
```  
This will send a notification every 30 minutes, 3 times in total.  

## Notes  
- Ensure the icon file path is correct.  
- Notifications will be visible for 10 seconds by default. 

## Use Case Ideas
- Hydration reminders
- Study session alerts
- Break time prompts
- Posture or eye break checks
- Repeating task reminders
- Mental health & mindfulness pings



## License  
This project is licensed under the MIT License.  

You’re free to use, share, and modify it!



