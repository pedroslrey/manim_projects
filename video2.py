from manimlib.imports import *
import numpy as np
import math

class Video(Scene):
	def construct(self):
		pointA = np.array([-4.57, -1.07, 0])
		pointB = np.array([-4.57, 1.07, 0])
		pointC = np.array([-2.43, -1.07, 0])
		pointO = np.array([-3.5, 0, 0])

		circle = Circle(radius=1.5, color=WHITE)
		circle.shift(np.array([-3.5, 0, 0]))

		angle1 = math.radians(0)
		angle2 = math.radians(90)
		quartercircle = Arc(start_angle=angle1, angle=angle2, radius=2.13)
		quartercircle.shift(pointA)

		angle1 = math.radians(0)
		angle2 = math.radians(90)
		paintquartercircle = Arc(start_angle=angle1, angle=angle2, radius=2.13, fill_color=GREEN, fill_opacity=1)
		paintquartercircle.shift(pointA)

		triangle = Polygon(pointA, pointB, pointC, color=GREEN, fill_color=GREEN, fill_opacity=1)
		
		dotA = Dot(pointA)
		dotB = Dot(pointB)
		dotC = Dot(pointC)

		letterA = TexMobject("B")
		letterA.shift(pointA + np.array([-0.25, -0.25, 0]))

		letterB = TexMobject("A")
		letterB.shift(pointB + np.array([-0.25, 0.25, 0]))

		letterC = TexMobject("C")
		letterC.shift(pointC + np.array([0.25, -0.25, 0]))

		lineAB = Line(pointA, pointB)
		lineAC = Line(pointA, pointC)

		text = TextMobject("Given that $\\hat{ABC} = \\measuredangle 90$, \\\\ find the ratio between the \\\\green area and the bigger \\\\circle area (CANADA-2013)")
		text.shift(np.array([3.5, 0, 0]))

		self.play(ShowCreation(circle))
		self.play(ShowCreation(triangle), ShowCreation(quartercircle), ShowCreation(paintquartercircle), ShowCreation(lineAB), ShowCreation(lineAC))
		self.play(ShowCreation(dotA), ShowCreation(dotB), ShowCreation(dotC), FadeIn(letterA) , FadeIn(letterB) , FadeIn(letterC))
		self.wait(2)
		self.play(Write(text))
		self.wait(5)
		self.play(FadeOut(text))
		self.wait(2)

		solution = TextMobject("Solution", color=GREEN)
		solution.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(solution))
		self.wait(3)
		self.play(FadeOut(solution))
		self.wait(2)

		text = TextMobject("Let $O$ be the center of the circle")
		text.shift(np.array([3.5, 3, 0]))

		new_triangle = Polygon(pointA, pointB, pointC, color=None, fill_color=BLACK, fill_opacity=1)

		lineOA = DashedLine(pointA, pointO)
		lineOB = Line(pointB, pointO)
		lineOC = Line(pointC, pointO)

		dotO = Dot(pointO)

		letterO = TexMobject("O")
		letterO.shift(pointO + np.array([0.25, 0.25, 0]))

		self.play(Write(text))
		self.wait(2)
		self.play(FadeOut(triangle), FadeOut(paintquartercircle), FadeIn(dotO), FadeIn(letterO))
		self.wait(1)
		self.play(ShowCreation(lineOA), ShowCreation(lineOB), ShowCreation(lineOC))
		self.wait(3)
		self.play(FadeOut(text))

		angle1 = math.radians(0)
		angle2 = math.radians(45)
		anglearc1 = Arc(start_angle=angle1, angle=angle2, radius=0.3)
		anglearc1.shift(pointA)

		angle1 = math.radians(45)
		angle2 = math.radians(45)
		anglearc2 = Arc(start_angle=angle1, angle=angle2, radius=0.4)
		anglearc2.shift(pointA)

		text2 = TextMobject("Since triangles $AOB$ and $BOC$\\\\ have the same side lenghts,\\\\ they are congruent")
		text2.shift(np.array([3.5, 0, 0]))

		text3 = TextMobject("Then we have that \\\\ $\\hat{ABO} = \\hat{CBO} = \\measuredangle 45$")
		text3.shift(np.array([3.5, 0, 0]))

		text4 = TextMobject("So finally we have that \\\\ $\\hat{COB} = \\hat{AOB} = \\measuredangle 90$, \\\\ which means that $A$, $O$ and $C$ \\\\ are colinear")
		text4.shift(np.array([3.5, 0, 0]))

		text5 = TextMobject("Now, let's get back to \\\\ the problem.")
		text5.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(text2))
		self.wait(6)
		self.play(FadeOut(text2), FadeIn(text3), FadeIn(anglearc1), FadeIn(anglearc2))
		self.wait(6)
		self.play(FadeOut(text3), FadeIn(text4))
		self.wait(6)
		self.play(FadeOut(text4), FadeIn(text5), FadeOut(lineOA), FadeOut(anglearc1), FadeOut(anglearc2))
		self.wait(6)
		self.play(FadeOut(text5))

		text1 = TextMobject("Let $l$ be the radius of \\\\ the quarter circle and $r$ the \\\\ radius of the bigger circle")
		text1.shift(np.array([3.5, 3, 0]))
		
		letterR1 = TexMobject("r")
		letterR1.shift((pointC + pointO)/2 + np.array([0.15, 0.15, 0]))

		letterR2 = TexMobject("r")
		letterR2.shift((pointB + pointO)/2 + np.array([0.15, 0.15, 0]))

		letterL1 = TexMobject("l")
		letterL1.shift((pointA + pointC)/2 + np.array([0, -0.2, 0]))

		letterL2 = TexMobject("l")
		letterL2.shift((pointA + pointB)/2 + np.array([-0.15, 0, 0]))

		text2 = TextMobject("By the Pythagorean theorem, \\\\ we have that")
		text2.shift(np.array([3.5, 3, 0]))

		eq1 = TexMobject("(2r)^2 = l^2 + l^2")
		eq1.shift(np.array([3.5, 0, 0]))

		eq2 = TexMobject("r = \\frac{\\sqrt{2}}{2} l")
		eq2.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(text1), FadeIn(letterR1), FadeIn(letterR2), FadeIn(letterL1), FadeIn(letterL2))
		self.wait(7)
		self.play(FadeOut(text1), FadeIn(text2))
		self.wait(4)
		self.play(FadeIn(eq1))
		self.wait(4)
		self.play(Transform(eq1, eq2))
		self.wait(4)
		self.play(FadeOut(eq1), FadeOut(text2))

		text = TextMobject("Now we will calculate the area \\\\ of the bigger circle, and the area \\\\ of the quarter circle")
		text.shift(np.array([3.5, 3, 0]))

		self.play(Write(text))

		allcirclepaint = Circle(radius=1.5, color=WHITE, fill_color=BLUE, fill_opacity=1)
		allcirclepaint.shift(np.array([-3.5, 0, 0]))

		eq1 = TexMobject("\\text{Circle} = \\pi \\big(\\frac{\\sqrt{2}}{2} l \\big)^2")
		eq1.shift(np.array([3.5, 1, 0]))

		eq1a = TexMobject("\\text{Circle} = \dfrac{1}{2}\\pi l^2")
		eq1a.shift(np.array([3.5, 1, 0]))

		eq2 = TexMobject("\\text{quarter circle} = \dfrac{1}{4}\\pi l^2")
		eq2.shift(np.array([3.5, -1, 0]))

		finaleq = TexMobject("\dfrac{\\text{quarter circle}}{\\text{circle}} = \dfrac{1}{2}")
		finaleq.shift(np.array([3.5, 0, 0]))

		self.remove(dotA, dotB, dotC)
		self.play(Write(eq1), FadeIn(allcirclepaint), FadeIn(dotA), FadeIn(dotB), FadeIn(dotC))
		self.wait(5)
		self.play(Transform(eq1, eq1a))
		self.wait(3)
		self.remove(lineAB, lineAC, dotA, dotB, dotC)
		self.play(Write(eq2), FadeOut(allcirclepaint), FadeIn(triangle), FadeIn(paintquartercircle), FadeIn(lineAB), FadeIn(lineAC), FadeIn(dotA), FadeIn(dotB), FadeIn(dotC))
		self.wait(5)
		self.play(FadeOut(eq1), FadeOut(eq2), FadeIn(finaleq))
		self.wait(5)
		self.clear()
		self.wait(10)
