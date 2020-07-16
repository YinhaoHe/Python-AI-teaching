import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]
# y axis values
y = [2,4,1]
# Plot lines and/or markers to the Axes.
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()









import matplotlib.pyplot as plt

x = []
y = []
sets = int(input("Enter the number of sets of values: "))
for _ in range(sets):
	x.append(int(input("Enter x: ")))
for _ in range(sets):
	y.append(int(input("Enter y: ")))

plt.plot(x, y, 'go-')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()
plt.savefig('line.png')