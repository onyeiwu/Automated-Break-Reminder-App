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



