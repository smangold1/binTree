import os 
from typing import List;
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def read_input(file_name):
    current_path = os.path.dirname(__file__)
    lines : List[int] = []
    try:
        with open(os.path.join(current_path, file_name), 'r') as file:
            for line in file:
                lines.append(int(line.strip()))  
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

class binTree():
    def __init__(self):
        self.testlist = []

    def add(self, value):
        if value in self.testlist:
            print(f"{value} is already in the list")
        else:
            self.testlist.append(value)
            self.testlist.sort()

    def __contains__(self, value):
        f_entry = 0                             # first spot in the array
        l_entry = len(self.testlist) - 1        # last spot in the array

        while f_entry <= l_entry:
            m_entry = (l_entry + f_entry) // 2  # Correct the middle index calculation

            if self.testlist[m_entry] == value:
                return True  
            elif self.testlist[m_entry] < value:
                f_entry = m_entry + 1 
            else:
                l_entry = m_entry - 1 
        return False
    
    def fill_list(self, values):
        for value in values:
            self.add(value)

    def findValue(self, value):
        if value in self.testlist:
            print(f"{value} is in the list.")
        else:
            print(f"{value} is not in the list.")

class Frequency:
    def __init__(self):
        self.currentFrequency = 0

    def calibrate(self, num):
        self.currentFrequency += num

lines = read_input('input.txt')

g = Frequency()

seen_frequencies = binTree()
repeat_frequency = None
times = []
x = []
start_time = time.time()
i = 0 

while i < 5000:
    for line in lines:
        i += 1
        g.calibrate(line)

        ret_val = g.currentFrequency in seen_frequencies
        if i % 100 == 0:
            times.append((time.time() - start_time))
            x.append(i)
            #start_time = time.time() 
            #print(time.time() - start_time)
            #print(i)

        if ret_val:
            repeat_frequency = g.currentFrequency
            break
        #print(f"added {g.currentFrequency} at {len(seen_frequencies)}")
        seen_frequencies.add(g.currentFrequency)


y = times
#x = np.linspace(1, len(times),len(times))

plt.plot(x, y, label='Data Points', color='blue', linestyle='--')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Sample Plot')
plt.legend()

plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()