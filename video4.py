from manimlib.imports import *
import numpy as np
import math
from random import *

class Video(Scene):
	def display_text(self, text, time_in, time_out=0, position=[3.5, 0, 0]):
		dtext = TextMobject(text)
		dtext.shift(np.array(position))

		self.play(FadeIn(dtext))
		self.wait(time_in)
		self.play(FadeOut(dtext))
		self.wait(time_out)

	def construct(self):
		O = np.array([ -3.5, 0, 0])
		A = np.array([ -2.5, 0, 0])
		B = np.array([ -2.5, 1.73, 0])

		circle = Circle(radius=2, color=WHITE)
		circle.shift(O)

		xline = Arrow(np.array([-3.5, -3, 0]), np.array([-3.5, 3, 0]), color=BLUE)
		yline = Arrow(np.array([-6.5, 0, 0]), np.array([-0.5, 0, 0]), color=BLUE)

		line = Line(A, B,)
		fillrectangle = Polygon(
			O, np.array([-3.5, 1.73, 0]),
			B,
			A, color=GREEN, fill_color=GREEN, fill_opacity=2)

		angle1 = math.radians(90)
		angle2 = math.radians(-30)
		fillarc = Arc(radius=2, start_angle=angle1, angle=angle2, color=GREEN, fill_color=GREEN, fill_opacity=1)
		fillarc.shift(O)

		filltriangle = Polygon(
			np.array([-2.55, 1.73, 0]),
			np.array([-3.5, 1.73, 0]),
			np.array([-3.5, 2, 0]),
			color=GREEN, fill_color=GREEN, fill_opacity=1)

		dotA = Dot(A)
		letterA = TexMobject("A")
		letterA.shift(np.array([-2.5, -0.25, 0]))

		dotO = Dot(O)
		letterO = TexMobject("O")
		letterO.shift(np.array([-3.75, -0.25, 0]))

		dotB = Dot(B)
		letterB = TexMobject("B")
		letterB.shift(np.array([-2.25, 1.98, 0]))

		dotC = Dot(np.array([-3.5, 2, 0]))
		letterC = TexMobject("C")
		letterC.shift(np.array([-3.75, 1.75, 0]))

		self.play(ShowCreation(circle))
		self.play(ShowCreation(fillrectangle), ShowCreation(fillarc), ShowCreation(filltriangle), ShowCreation(line))
		self.play(ShowCreation(xline), ShowCreation(yline))
		self.play(FadeIn(dotA), Write(letterA), FadeIn(dotO), Write(letterO), FadeIn(dotB), Write(letterB), FadeIn(dotC), Write(letterC))
		self.wait(3)

		text = TextMobject("Given that the radius of the\\\\ circle is $2$ and $OA = 1$. \\\\Determine the", "green", "area\\\\", "(No calculus allowed)")
		text.shift(np.array([3.5, 0, 0]))
		text.set_color_by_tex("green", GREEN)

		self.play(FadeIn(text))
		self.wait(5)
		self.play(FadeOut(text))
		self.wait(2)

		solution = TextMobject("Solution", color=GREEN)
		solution.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(solution))
		self.wait(3)
		self.play(FadeOut(solution))
		self.wait(2)

		text = TextMobject("Trace the segment $\\overline{OB}$")
		text.shift(np.array([3.5, 0, 0]))

		lineOB = DashedLine(O, B)

		self.play(FadeIn(text))
		self.play(FadeOut(fillarc), FadeOut(filltriangle), FadeOut(fillrectangle), ShowCreation(lineOB))
		self.wait(1)
		self.play(FadeOut(text))
		
		filltriangle2 = Polygon(O, A, B, fill_color=BLUE, fill_opacity=1, color=BLUE)
		
		text = TextMobject("Let $A_1$ be the area \\\\of the blue region")
		text.shift(np.array([3.5, 0, 0]))

		self.mobjects = [filltriangle2] + self.mobjects

		self.play(FadeIn(text), FadeIn(filltriangle2))
		self.wait(6)
		self.play(FadeOut(filltriangle2), FadeOut(text))
		self.wait(2)

		text = TextMobject("And let $A_2$ de the area \\\\ of the red region")
		text.shift(np.array([3.5, 0, 0]))

		angle1 = math.radians(90)
		angle2 = math.radians(-30)
		fillarc2 = Arc(radius=2, start_angle=angle1, angle=angle2, color=RED, fill_color=RED, fill_opacity=1)
		fillarc2.shift(O)

		filltriangle2 = Polygon(
			np.array([-2.55, 1.73, 0]),
			np.array([-3.5, 1.73, 0]),
			np.array([-3.5, 2, 0]),
			color=RED, fill_color=RED, fill_opacity=1)

		filltriangle3 = Polygon(
			O,
			np.array([-3.5, 1.73, 0]),
			B,
			color=RED, fill_color=RED, fill_opacity=1)

		self.mobjects = [filltriangle2, filltriangle3, fillarc2] + self.mobjects

		self.play(FadeIn(text), FadeIn(filltriangle2), FadeIn(fillarc2), FadeIn(filltriangle3))
		self.wait(6)
		self.play(FadeOut(filltriangle2), FadeOut(fillarc2), FadeOut(filltriangle3), FadeOut(text))
		self.wait(2)

		text = "Let $h = AB$. We will\\\\compute $h$"

		self.display_text(text, 5, 3)

		letterh = TexMobject("h").shift((A + B)/2 + np.array([0.25, 0, 0])).scale(0.9)
		letter1 = TexMobject("1").shift((A + O)/2 + np.array([0, -0.25, 0])).scale(0.9)
		letter2 = TexMobject("2").shift((B + O)/2 + np.array([-0.15, 0.15, 0])).scale(0.9)

		self.play(FadeIn(letterh), FadeIn(letter1), FadeIn(letter2))

		text = "By the Pythagorean theorem we\\\\have that $h = \sqrt{2^2 - 1^2} = \sqrt{3}$"

		letterh2 = TexMobject("\sqrt{3}").shift((A + B)/2 + np.array([0.25, 0, 0])).scale(0.8)

		self.display_text(text, 7, 0)
		self.play(Transform(letterh, letterh2))

		text = "Then $A_1 = \\dfrac{\sqrt{3}}{2}$"

		self.display_text(text, 4, 2)

		text = "Now let's calculate $A_2$"

		self.display_text(text, 4, 1)
		
		text = "Notice that \\\\ $\hat{BOA} = \\cos^{-1} 1/2 = \\dfrac{\\pi}{3}$"

		self.display_text(text, 4, 1)

		angle1 = math.radians(90)
		angle2 = math.radians(-30)
		fillarc2 = Arc(radius=2, start_angle=angle1, angle=angle2, color=RED, fill_color=RED, fill_opacity=1)
		fillarc2.shift(O)

		filltriangle2 = Polygon(
			np.array([-2.55, 1.73, 0]),
			np.array([-3.5, 1.73, 0]),
			np.array([-3.5, 2, 0]),
			color=RED, fill_color=RED, fill_opacity=1)

		filltriangle3 = Polygon(
			O,
			np.array([-3.5, 1.73, 0]),
			B,
			color=RED, fill_color=RED, fill_opacity=1)

		self.mobjects = [filltriangle2, filltriangle3, fillarc2] + self.mobjects

		self.play(FadeIn(filltriangle2), FadeIn(fillarc2), FadeIn(filltriangle3))

		text = "Then the red arc angle is $\\dfrac{\\pi}{6}$"

		self.display_text(text, 4, 1)

		text = "Thus $A_2 = \\pi 2^2 \\dfrac{1}{12} = \\dfrac{\\pi}{3}$"

		self.display_text(text, 6, 1)

		filltriangle2 = Polygon(O, A, B, fill_color=BLUE, fill_opacity=1, color=BLUE)

		self.mobjects = [filltriangle2] + self.mobjects

		self.play(FadeIn(filltriangle2))

		text = "Finally, the total area is \\\\$\\dfrac{\sqrt{3}}{2} + \\dfrac{\\pi}{3}$"

		self.display_text(text, 6, 1)

		self.clear()

		self.wait(10)

