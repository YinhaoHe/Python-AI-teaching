import matplotlib.pyplot as plt
with open("data.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()