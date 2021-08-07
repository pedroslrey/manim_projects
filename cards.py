from manimlib.imports import *
import numpy as np
import math
from collections import defaultdict

card1a = Polygon(
		np.array([-6, -1.5, 0]),
		np.array([-4, -1.5, 0]),
		np.array([-4, 1.5, 0]),
		np.array([-6, 1.5, 0]), color=WHITE, fill_color=GREEN, fill_opacity=1)
card2a = Polygon(
		np.array([-3, -1.5, 0]),
		np.array([-1, -1.5, 0]),
		np.array([-1, 1.5, 0]),
		np.array([-3, 1.5, 0]), color=WHITE, fill_color=GREEN, fill_opacity=1)
card3a = Polygon(
		np.array([0, -1.5, 0]),
		np.array([2, -1.5, 0]),
		np.array([2, 1.5, 0]),
		np.array([0, 1.5, 0]), color=WHITE, fill_color=GREEN, fill_opacity=1)
card4a = Polygon(
		np.array([3, -1.5, 0]),
		np.array([5, -1.5, 0]),
		np.array([5, 1.5, 0]),
		np.array([3, 1.5, 0]), color=WHITE, fill_color=GREEN, fill_opacity=1)

card1b = Polygon(
		np.array([-6, -1.5, 0]),
		np.array([-4, -1.5, 0]),
		np.array([-4, 1.5, 0]),
		np.array([-6, 1.5, 0]), color=WHITE, fill_color=BLUE, fill_opacity=1)
card2b = Polygon(
		np.array([-3, -1.5, 0]),
		np.array([-1, -1.5, 0]),
		np.array([-1, 1.5, 0]),
		np.array([-3, 1.5, 0]), color=WHITE, fill_color=BLUE, fill_opacity=1)
card3b = Polygon(
		np.array([0, -1.5, 0]),
		np.array([2, -1.5, 0]),
		np.array([2, 1.5, 0]),
		np.array([0, 1.5, 0]), color=WHITE, fill_color=BLUE, fill_opacity=1)
card4b = Polygon(
		np.array([3, -1.5, 0]),
		np.array([5, -1.5, 0]),
		np.array([5, 1.5, 0]),
		np.array([3, 1.5, 0]), color=WHITE, fill_color=BLUE, fill_opacity=1)

states = [0, 1, 0, 1]


class Cards(Scene):
	up_text = -1

	def update_it(self):
		self.remove(card1a, card1b, card2a, card2b, card3a, card3b, card4a, card4b)
		if states[0] == 1:
			self.add(card1a)
		else:
			self.add(card1b)
		if states[1] == 1:
			self.add(card2a)
		else:
			self.add(card2b)
		if states[2] == 1:
			self.add(card3a)
		else:
			self.add(card3b)
		if states[3] == 1:
			self.add(card4a)
		else:
			self.add(card4b)

	def S(self, num):
		x = 0
		for i in range(4):
			if (states[i] != 0): x = -1
		if (x == 0): return
		if (num == 0): return
		self.S(num-1)
		states[num-1] = not states[num-1]
		self.remove(self.up_text)
		newtext = TexMobject(str(num)).shift(np.array([0, 3, 0]))
		self.add(newtext)
		self.up_text = newtext

		self.update_it()
		self.wait(1)
		self.S(num-1)

	def construct(self):
		self.play(
			ShowCreation(card1a),
			ShowCreation(card2a), 
			ShowCreation(card3a), 
			ShowCreation(card4a))

		self.up_text = TexMobject("1").shift(np.array([0, 3, 0]))

		text = TextMobject("If a card is blue, than it is facing down\\\\ and if it is  green then it is facing up").scale(0.75).shift(np.array([0, -2, 0]));
		self.play(Write(text))
		self.wait(6)
		self.play(FadeOut(text))

		text = TextMobject("Let us consider a random state for the sequence").shift(np.array([0, -2.5, 0]))

		self.play(Write(text))
		self.wait(3)

		self.update_it()
		self.wait(1)

		self.S(4)

		self.wait(3)