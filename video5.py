from manimlib.imports import *
import numpy as np
import math
from collections import defaultdict

class graph(object):
	def __init__(self, n, scene):
		self.graph = [[] for i in range(n)]
		self.size = n
		self.vertex_coord = {i: np.array([0, 0, 0]) for i in range(self.size)}
		self.vertex_obj = {i: Dot(np.array([0, 0, 0])) for i in range(self.size)}
		self.arc_obj = {(i, j): Line(np.array([0, 0, 0]), np.array([0, 0, 0])) for i in range(self.size) for j in range(self.size)}
		self.scene = scene

	def set_vertex_coord(self, u, x_coord, y_coord, color=BLUE):
		self.vertex_coord[u] = np.array([x_coord, y_coord, 0])
		self.vertex_obj[u] = Dot(self.vertex_coord[u], color=color)

	def add_arc(self, u, v, color=WHITE):
		self.graph[u].append(v)
		self.graph[v].append(u)
		self.arc_obj[(u, v)] = Line(self.vertex_coord[u], self.vertex_coord[v], color)

	def set_graph(self, graph):
		self.graph=graph
		for u in range(self.size):
			for v in graph[u]:
				self.arc_obj[(u, v)] = Line(self.vertex_coord[u], self.vertex_coord[v], color=WHITE)
				
	def change_arc_color(self, u, v, color):
		self.scene.remove(self.arc_obj[(u, v)])
		self.arc_obj[(u, v)] = Line(self.vertex_coord[u], self.vertex_coord[v], color=color)
		self.scene.add(self.arc_obj[(u, v)])
		self.scene.add(self.vertex_obj[u])
		self.scene.add(self.vertex_obj[v])

	#NOTE: path[1] = path[-1] if you want to draw a cicle
	def show_path(self, path, color=ORANGE, delay=0.5, erase=False):
		for i in range(len(path)-1):
			self.change_arc_color(path[i], path[i+1], color)
			self.scene.wait(delay)
			if erase: self.change_arc_color(path[i], path[i+1], WHITE)

	def draw(self):
		for u in range(self.size):
			for v in self.graph[u]:
				self.scene.add(Line(self.vertex_coord[u], self.vertex_coord[v]))
		for u in range(self.size): self.scene.add(self.vertex_obj[u])

class Video(Scene):
	def construct(self):		
		example_graph = graph(5, self)
		example_graph.set_graph([[1, 2, 4], [0, 2, 4], [0, 1, 3, 4], [2, 4], [0, 1, 2, 3]])
		example_graph.set_vertex_coord(0, -3.5-0.75, -1.5)
		example_graph.set_vertex_coord(1, -3.5+0.75, -1.5)
		example_graph.set_vertex_coord(2, -3.5+0.75, 0)
		example_graph.set_vertex_coord(4, -3.5-0.75, 0)
		example_graph.set_vertex_coord(3, -3.5, 0.75)
		example_graph.draw()

		text = TextMobject("Given a conected graph, \\\\determine the property that it\\\\ should have so that you\\\\ can trace a line passing\\\\ through all edges once").shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(text))
		example_graph.show_path([0, 1, 4, 2, 3, 4, 0, 2, 1])
		example_graph.show_path([1, 2, 0, 4, 3, 2, 4, 1, 0], WHITE)
		self.wait(3)

		self.clear()
		
		text = TextMobject("We will paint", "green\\\\", "the vertices with even degree\\\\", "and", "red", "the vertices with odd degree")
		text.set_color_by_tex("green", GREEN)
		text.set_color_by_tex("red", RED_E)

		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		text = TextMobject("Let's see some graphs with such property")

		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		bigger_graph = graph(5, self)
		bigger_graph.set_graph([[1, 2, 4], [0, 2, 4], [0, 1, 3, 4], [2, 4], [0, 1, 2, 3]])
		bigger_graph.set_vertex_coord(0, -2.5*0.5, -5*0.5, RED)
		bigger_graph.set_vertex_coord(1, 2.5*0.5, -5*0.5, RED)
		bigger_graph.set_vertex_coord(2, 2.5*0.5, 0*0.5, GREEN)
		bigger_graph.set_vertex_coord(4, -2.5*0.5, 0, GREEN)
		bigger_graph.set_vertex_coord(3, 0, 2.5*0.5, GREEN)
		bigger_graph.draw()

		text = TextMobject("There are", "3 even", "and", "2 odd").shift(np.array([0, 3, 0]))
		text.set_color_by_tex("3 even", GREEN)
		text.set_color_by_tex("2 odd", RED_E)

		self.play(FadeIn(text))
		self.wait(5)
		self.clear()

		bigger_graph = graph(3, self)
		bigger_graph.set_graph([[1, 2], [0, 2], [1, 2]])
		bigger_graph.set_vertex_coord(0, -1.67, -1.5, GREEN)
		bigger_graph.set_vertex_coord(1, 1.67, -1.5, GREEN)
		bigger_graph.set_vertex_coord(2, 0, 1.5, GREEN)
		bigger_graph.draw()

		text = TextMobject("There are", "3 even", "and", "0 odd").shift(np.array([0, 3, 0]))
		text.set_color_by_tex("3 even", GREEN)
		text.set_color_by_tex("0 odd", RED_E)

		self.play(FadeIn(text))
		self.wait(5)
		self.clear()

		text = TextMobject("And so on. If you continue drawing graphs with such property,\\\\you will notice that the graphs are divided in two groups")

		self.play(FadeIn(text))
		self.wait(8)
		self.play(FadeOut(text))

		text = TextMobject("The ones with no ", "red vertices\\\\", "and the ones with two", "red vertices")
		text.set_color_by_tex("red vertices", RED)

		self.play(FadeIn(text))
		self.wait(8)
		self.play(FadeOut(text))		

		text = TextMobject("We will focus on graphs with no", "red vertices")
		text.set_color_by_tex("red vertices", RED)

		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))

		text = TextMobject("We will prove that the path for theese graphs exist,\\\\ and are all cicles.")

		self.play(FadeIn(text))
		self.wait(8)
		self.play(FadeOut(text))

		