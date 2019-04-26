import numpy as np
import matplotlib.pyplot as plt
from shoes_lib import *


trials = 500


max_people = 100
data = [exp_value(num_people, trials) for num_people in range(1, max_people + 1)]


plt.plot(range(1, max_people + 1), data, 'ro', label = "Experimental Data")
plt.plot(range(1, max_people + 1), np.ones(max_people), 'b-', label = "Theoretical Value")
plt.xlabel("Number of People")
plt.ylabel("Number of Correctly Returned Shoes")
plt.title("Problem 1")
plt.axis([0, max_people + 1, 0, 2])
plt.legend(loc = "lower right")
plt.show()
