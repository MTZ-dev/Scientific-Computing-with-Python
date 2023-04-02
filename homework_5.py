#EXERCISE 5.1

import os

def find_pdf_size(top):
    size = 0
    for root_path, dir_names, file_names in os.walk(top):
        for file_name in file_names:
            if file_name.endswith('.pdf'):
                file_path = os.path.join(root_path, file_name)
                size += os.path.getsize(file_path)
    return size

pdf_size = find_pdf_size(".")
print(pdf_size)


#EXERCISE 5.2
print("\n")

import datetime

def print_working_days(date1, date2):
    start_date = datetime.date.fromisoformat(date1)
    end_date = datetime.date.fromisoformat(date2)
    td = datetime.timedelta(days=1)
    while start_date < end_date:
        if start_date.weekday() < 5:
            print(start_date.isoformat())
        start_date += td

print_working_days("2023-02-21", "2023-04-02")


#EXERCISE 5.3
print("\n")

import random
import matplotlib.pyplot as plt

def random_walk(start):
    position = start
    for i in range(100):
        yield position
        position += random.choice([-1, 1])

x_values = range(100)
y_values = []

for position in random_walk(0):
    y_values.append(position)
    print(position)


plt.plot(x_values, y_values, label=f"Random Walking Experiment")
plt.legend()
plt.xlabel("Number of steps")
plt.ylabel("Position")
plt.show()

#in order to enable the plot's appearance on my machine (UBUNTU) I needed to run the following:
#python -m pip install -U matplotlib
#sudo apt-get install python3-tk