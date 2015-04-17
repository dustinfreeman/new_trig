# An implementation of the 27 trig functions discussed in The Onion's article:
# Nation's Math Teachers Introduce 27 New Trig Functions
# http://www.theonion.com/articles/nations-math-teachers-introduce-27-new-trig-functi,33804/

# WASHINGTON - Adding to the six basic functions that have for years  made up the foundation of trigonometry, the nation's mathematics teachers reportedly introduced 27 new functions today that high schoolers will be expected to master. 
#"While the core of the trigonometry curriculum has traditionally consisted solely of sine, cosine, tangent, secant, cosecant, and cotangent, henceforth we will be including gasmin, negtan, cosvnx, and two dozen others, such as tosna and cotosna, that our pupils will need to have down pat in order to pass," Coolidge Senior High School trig teacher Robert Beckman said on behalf of the nation's math educators, emphasizing that students will be required to have full understanding of tofsin, pomen, cocosine, phyxyx, fotsin, and fostin as they apply to the various properties of equilateral, isosceles, and scalene triangles. 
#"Students will also need to know the corresponding graphs for the functions. For example, drin forms a sort of stepladder going up the X and Y axes, while codrin forms a stepladder going down. 
#I can assure you that all of these are absolutely crucial to understanding basic trigonometry, not to mention a requisite for anyone seeking to graduate and move on to college." 
#Beckman added that factoring will be cut from the math curriculum entirely because it's "annoying and too fucking hard sometimes."

from math import *

def gasmin(x):
	#returns the length, in letters, of the day of the day of the week,
	#	divided by the average letters of days in the week.
	days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
	total_letters = 0
	for day in days_of_the_week:
		total_letters += len(day)
	
	today = int(x/(2*pi)*len(days_of_the_week))
	#today can be negative
	return len(days_of_the_week[today]) / (total_letters/(1.0*len(days_of_the_week)))

def negtan(x):
	# "I don't know what I expected"
	return -tan(x)

def cosvnx(x):
	value = 0

	x_norm = (x/pi + 1) % 2 - 1
	if x_norm < -1/3.0:
		# v
		value = 3*abs(x_norm + 2/3.0)
	elif x_norm < 1/3.0:
		# n
		value = 1 + -3*x_norm**2
	else:
		# x
		value_upwards = x_norm - 1/3.0
		value_downwards = 1 - (x_norm - 1/3.0)
		if x_norm % 0.02 > 0.01:
			value = value_upwards
		else:
			value = value_downwards
	return value #cos(value)

def tosna(x):
	pass

def cotosna(x):
	pass


def tofsin(x):
	# tof = time of flight.
	# for each x, this function returns 
	# 	the time of flight (distance) between the origin (0,0)
	# 	and sin(x)

	return sqrt(x**2 + sin(x)**2)

def pomen(x):
	# returns the the average number of seeds in a pomegranate of radius x (in furlongs).
	# formula courtesy of the US Department of Agriculture ("Statistical Modeling of Fruit", 1975, 6.3 p5, US Department of Agriculture)
	GROWTH_FACTOR = gasmin("thursday")
	return (x / GROWTH_FACTOR) + negtan(pi*x)

def cocosine(x):
	# "What does 'co' mean anyway? opposite, right?
	# This function returns the string-reverse of cos(x)
	_y = cos(x)
	
	#small values get awkward to reverse with e-notation
	if abs(_y) < 1e-9:
		_y = 0

	str_y = str(_y)

	#must be careful if there is a negative sign
	if (_y < 0):
		str_y = str_y[1:]

	str_y_rev= str_y[::-1]
	return copysign(float(str_y_rev), _y)

def phyxyx(x):
	pass

def fotsin(x):
	pass

def fostin(x):
	pass


def drin(x):
	# drin forms a sort of stepladder going up the X and Y axes
	return copysign(round(abs(x)),x)

def codrin(x):
	# codrin forms a stepladder going down
	# set to -drin(x)
	return -copysign(round(abs(x)),x)


#Need 14 more functions than those named so far.

