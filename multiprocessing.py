# Multiprocessing

# 1. What problem does Multiprocessing solve?

# Some tasks require a lot of CPU power, for example:

# Large mathematical calculations
# Image processing
# Video processing
# Data processing
# Machine learning computations

# For these tasks, threads may not give the performance you expect
# because of Python's GIL (Global Interpreter Lock).

# Multiprocessing solves this by creating separate processes.

# Main Program
#     │
#     ├── Process 1 → CPU work
#     ├── Process 2 → CPU work
#     └── Process 3 → CPU work

# Each process can run independently and use a CPU core.


# Process vs Thread

# Thread
# One Process
# │
# ├── Thread 1
# ├── Thread 2
# └── Thread 3

# Threads share the same process memory.

# Process
# Process 1 → Separate memory
# Process 2 → Separate memory
# Process 3 → Separate memory

# Processes are more isolated from each other.

# Simple rule
# I/O-bound → Multithreading
# CPU-bound → Multiprocessing


# Basic pattern:

# import multiprocessing
#
# process = multiprocessing.Process(target=my_function)
#
# process.start()
# process.join()


import multiprocessing
import time


# Simple Example

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")


if __name__ == "__main__":

    process = multiprocessing.Process(target=task)

    process.start()
    process.join()

    print("Program finished")


# --------------------------------------------------
# Practical Problem
# --------------------------------------------------

# Problem Statement:
#
# Imagine you have two CPU-intensive tasks:
#
# Task 1 → Process large dataset
# Task 2 → Process another large dataset
#
# Create two separate processes so they can run independently.


def process_data_one():
    print("Processing dataset 1.....")


def process_data_two():
    print("Processing dataset 2....")


if __name__ == "__main__":

    process1 = multiprocessing.Process(target=process_data_one)
    process2 = multiprocessing.Process(target=process_data_two)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processing completed")