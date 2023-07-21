# Importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Helvetica Neue"
plt.rcParams["font.size"] = 14

# Defining a function to read data from a file and return a numpy array
def read_data(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        # Ignoring the comment lines
        content = [row for row in content if not row.startswith("#") and not row.startswith("@")]
        # Converting each row to a list of floats
        content = [[float(col) for col in row.split()] for row in content]
    return np.array(content)

# Reading the data from the single file
data = read_data("gyr_all.xvg")
# Extracting the second column
column = data[:, 1]

fig = plt.figure(figsize=(6 ,6) ,facecolor='w')
# Plotting a histogram of the column with 20 bins, normalized counts and separation
plt.hist(column ,bins=20 ,weights=np.ones(len(column))/len(column) ,rwidth=0.9)
# Adding labels
plt.xlabel("Radius of gyration (nm)")
plt.ylabel("Normalized counts")
# Saving the plot as an image file with 300 dpi resolution
plt.savefig("histogram_gyr.png" ,dpi=300)