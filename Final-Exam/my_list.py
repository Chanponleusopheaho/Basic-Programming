import numpy
score_of_students = [30, 35, 98, 54, 76, 89, 15, 64, 73, 47]
print("All my number:" , score_of_students)
# Calculate Mean
Mean = numpy.mean(score_of_students)
print(" The mean of the list is:",Mean)

# Calculate Median
Median = numpy.median(score_of_students)
print(" The median of the list is:",Median)

# Calculate Mode
from scipy import stats
Mode = stats.mode(score_of_students)
print("The mode of the list is:",Mode)
#The mode() method returns a ModeResult object that contains the mode number (15), and count (how many times the mode number appeared (1)).