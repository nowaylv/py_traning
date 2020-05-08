import matplotlib.pyplot as plt
'''
output = [1, 4, 9, 16, 25]
input = [1, 2, 3, 4, 5]
plt.plot(output, linewidth = 1)
plt.plot(input, output, linewidth = 1)
plt.title("matplotliib", fontsize = 20)
plt.xlabel("matpltlib_x", fontsize  = 14)
plt.ylabel("matpltlib_y", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 7)
'''


x_values = list(range(1, 255))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = (0, 0.8, 0.5), s = 10, edgecolor = 'none')
plt.axis([0, 100, 0, 10000])    
plt.axes().get_yaxis().set_visible(False)
plt.axes().get_xaxis().set_visible(False)
plt.show()  

