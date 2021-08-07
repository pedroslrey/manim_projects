from manimlib.imports import *
import numpy as np
import math
from random import *

class Video(Scene):
	def construct(self):
		hoop = Circle(radius=0.25, fill_color=GREEN, fill_opacity=1, color=GREEN)
		hoop.shift(np.array([-3.5, 0, 0]))
		for i in range(-7, 1):
			line = Line(np.array([i, -5, 0]), np.array([i, 6, 0]), color=WHITE)
			self.add(line)
		for i in range(-4, 5):
			line = Line(np.array([-7, i, 0]), np.array([0, i, 0]), color=BLUE)
			self.add(line)

		text = TextMobject("A hoop of diameter $d$ is thrown \\\\ on to an infinitely large \\\\ chessboard with squares of side \\\\ $L$, where $d < L$. What is the \\\\ chance of the hoop being \\\\ between two squares?\\\\ (Professor Povey's \\\\Perplexing Problems)")
		text.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(hoop), Write(text))
		self.wait(3)
		for i in range(3):
			x = randint(-70, 0)
			y = randint(-40, 50)
			hoop2 = Circle(radius=0.25, fill_color=GREEN, fill_opacity=1, color=GREEN)
			hoop2.shift(np.array([x/10, y/10, 0]))
			self.play(FadeOut(hoop), FadeIn(hoop2))
			self.wait(2)
			hoop = hoop2

		solution = TextMobject("Solution", color=GREEN)
		solution.shift(np.array([3.5, 0, 0]))

		self.play(FadeOut(text))
		self.play(FadeIn(solution))
		self.wait(3)
		self.play(FadeOut(solution))
		self.wait(2)
		self.clear()

		text = TextMobject("Suppose that the hoop have \\\\ fallen over the square $ABCD$.\\\\ Let's analize what should\\\\ happen so that the hoop \\\\is totaly inside the square")
		text.shift(np.array([3.5, 0, 0]))

		square = Polygon(
			np.array([-5, -1.5, 0]),
			np.array([-2, -1.5, 0]),
			np.array([-2, 1.5, 0]),
			np.array([-5, 1.5, 0]), color=WHITE)

		dotA = Dot(np.array([-5, -1.5, 0]))
		dotB = Dot(np.array([-2, -1.5, 0]))
		dotC = Dot(np.array([-2, 1.5, 0]))
		dotD = Dot(np.array([-5, 1.5, 0]))

		letterA = TexMobject("A")
		letterA.shift(np.array([-5, -1.5, 0]) + np.array([-0.25, -0.25, 0]))
		letterB = TexMobject("B")
		letterB.shift(np.array([-2, -1.5, 0]) + np.array([0.25, -0.25, 0]))
		letterC = TexMobject("C")
		letterC.shift(np.array([-2, 1.5, 0]) + np.array([0.25, 0.25, 0]))
		letterD = TexMobject("D")
		letterD.shift(np.array([-5, 1.5, 0]) + np.array([-0.25, 0.25, 0]))

		self.play(FadeIn(text), FadeIn(square), FadeIn(dotA), FadeIn(dotB), FadeIn(dotC), FadeIn(dotD), FadeIn(letterA), FadeIn(letterB), FadeIn(letterC), FadeIn(letterD))
		self.wait(5)
		self.play(FadeOut(text))

		text2 = TextMobject("If the hoop is totally inside \\\\ the square, its center falls\\\\ inside inside the green \\\\square")
		text2.shift(np.array([3.5, 0, 0]))

		smallsquare = Polygon(
			np.array([-4, -0.5, 0]),
			np.array([-3, -0.5, 0]),
			np.array([-3, 0.5, 0]),
			np.array([-4, 0.5, 0]), color=WHITE, fill_color=GREEN, fill_opacity=1)
		circle1 = Circle(radius=1)
		circle1.shift(np.array([-4, -0.5, 0]))

		circle2 = Circle(radius=1)
		circle2.shift(np.array([-3, -0.5, 0]))

		circle3 = Circle(radius=1)
		circle3.shift(np.array([-3, 0.5, 0]))

		circle4 = Circle(radius=1)
		circle4.shift(np.array([-4, 0.5, 0]))

		line1 = DashedLine(np.array([-4, 0, 0]), np.array([-5, 0, 0]))
		arrow = CurvedArrow(start_point=np.array([-4.5, 0, 0]), end_point=np.array([-5.5, 0, 0]))
		eq1 = TexMobject("d/2")
		eq1.shift(np.array([-5.5, -0.5, 0]))

		self.wait(1)
		self.play(FadeIn(text2), FadeIn(smallsquare))
		self.play(FadeInFrom(circle1, LEFT+DOWN), FadeInFrom(circle2, RIGHT+DOWN), FadeInFrom(circle3, RIGHT + UP), FadeInFrom(circle4, LEFT+UP))
		self.play(FadeIn(line1), ShowCreation(arrow), FadeIn(eq1))
		self.wait(6)
		self.play(FadeOut(text2))

		text3 = TextMobject("Then the chace of the hoop\\\\ being between two squares is \\\\the ratio between the area \\\\of $ABCD$ and the black region")
		text3.shift(np.array([3.5, 2.5, 0]))

		eq2 = TexMobject("P = \\dfrac{L^2 - (L-d)^2}{L^2}")
		eq2.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(text3))
		self.wait(5)
		self.play(FadeIn(eq2))
		self.wait(5)

		self.clear()
		for i in range(-7, 1):
			line = Line(np.array([i, -5, 0]), np.array([i, 6, 0]), color=WHITE)
			self.add(line)
		for i in range(-4, 5):
			line = Line(np.array([-7, i, 0]), np.array([0, i, 0]), color=BLUE)
			self.add(line)

		text = TextMobject("To test our formula,\\\\ let's make some \\\\simulations for $L = 1$ and \\\\ $d = 0.5$")
		text.shift(np.array([3.5, 0, 0]))

		total = 0
		outsquare = 0
		statustext = TextMobject("total = $0$\\\\ hoops between two squares = $0$")
		statustext.shift(np.array([3.5, 3, 0]))

		self.play(FadeIn(text), FadeIn(statustext))
		for i in range(50):
			total += 1
			x = randint(-70, 0)
			y = randint(-40, 50)

			downx = x%10
			downy = y%10

			if (not (downx > 2 and downx < 8 and downy > 2 and downy < 8)): outsquare += 1

			hoop2 = Circle(radius=0.25, fill_color=GREEN, fill_opacity=1, color=GREEN)
			hoop2.shift(np.array([x/10, y/10, 0]))

			newstatustext = TextMobject("total = $" + str(total) + "$\\\\ hoops between two sqares = $" + str(outsquare) + "$")
			newstatustext.shift(np.array([3.5, 3, 0]))
			self.add(hoop2)
			self.remove(hoop)
			self.remove(statustext)
			self.add(newstatustext)
			self.wait(0.3)
			hoop = hoop2
			statustext = newstatustext
		self.wait(3)
		self.play(FadeOut(text), FadeOut(statustext))
		self.wait(1)

		text = TextMobject("Then we have an aproximation\\\\ for the chance of the hoop \\\\falling between two sqaures,\\\\ which is $\\frac{38}{50} \\approx \\frac{3}{4}$")
		text.shift(np.array([3.5, 0, 0]))
		text2 = TextMobject("And $\\frac{3}{4}$ is the value that \\\\our formula give us!")
		text2.next_to(text, DOWN)

		self.play(FadeIn(text))
		self.wait(6)
		self.play(FadeIn(text2))
		self.wait(6)
		self.clear()
		self.wait(10)