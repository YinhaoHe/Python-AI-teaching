import matplotlib.pyplot as plt
x = range(10)
y = [_ * 3 for _ in x]
plt.plot(x, y, label = 'y = x * 3')

plt.xlim(0, 15)
plt.ylim(0, 35)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Draw a line with limit value')

plt.show()









# import matplotlib.pyplot as plt
# X = range(1, 50)
# Y = [value * 3 for value in X]
# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# # shows the current axis limits values
# print(plt.axis()) 
# # set new axes limits
# # Limit of x axis 0 to 100
# # Limit of y axis 0 to 200
# plt.axis([0, 100, 0, 200]) 
# # Display the figure.
# plt.show()
# print(plt.axis()) 