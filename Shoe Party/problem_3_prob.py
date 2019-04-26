import numpy as np
import matplotlib.pyplot as plt
from shoes_lib import *

trials = 500

max_people = 100
data = [1 - prob_match(num_people - 1, trials) for num_people in range(1, max_people + 1)]

plt.plot(range(1, max_people + 1), data, 'ro', label = "Experimental Data")
plt.plot(range(1, max_people + 1), (1/np.exp(1)) * np.ones(max_people), 'b-', label = "Theoretical Value")
plt.xlabel("Number of People")
plt.ylabel("Number of Correctly Returned Shoes")
plt.title("Problem 3(Probability)")
plt.axis([0, max_people + 1, -0.5, 1.5])
plt.legend(loc = "lower right")
plt.show()