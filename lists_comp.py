# List Comprehensions
# What problem does it solve?

# List comprehension gives you a short and clean way to create a list from another iterable.

# Instead of writing:

numbers = []

for number in range(1, 6):
    numbers.append(number * 2)

# you can write:

numbers = [number * 2 for number in range(1, 6)]

#  You can also filter values using if



#  Transforming Data
#  Suppose we have

names = ["gull", "ahmed", "kamran"]

# we want uppercase names

# Normal we cn write this

upper_names = []

for names in names:
    upper_names.append(names.upper())


# but by using list comprehension:

upper_names = [name.upper() for name in names]
print(upper_names)


# So list comprehensions are useful for both:

# filtering
# transforming





#  Problem: Filter and Transform Student Scores


# You are given a list of student scores:

# scores = [45, 78, 90, 32, 65, 88, 50, 95]

# You need to:

# Find scores that are 60 or higher.
# Add 5 bonus marks to each passing score.
# Store the final scores in a new list.
# Print the new list.

# Expected output
# [83, 95, 70, 93, 100]


# Write this using a normel loop first

scores = [45, 78, 90, 32, 65, 88, 50, 95]

final_scores = []

for score in scores:
    if score >= 60:
       final_scores.append(score + 5)

print(final_scores)       


# Convert it to List Comprehension

# Our loop has three important parts:

# What should we put into the new list?

# score + 5

# Where are we getting the values from?

# for score in scores

# Which values do we want?

# if score >= 60

# Put them together:

final_scores = [score + 5 for score in scores if score >= 60]

scores = [45, 78, 90, 32, 65, 88, 50, 95]

final_scores = [score + 5 for score in scores if score >= 60]

print(final_scores)