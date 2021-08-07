from manimlib.imports import *
import numpy as np
import math

city_map = [
	"................................."
	".#######..#######..######..#####.",
	".#######..#######..######..#####.",
	".................................",
	".######...@@@@.....@@@@..#####.#.",
	".#....#....@.@.....@.@...#...#.#.",
	".######....@@@@@@@@@@@...#####.#.",
	"................................."
]

def coord(x, y):
	return np.array([x*14/8 - 7, y*8/33 - 4, 0])

class Video(Scene):
	people = []
	original = []

	def construct(self):
		square = Polygon(
			coord(0, 0),
			coord(0, 33),
			coord(8, 33),
			coord(8, 0),
			color=WHITE, fill_color = WHITE, fill_opacity = 1)

		self.add(square)
		self.wait(3)
		p = 0
		
		for i in range(7):
			for j in range(32):
				if city_map[i][j] == '#':
					square = Polygon(
						coord(i, j),
						coord(i + 1, j),
						coord(i + 1, j + 1),
						coord(i, j + 1), color = BLUE_E, fill_color=BLUE_E, fill_opacity=1)
					self.add(square)
					p += 1
					circ = Circle(radius=0.1, color = LIGHT_BROWN, fill_color = LIGHT_BROWN, fill_opacity = 1).shift(coord(i + 0.5, j + 0.5))
					self.add(circ)
					self.people.append(circ)
					self.original.append(coord(i + 0.5, j + 0.5))
					
				elif city_map[i][j] == '@':
					square = Polygon(
						coord(i, j),
						coord(i + 1, j),
						coord(i + 1, j + 1),
						coord(i, j + 1), color = RED_A, fill_color=RED_A, fill_opacity=1)
					self.add(square)

		while (1):
			paths = [[] for i in range(p)]
			try:
				x, y = [int(k) for k in input().split()]
			except EOFError:
				break

			operations = []

			paths[0].append((x, y))
			maxi = 0
			for i in range(p):
				c = 0
				while (1):
					x, y = [int(k) for k in input().split()]
					if x == -1: break;
					paths[i].append((x, y))
					c += 1
					maxi = max(maxi, c)
			
			for op in range(maxi, 1, -1):
				for i in range(p):
					if (len(paths[i]) <= op): continue
					c = coord(*paths[i][op])
					path = VMobject()
					path.set_points_as_corners([c, coord(*paths[i][op - 1])])
					operations.append(MoveAlongPath(self.people[i], path))

				self.play(*operations)
				self.wait(1)

			for i in range(p):
				x, y = [int(k) for k in input().split()]
				if (x != 0): self.people[i] = Circle(radius=0.1, color = GREEN_D, fill_color = GREEN_D, fill_opacity = 1).shift(self.original[i])
				else: self.people[i] = Circle(radius=0.1, color = LIGHT_BROWN, fill_color = LIGHT_BROWN, fill_opacity = 1).shift(self.original[i])