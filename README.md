# LinkedIn Automation Script

This script uses Selenium to automate interactions with LinkedIn, such as logging in, updating your profile summary, posting tweets, and creating polls. It includes methods for handling these tasks while logging the process.

## Features

- **Login**: Automates the login process using email and password.
- **Update Profile Summary**: Navigates to your profile and updates the summary section.
- **Post Tweet**: Allows you to post tweets to your LinkedIn feed.
- **Post Poll**: Enables the creation of polls with multiple options.

### Project Note

This LinkedIn Automation Script can be significantly enhanced and updated to improve its functionality and reliability. While it currently utilizes `sleep` methods to manage timing, switching to more robust Selenium methods would enhance its performance and efficiency.

#### Potential Improvements

- **Use of Explicit Waits**: Replace `sleep` with explicit waits to wait for specific elements to be present or clickable, reducing unnecessary delays and improving script efficiency.
- **Error Handling**: Implement more sophisticated error handling to manage different scenarios gracefully, including handling network issues and element not found errors.
- **Modular Design**: Break down methods into smaller, reusable components for better maintainability and readability.
- **User Input**: Enhance the script to accept dynamic input from the user, allowing for more flexible use cases.

#### Flaws

- **Over-reliance on `sleep`**: The use of `sleep` can lead to inefficiencies and may cause the script to fail if the timing does not align with the page load times.
- **Limited Error Handling**: Current error handling is basic and may not cover all potential exceptions, which could lead to unhandled crashes.
- **Static Credentials**: Hardcoding credentials is a security risk; a more secure method for managing credentials should be implemented.
- **Lack of Logging**: While basic logging is present, more detailed logs would help in debugging and tracking the script's execution.
- **Inflexible Methods**: The methods assume a fixed flow and do not allow for easy modifications or adaptations to different tasks or workflows.

## Usage

### Initialization

To start using the script, instantiate the `Alinkedin` class with your LinkedIn credentials:

```python
linkedin_bot = Alinkedin(email="your_email", password="your_password")
```
### Logging In

The `login` method is called automatically by other methods if the `login` parameter is set to `True`. Once you log in, you don't need to log in again for subsequent calls within the same session.

### Method Summaries

- **`login()`**: Logs into LinkedIn using the provided credentials.
- **`update_summary(summary_text, summary_link, login=True)`**: Updates your LinkedIn summary. Call with `login=True` to log in first.
- **`post_tweet(url, post="hello .", login=True)`**: Posts a tweet to your LinkedIn feed.
- **`post_poll(url, poll, login=True)`**: Creates a poll with the specified options.
- **`quit_driver()`**: Closes the browser session.

### Important Note

If you call a method with `login=True`, you will be logged in. For subsequent method calls, set `login=False` only if you want to skip logging in again. If you set it to `True`, the script will attempt to log in again, which may lead to errors if already logged in.

# Learn About Task Scheduler

You can watch a comprehensive video tutorial on using Task Scheduler by following this link:

[Watch the Video](https://youtu.be/ic4lUiDTbVI?si=j2jLh5IN-lbAcGbo)

## Overview

In this video, you'll learn:

- How to open Task Scheduler
- Creating and configuring tasks
- Setting triggers and actions
- Managing and troubleshooting scheduled tasks

## Key Features of Task Scheduler

- **Automate Tasks:** Schedule scripts, applications, or processes to run at specific times or events.
- **User-Friendly Interface:** Easy to navigate and set up tasks.
- **Flexibility:** Allows you to set conditions, triggers, and repeat schedules.

## Why Use Task Scheduler?

- **Efficiency:** Automate routine tasks to save time.
- **Consistency:** Ensure tasks run at designated times without manual intervention.
- **Monitoring:** Keep track of task execution and troubleshoot issues easily.

# Installing Selenium and Requests

To get started with Selenium and Requests in Python, follow these steps to install the necessary packages.

## Prerequisites

Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

## Step 1: Open Command Prompt

1. Press `Windows + R`, type `cmd`, and press `Enter` to open the Command Prompt.

## Step 2: Upgrade pip (Optional)

Before installing the packages, it's a good idea to upgrade pip, the Python package installer. Run the following command:

```bash
python -m pip install --upgrade pip

pip install selenium
pip install requests
```
# Prerequisites for `main.py`

Before running the `main.py` script, you need to set up a couple of URLs specific to your LinkedIn profile. Follow the steps below to obtain the necessary URLs and set them in your script.

## Steps to Set Up URLs

### 1. Create Post URL

1. Go to your LinkedIn profile page.
2. Click on the **Create Post** button.
3. Copy the URL from your browser's address bar.
4. Paste the copied URL into the `main.py` variable `create_post_url`.

   ```python
   create_post_url = "PASTE_YOUR_CREATE_POST_URL_HERE"
   ```
### 2. Update About URL

1. Go to your LinkedIn profile page.
2. Click on the About section or the Edit button next to it.
3. Copy the URL from your browser's address bar.
4. Paste the copied URL into the main.py variable update_about_url.

```python
update_about_url = "PASTE_YOUR_UPDATE_ABOUT_URL_HERE"
```
```Example Usage
# Create an instance
linkedin_bot = Alinkedin(email="your_email", password="your_password")

# Log in and update summary
linkedin_bot.update_summary("New summary text", "https://www.linkedin.com/in/yourprofile", login=True)

# Post a tweet
linkedin_bot.post_tweet("https://www.linkedin.com/feed/", "Check out my latest update!")

# Post a poll
poll_data = {
    'question': "What's your favorite programming language?",
    'options': ["Python", "JavaScript", "C++", "Java"]
}
linkedin_bot.post_poll("https://www.linkedin.com/feed/", poll_data)

# Quit the browser
linkedin_bot.quit_driver()
```
