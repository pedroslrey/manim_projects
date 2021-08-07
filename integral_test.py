from manimlib.imports import *
import numpy as np
import math

class IntegralScene(GraphScene):
	CONFIG = {
	"x_min" : -2,
	"x_max" : 2,
	"y_min" : -1.5,
	"y_max" : 1.5,
	"graph_origin" : ORIGIN ,
	"function_color" : RED ,
	"axes_color" : BLUE,
	"x_tick_frequency": 0.5,
	"x_labeled_nums" :np.arange(-2,3),
	}

	def construct(self):
		self.setup_axes(animate=True)
		func_graph=self.get_graph(self.func_to_graph, self.function_color)
		graph_lab = self.get_graph_label(func_graph, label = "x^2")
		 
		self.play(ShowCreation(func_graph))
		self.play(ShowCreation(graph_lab))
		self.fill_with_rectangles(0, 1, self.func_to_graph, speed=0)

	def func_to_graph(self, x):
		return x*x

	def fill_with_rectangles(self, x0, x1, func, speed=3):
		step = 0.5
		while step > 0.0025:
			xs = []
			for i in np.arange(x0, x1, step):
				rect = Polygon(
					self.coords_to_point(i, 0),
					self.coords_to_point(i + step, 0),
					self.coords_to_point(i + step, self.func_to_graph(i + step)),
					self.coords_to_point(i, self.func_to_graph(i + step)), fill_color=GREEN, fill_opacity=1, color=GREEN)
				xs.append(rect)
				self.mobjects = [rect] + self.mobjects
				self.wait(speed*step/((x1-x0)))
			self.wait(1)
			for rect in xs:
				self.remove(rect)
			step /= 2	