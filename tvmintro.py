from manimlib.imports import *
import numpy as np
import math

class Intro(Scene):
	def construct(self):
		background = Rectangle(
			width = FRAME_WIDTH,
			height = FRAME_HEIGHT,
			stroke_width = 0,
			fill_color = WHITE,
			fill_opacity = 1)
		self.add(background)
		tvm = TextMobject("\\usefont{T1}{fco}{m}{n}TVM", color = BLACK).scale(4)
		under_tvm = TextMobject("\\usefont{T1}{fco}{m}{n}Matemática, Física e Computação", color = BLACK).next_to(tvm, DOWN)
		self.play(FadeInFrom(tvm, RIGHT), FadeInFrom(under_tvm, LEFT))
		self.wait(4)
		self.play(FadeOut(tvm), FadeOut(under_tvm))