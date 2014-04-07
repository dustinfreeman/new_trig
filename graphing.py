from new_trig import *
import matplotlib.pyplot as plt

#generating plot range
PLT_PRECISION = 100
plt_range = []
for i in range(-PLT_PRECISION, PLT_PRECISION):
	plt_range.append(2.0*pi*i/(PLT_PRECISION))

def graph_fun(fun, fun_name):
	y = []
	for x in plt_range:
		y.append(fun(x))

	plt.plot(plt_range, y)
	
	plt.title(fun_name)
	plt.show()


if __name__ == '__main__':
	graph_fun(sin, 'sin')



