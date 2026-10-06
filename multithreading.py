# What problem does Multithreading solve?

# Imagine your application needs to do two tasks:

# Task 1 → Download a file
# Task 2 → Send an email

# If you do them one after another:

# Download → wait → finish
#                     ↓
#                  Email → finish

# This can waste time while one task is waiting.

# With multithreading, multiple tasks can make progress concurrently:

# Thread 1 → Downloading
# Thread 2 → Sending email

# So:

# Multithreading allows multiple tasks to run concurrently within the same Python process.


# Thread

# A thread is a small unit of execution inside a program.

# For example:

# Program
# │
# ├── Main Thread
# │
# ├── Thread 1 → Download file
# │
# └── Thread 2 → Send email


# Simple Example

import threading
import time


def download_file():
    print("Downloading file.....")
    time.sleep(2)
    print("Download Complete")


thread = threading.Thread(target=download_file)

thread.start()
thread.join()

print("Program finished")




# Practical Problem
# Problem Statement

# You are building an application that needs to perform two independent tasks:

# Download a file
# Send an email

# Each task takes 2 seconds.

# Create two threads so both tasks can run concurrently.


import threading
import time

def download_file():
    print("Downloading file....")
    time.sleep(2)
    print("File download")

def send_email():
    print("Sending email...") 
    time.sleep(2)
    print("Email sent")

thread1 = threading.Thread(target=download_file) 
thread2 = threading.Thread(target=send_email)   

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print("All tasks completed")


# What to remember

# threading.Thread()
#        ↓
#     start()
#        ↓
# Thread runs
#        ↓
#     join()
#        ↓
# Wait for completion

