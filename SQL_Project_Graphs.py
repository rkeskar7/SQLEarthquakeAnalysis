import matplotlib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score


number_of_earthquakes_mag = [14996, 1750, 169, 23, 3]
labels = ['Minor', 'Light', 'Moderate', 'Strong', 'Major']
plt.bar(range(len(number_of_earthquakes_mag)), number_of_earthquakes_mag) #Plotting the numbers
plt.title('Figure 1: Number of earthquakes per classification')
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Number of Earthquakes based on classification')
axis = plt.subplot() #Creating a subplot
axis.set_xticks([0, 1, 2, 3, 4])
axis.set_xticklabels(labels)
plt.show()

plt.scatter(range(len(number_of_earthquakes_mag)), number_of_earthquakes_mag)
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Number of Earthquakes based on classification')
plt.title('Figure 2: Scatterplot of Number of earthquakes per classification')
axis_scatter = plt.subplot() #Creating a subplot
axis_scatter.set_xticks([0, 1, 2, 3, 4])
axis_scatter.set_xticklabels(labels)
plt.show()


###################################

average_horizontal_distance_epicenter = [0.33, 0.5, 0.5, 1.21, 0.51]
plt.bar(range(len(average_horizontal_distance_epicenter)), average_horizontal_distance_epicenter) #Plotting the numbers
plt.title('Figure 3: Average Horizontal Distance from the Epicenter per Classification (kilometers) ')
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Average Horizontal Distance (kilometers)')
axis_1 = plt.subplot() #Creating a subplot
axis_1.set_xticks([0, 1, 2, 3, 4])
axis_1.set_xticklabels(labels)
plt.show()

plt.scatter(range(len(average_horizontal_distance_epicenter)), average_horizontal_distance_epicenter)
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Average Horizontal Distance (kilometers)')
plt.title('Figure 4: Scatterplot of Average Horizontal Distance from the Epicenter per Classification (kilometers) ')
axis_1_scatter = plt.subplot() #Creating a subplot
axis_1_scatter.set_xticks([0, 1, 2, 3, 4])
axis_1_scatter.set_xticklabels(labels)
plt.show()


####################################
average_depth = [6.35, 8.62, 9.53, 13.69, 12.24]
plt.bar(range(len(average_depth)), average_depth) #Plotting the numbers
plt.title('Figure 5: Average Depth of the Event per classification (kilometers) ')
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Average Depth of the Event (kilometers)')
axis_2 = plt.subplot() #Creating a subplot
axis_2.set_xticks([0, 1, 2, 3, 4])
axis_2.set_xticklabels(labels)
plt.show()

plt.scatter(range(len(average_depth)), average_depth)
plt.xlabel('Classification of Earthquakes')
plt.ylabel('Average Depth of the Event (kilometers)')
plt.title('Figure 6: Scatterplot of Average Depth of the Event per classification (kilometers) ')
axis_2_scatter = plt.subplot() #Creating a subplot
axis_2_scatter.set_xticks([0, 1, 2, 3, 4])
axis_2_scatter.set_xticklabels(labels)
plt.show()
