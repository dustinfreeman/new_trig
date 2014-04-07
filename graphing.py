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

	plt.ylim(-2*pi,2*pi)
	plt.xlim(-2*pi,2*pi)

	plt.plot(plt_range, y)

	plt.title(fun_name)
	plt.grid(True)
	plt.show()


if __name__ == '__main__':
	print("Close each plot to see the next.")

	#the old
	#graph_fun(sin, 'sin')
	
	#the new
	graph_fun(negtan, 'negtan')
	graph_fun(tofsin, 'tofsin')
	graph_fun(drin, 'drin')
	graph_fun(codrin, 'codrin')
	graph_fun(cocosine, 'cocosine')



