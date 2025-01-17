#!/usr/bin/env python3

# Copyright © 2022 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_write_speed.py input_file.csv")
    print("Example:")
    print("  plot_write_speed.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

# Try to open the CSV file specified.
with open(input_csv) as csv_input:
    # And open this file as CSV
    csv_reader = csv.reader(csv_input)

    # Skip header
    next(csv_reader, None)
    rows = 0

    # Read all rows from the provided CSV file
    data = [(int(row[0]), int(row[1]), int(row[2]),
             int(row[3]), int(row[4]),
             int(row[5]), int(row[6])) for row in csv_reader]
    print(data)


# data to be plotted
records = [item[0] for item in data]

time1 = [item[1]*60+item[2] for item in data]
durations1 = [1000/item for item in time1]

time2 = [item[3]*60+item[4] for item in data]
durations2 = [1000/item for item in time2]

time3 = [item[5]*60+item[6] for item in data]
durations3 = [1000/item for item in time3]

# Create new graph
plt.plot(records, durations1, label="Original")
plt.plot(records, durations2, label="w/o UPDATE")
plt.plot(records, durations3, label="proper index")

# Title of a graph
plt.title("Write speed")

# Add a label to x-axis
plt.xlabel("Records in database")

# Add a label to y-axis
plt.ylabel("Writes per second")

plt.legend(loc="upper right")

# Set the plot layout
plt.tight_layout()

# And save the plot into raster format and vector format as well
plt.savefig("write_speed_3.png")
plt.savefig("write_speed_3.svg")

# Try to show the plot on screen
plt.show()
