from manimlib.imports import *
import numpy as np
import math

class Video(Scene):
	def construct(self):
		angle1 = math.radians(-90)
		angle2 = math.radians(180)
		semicircle1 = Arc(start_angle=angle1, angle=angle2, radius=1.5)
		semicircle1.shift(np.array([-5, 0, 0]))

		angle1 = math.radians(0)
		angle2 = math.radians(180)
		semicircle2 = Arc(start_angle=angle1, angle=angle2, radius=1.5)
		semicircle2.shift(np.array([-3.5, -1.5, 0]))

		angle1 = math.radians(0)
		angle2 = math.radians(90)
		quartercircle = Arc(start_angle=angle1, angle=angle2, radius=3)
		quartercircle.shift(np.array([-5, -1.5, 0]))

		a = TexMobject("a")
		a.shift(np.array([-4.25, -0.75, 0]))

		b = TexMobject("b")
		b.shift(np.array([-3.2, 0.41, 0]))

		square = Polygon(
			np.array([-5, -1.5, 0]),
			np.array([-2, -1.5, 0]),
			np.array([-2, 1.5, 0]),
			np.array([-5, 1.5, 0]), color=WHITE)

		dotA = Dot(np.array([-5, -1.5, 0]))
		letterA = TexMobject("A")
		letterA.shift(np.array([-5.25, -1.75, 0]))

		dotB = Dot(np.array([-2, -1.5, 0]))
		letterB = TexMobject("B")
		letterB.shift(np.array([-1.75, -1.75, 0]))
		
		dotC = Dot(np.array([-2, 1.5, 0]))
		letterC = TexMobject("C")
		letterC.shift(np.array([-1.75, 1.75, 0]))

		dotD = Dot(np.array([-5, 1.5, 0]))
		letterD = TexMobject("D")
		letterD.shift(np.array([-5.25, 1.75, 0]))

		text = TextMobject("Given that $ABCD$ is a square, \\\\find the ratio between the areas \\\\ $a$ and $b$")
		text.shift(np.array([3.5, 0, 0]))

		self.play(ShowCreation(square))
		self.play(ShowCreation(dotA), Write(letterA), ShowCreation(dotB), Write(letterB), ShowCreation(dotC), Write(letterC), ShowCreation(dotD), Write(letterD))
		self.play(ShowCreation(semicircle1), ShowCreation(semicircle2), ShowCreation(quartercircle))
		self.play(Write(a), Write(b))
		self.wait(2)
		self.play(Write(text))
		self.wait(4)
		self.play(FadeOut(text))
		self.wait(2)

		solution = TextMobject("Solution", color=GREEN)
		solution.shift(np.array([3.5, 0, 0]))

		self.play(FadeIn(solution))
		self.wait(3)
		self.play(FadeOut(solution))
		self.wait(2)

		text = TextMobject("Let $c$ be the area of the \\\\ following regions, and let $l$ \\\\ be the side of the square")
		text.shift(np.array([3.5, 0, 0]))

		c1 = TexMobject("c")
		c1.shift(np.array([-2.95, -0.75, 0]))

		c2 = TexMobject("c")
		c2.shift(np.array([-4.45, 0.65, 0]))

		self.play(Write(text), Write(c1), Write(c2))
		self.wait(5)
		self.play(FadeOut(text))

		text = TextMobject("Notice the following equations")
		text.shift(np.array([3.5, 3, 0]))

		eq1 = TexMobject("a + c = \\frac{1}{2}\\pi(l/2)^2")
		eq1.shift(np.array([3.5, 2, 0]))

		eq2 = TexMobject("a + 2c + b = \\frac{1}{4}\\pi l^2")
		eq2.shift(np.array([3.5, 1, 0]))

		eq1l = TexMobject("a + c = \\pi l^2/8")
		eq1l.shift(np.array([3.5, 2, 0]))

		eq2l = TexMobject("a + 2c + b = \\pi l^2/4")
		eq2l.shift(np.array([3.5, 1, 0]))

		eq1ll = TexMobject("2a + 2c = \\pi l^2/4")
		eq1ll.shift(np.array([3.5, 2, 0]))

		line = Line(np.array([1, 0.5, 0]), np.array([6, 0.5, 0]))

		minus = TexMobject("-")
		minus.shift(np.array([1, 1.5, 0]))

		eq3 = TexMobject("a - b = 0")
		eq3.shift(np.array([3.5, 0, 0]))

		final = TexMobject("\dfrac{a}{b} = 1")
		final.shift(np.array([3.5, 0, 0]))

		finaltext = TextMobject("Finally, we have that the\\\\ ratio between $a$ and $b$ is 1!")
		finaltext.next_to(final, DOWN)

		self.play(Write(text))
		self.wait(3)
		self.play(FadeIn(eq1), FadeIn(eq2))
		self.wait(7)
		self.play(Transform(eq1, eq1l), Transform(eq2, eq2l))
		self.wait(3)
		self.play(Transform(eq1, eq1ll))
		self.wait(3)
		self.play(ShowCreation(line), FadeIn(minus))
		self.wait(3)
		self.play(Write(eq3))
		self.wait(4)
		self.play(Transform(eq3, final), FadeIn(finaltext), FadeOut(text), FadeOut(eq1), FadeOut(eq2), FadeOut(line), FadeOut(minus))
		self.wait(5)
		self.clear()
		self.wait(5)

