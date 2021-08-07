from manimlib.imports import *
import numpy as np
import math

class Video(Scene):
	def construct(self):
		text = TextMobject('Olá, recentementte criei um\\\\ outro canal de matemática chamado "My math Notes"\\\\ de animações matemáticas')
		self.play(FadeIn(text))
		self.wait(7)
		self.play(FadeOut(text))
		text = TextMobject("Como estas").shift([3.5, 0, 0])
		self.play(FadeIn(text))

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

		self.play(ShowCreation(circle))
		self.play(ShowCreation(triangle), ShowCreation(quartercircle), ShowCreation(paintquartercircle), ShowCreation(lineAB), ShowCreation(lineAC))
		self.play(ShowCreation(dotA), ShowCreation(dotB), ShowCreation(dotC), FadeIn(letterA) , FadeIn(letterB) , FadeIn(letterC))
		self.wait(2)

		self.clear()
		self.add(text)

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

		self.play(ShowCreation(square))
		self.play(ShowCreation(dotA), Write(letterA), ShowCreation(dotB), Write(letterB), ShowCreation(dotC), Write(letterC), ShowCreation(dotD), Write(letterD))
		self.play(ShowCreation(semicircle1), ShowCreation(semicircle2), ShowCreation(quartercircle))
		self.play(Write(a), Write(b))
		self.wait(2)


		self.clear()

		text = TextMobject("Se inscrevam!\\\\Obrigado").to_edge(UP)

		self.play(FadeIn(text))
		self.wait(10)