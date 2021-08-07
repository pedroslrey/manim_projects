from manim import *
import numpy as np
import math
from random import *
from datetime import datetime

class BallsScene(Scene):
	def construct(self):
		seed(123)
		n_rows = 7
		positions = [[] for i in range(n_rows)]

		positions[0] = [np.array([0, 3, 0])]

		for i in range(1, n_rows):
			for j in range(i):
				positions[i].append(positions[i-1][j] + np.array([-0.4, -0.4, 0]))
			positions[i].append(positions[i-1][-1] + np.array([0.4, -0.4, 0]))

		for xs in positions:
			for x in xs:
				circle1 = Circle(radius = 0.05, color=WHITE, fill_color = WHITE, fill_opacity = 1).shift(x)
				self.add(circle1)
				#print(x, end = ' ')
			#print()

		num_balls = 2**6
		balls = [
			Circle(radius = 0.03, color="#ff0000", fill_color = "#ff0000", fill_opacity = 1).shift(np.array([0, 3, 0]))
			for i in range(num_balls)]

		there = [0 for i in range(n_rows)]

		xs = [[np.array([0, 3.5, 0])] for i in range(num_balls)]
		finals = []
		for z in range(num_balls):
			j = 0
			xs[z].append(np.array([0, 3, 0]))
			for i in range(1, n_rows):
				if randint(0, 1) == 0:
					j += 1
				xs[z].append(positions[i][j])
			finals.append(j)
			xs[z].append(xs[z][-1] + np.array([0, -3.7, 0] + there[j]*np.array([0, 0.1, 0])))
			there[j] += 1

		paths = [VMobject() for i in range(num_balls)]
		for i in range(num_balls):
			paths[i].set_points_as_corners(xs[i])

		self.wait(4)
		self.play(*[AnimationGroup(
			Animation(Mobject(), run_time=i*0.3),
			MoveAlongPath(balls[i], paths[i]),
			lag_ratio=1
		) for i in range(num_balls)])
		self.wait(2)
		self.play(*[FadeOut(b) for b in balls])

class PascalTriangle(Scene):
	def construct(self):
		n_rows = 7
		pos = [[] for i in range(n_rows)]
		dots = [[] for i in range(n_rows)]
		new_pos = [[] for i in range(n_rows)]

		pos[0] = [np.array([0, 3, 0])]
		new_pos[0] = [np.array([0, 1.5, 0])]

		for i in range(1, n_rows):
			for j in range(i):
				pos[i].append(pos[i-1][j] + np.array([-0.4, -0.4, 0]))
				new_pos[i].append(new_pos[i-1][j] + np.array([-0.5, -0.5, 0]))
			pos[i].append(pos[i-1][-1] + np.array([0.4, -0.4, 0]))
			new_pos[i].append(new_pos[i-1][-1] + np.array([0.5, -0.5, 0]))

		for i in range(n_rows):
			for x in pos[i]:
				circle1 = Circle(radius = 0.05, color=WHITE, fill_color = WHITE, fill_opacity = 1).shift(x)
				self.add(circle1)
				dots[i].append(circle1)

		anims = []
		for i in range(n_rows):
			for j in range(i + 1):
				path = VMobject()
				path.set_points_smoothly([pos[i][j], new_pos[i][j]])
				anims.append(MoveAlongPath(dots[i][j], path))

		self.play(*anims)
		self.wait(5)

		pascal = [[] for i in range(n_rows)]
		pascal[0] = [1]

		for i in range(1, n_rows):
			pascal[i].append(1)
			for j in range(1, i):
				pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
			pascal[i].append(1)

		val = [[] for i in range(n_rows)]
		for i in range(n_rows):
			for j in range(i+1):
				val[i].append(i//2 - int(abs(i/2 - j)))
			#print(val[i])

		anims = []
		timing = [0, 6, 8, 8.5, 9, 9.25, 9.35]
		cs = ["#77c957", "#57c99d", "#42c2f5", "#5742f5"]
		for i in range(n_rows):
			for j in range(i + 1):
				text = MathText(str(pascal[i][j]), color=cs[val[i][j]]).scale(0.75)
				text.shift(new_pos[i][j])
				anims.append(AnimationGroup(
					Animation(Mobject(), run_time=timing[i]),
					Transform(dots[i][j], text),
					lag_ratio=1))

		self.play(*anims)
		self.wait(5)

		arc1 = Arrow(new_pos[5][2], new_pos[4][1])
		arc2 = Arrow(new_pos[5][2], new_pos[4][2])

		self.play(ShowCreation(arc1), ShowCreation(arc2))
		self.wait(7)

		text = TextMobject("Triângulo de Pascal", color=YELLOW).shift(np.array([0, 3.5, 0]))
		self.play(Write(text))
		self.wait(4)

class BinomAnimation(Scene):
	def construct(self):
		pos = [np.array([-2.5, 0, 0]) + i*np.array([0.5, 0, 0]) for i in range(10)]
		objs = [MathText(str(i + 1)).shift(pos[i]) for i in range(10)]

		rects_pos = [(np.array([-1.875, 2, 0]) + i*np.array([1.25, 0, 0])) for i in range(3)]
		cs = ["#1b9419", "#1339c2", "#eb0e24"]
		rects = [Rectangle(height = 1, width=0.75, color=cs[i]).shift(rects_pos[i]) for i in range(3)]

		dots = [MathText("\\cdot").shift((rects_pos[i] + rects_pos[i-1])/2 + np.array([0, 0.9, 0])).scale(0.75)
			    for i in range(1, 3)]
		self.add(*objs)
		self.play(*[ShowCreation(r) for r in rects])
		self.play(*[Write(d) for d in dots])
		self.wait(20)

		rs = [2, 1, 6]
		texts = ["10", "9", "8"]
		ts = [3, 3, 3]
		for k in range(3):
			paths = []
			for i in range(10):
				path = VMobject()
				path.set_points_smoothly([pos[i], rects_pos[k], pos[i]])
				if i not in rs[0:k]: paths.append(path)
				else: paths.append(None)

			self.play(*[AnimationGroup(
				Animation(Mobject(), run_time=0.5*i),
				MoveAlongPath(objs[i], paths[i]),  lag_ratio=1) for i in range(10) if paths[i] != None])
			#self.wait(1)

			text = MathText(texts[k]).shift(rects_pos[k] + np.array([0, 0.9, 0])).scale(0.75)
			self.play(Write(text))
			path = VMobject()
			path.set_points_smoothly([pos[rs[k]], rects_pos[k]])
			self.play(MoveAlongPath(objs[rs[k]], path))
			self.wait(3.5)

		self.wait(9.5)
		total_t = TextMobject("Número de formas: ", color = YELLOW).shift(np.array([4, 2.5, 0]))
		self.play(Write(total_t))
		self.wait(1)

		text0 = MathText("n\\times (n-1) \\times \\cdots \\times (n - k + 1) ").next_to(total_t, DOWN).scale(0.75)
		self.play(Write(text0))
		self.wait(3)

		text1 = MathText("\\frac{n!}{(n-k)!}").next_to(total_t, DOWN)
		self.play(Transform(text0, text1))
		self.wait(11)

		text2 = MathText("\\frac{n!}{(n-k)!k!}").next_to(total_t, DOWN)
		self.play(Transform(text0, text2))
		self.wait(3)

		text3 = MathText("\\binom{n}{k} = \\frac{n!}{(n-k)!k!}").next_to(total_t, DOWN)
		self.play(Transform(text0, text3))
		self.wait(3)

class CalcPascal(Scene):
	def construct(self):
		n_rows = 7
		pos = [[] for i in range(n_rows)]
		new_pos = [[] for i in range(n_rows)]

		pos[0] = [np.array([0, 1.5, 0])]
		new_pos[0] = [np.array([-3.5, 1.5, 0])]

		for i in range(1, n_rows):
			for j in range(i):
				pos[i].append(pos[i-1][j] + np.array([-0.5, -0.5, 0]))
				new_pos[i].append(new_pos[i-1][j] + np.array([0, -0.5, 0]))
			pos[i].append(pos[i-1][-1] + np.array([0.5, -0.5, 0]))
			new_pos[i].append(new_pos[i][-1] + np.array([0.75, 0, 0]))

		pascal = [[] for i in range(n_rows)]
		pascal[0] = [1]

		for i in range(1, n_rows):
			pascal[i].append(1)
			for j in range(1, i):
				pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
			pascal[i].append(1)

		val = [[] for i in range(n_rows)]
		for i in range(n_rows):
			for j in range(i+1):
				val[i].append(i//2 - int(abs(i/2 - j)))
			#print(val[i])

		texts = [[] for i in range(n_rows)]
		cs = ["#77c957", "#57c99d", "#42c2f5", "#5742f5"]
		for i in range(n_rows):
			for j in range(i + 1):
				text = MathText(str(pascal[i][j]), color = cs[val[i][j]]).shift(pos[i][j])
				texts[i].append(text)
				self.add(text)

		self.wait(3)

		anims = []
		for i in range(n_rows):
			for j in range(i + 1):
				path = VMobject()
				path.set_points_as_corners([pos[i][j], new_pos[i][j]])
				anims.append(MoveAlongPath(texts[i][j], path))

		self.play(*anims)
		self.wait(3)

		dots = [[] for i in range(n_rows)]
		for i in range(n_rows):
			for x in new_pos[i]:
				circle1 = Circle(radius = 0.05, color=WHITE, fill_color = WHITE, fill_opacity = 1).shift(x)
				dots[i].append(circle1)

		anims = []
		for i in range(n_rows):
			for j in range(i + 1):
				anims.append(Transform(texts[i][j], dots[i][j]))

		self.play(*anims)
		line_nums = [MathText(str(i + 1)).shift(new_pos[i][0] + np.array([-0.5, 0, 0])).scale(0.75) for i in range(n_rows)]
		col_nums = [MathText(str(i + 1)).shift(new_pos[-1][i] + np.array([0, -0.5, 0])).scale(0.75) for i in range(n_rows)]

		self.play(*[Write(l) for l in line_nums], *[Write(c) for c in col_nums])
		self.wait(15)

		dots[6][2].set_color("#ff0000")
		self.play(Transform(texts[6][2], dots[6][2]))

		def show_arrows(seq):
			arrows = []
			for i in range(n_rows - 1):
				arrow = Arrow(dots[seq[i][0]][seq[i][1]], dots[seq[i + 1][0]][seq[i + 1][1]], color="#ff0000")
				arrows.append(arrow)
				self.play(ShowCreation(arrow))
			self.play(*[FadeOut(a) for a in arrows])

		def show_arrows2(seq):
			arrows = []
			for i in range(n_rows - 1):
				arrow = Arrow(dots[seq[i][0]][seq[i][1]], dots[seq[i + 1][0]][seq[i + 1][1]], color="#ff0000")
				arrows.append(arrow)
			self.play(*[ShowCreation(a) for a in arrows])
			return arrows

		def calc_arrows(seq):
			arrows = []
			for i in range(n_rows - 1):
				arrow = Arrow(dots[seq[i][0]][seq[i][1]], dots[seq[i + 1][0]][seq[i + 1][1]], color="#ff0000")
				arrows.append(arrow)
			return arrows

		seq = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2)]
		show_arrows(seq)

		seq = [(0, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2)]
		show_arrows(seq)

		angle90 = math.radians(-90)
		angle45 = math.radians(45)
		r_arrows = [Arrow(color="#ff0000").shift(np.array([3.5, 1.5, 0]) + i*np.array([0, -0.5, 0])).scale(0.3).rotate(angle90) for i in range(n_rows - 1)]
		self.play(*[ShowCreation(a) for a in r_arrows])
		self.wait(3)

		arrows = show_arrows2([(i, 0) for i in range(n_rows)])
		marc = [0 for i in range(n_rows)]

		chs = [(3, 1), (5, 1), (3, 0)]
		for i in range(3):
			marc[chs[i][0]] = chs[i][1]
			xs = []
			s = 0
			for j in range(n_rows):
				xs.append((j, s))
				s += marc[j]
			arrows2 = calc_arrows(xs)
			self.play(Rotate(r_arrows[chs[i][0]], (angle45 if chs[i][1] else -angle45)), *[Transform(arrows[j], arrows2[j]) for j in range(n_rows - 1)])
			self.wait(0.5)

		text = TextMobject("terceiro pino da sétima linha").shift(np.array([-1, 3, 0]))
		binom = MathText("= \\binom{6}{2}").next_to(text, RIGHT)

		self.play(Write(text))
		self.wait(3)
		self.play(Write(binom))
		self.wait(6)

		text2 = TextMobject("$i$-ésimo pino da $j$-ésima linha").shift(np.array([-1, 3, 0]))
		binom2 = MathText("= \\binom{j-1}{i-1}").next_to(text2, RIGHT)

		self.play(Transform(text, text2), Transform(binom, binom2))
		self.wait(6)

		line_nums2 = [MathText(str(i)).shift(new_pos[i][0] + np.array([-0.5, 0, 0])).scale(0.75) for i in range(n_rows)]
		col_nums2 = [MathText(str(i)).shift(new_pos[-1][i] + np.array([0, -0.5, 0])).scale(0.75) for i in range(n_rows)]

		self.play(*[Transform(line_nums[i], line_nums2[i]) for i in range(n_rows)],
				  *[Transform(col_nums[i], col_nums2[i]) for i in range(n_rows)])
		self.wait(3)

		binom4 = MathText("= \\binom{j}{i}").next_to(text2, RIGHT)
		self.play(Transform(binom, binom4))
		self.wait(6)

		self.play(*[FadeOut(a) for a in r_arrows], *[FadeOut(a) for a in arrows])
		n_texts = [[] for i in range(n_rows)]
		cs = ["#77c957", "#57c99d", "#42c2f5", "#5742f5"]
		for i in range(n_rows):
			for j in range(i + 1):
				text1 = MathText(str(pascal[i][j]), color = cs[val[i][j]]).shift(pos[i][j])
				n_texts[i].append(text1)
				#self.add(text)

		self.play(*[FadeOut(c) for c in col_nums], *[FadeOut(c) for c in line_nums])

		anims = []
		for i in range(n_rows):
			for j in range(i + 1):
				path = VMobject()
				path.set_points_as_corners([new_pos[i][j], pos[i][j]])
				anims.append(MoveAlongPath(texts[i][j], path))
				anims.append(Transform(texts[i][j], n_texts[i][j]))

		self.play(*anims)
		self.wait(3)
		text3 = TextMobject("$i$-ésima coluna e $j$-ésima linha \\\\ do Triângulo de Pascal").shift(np.array([-1, 3, 0]))
		binom3 = MathText("= \\binom{j}{i}").next_to(text3, RIGHT)

		self.play(Transform(text, text3), Transform(binom, binom3))
		self.wait(3)