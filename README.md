
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

