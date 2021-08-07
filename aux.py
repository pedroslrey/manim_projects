from manimlib.imports import *
import numpy as np
import math
from random import *
from datetime import datetime

class Test2(Scene):
    def construct(self):
        EXPLAIN_WIDTH = 5
        EXPLAIN_HEIGHT = 2
        explain_rect = Rectangle(
                                    width=EXPLAIN_WIDTH,
                                    height=EXPLAIN_HEIGHT,
                                    origin=ORIGIN,
                                    stroke_width=1
                                )
        explain_filled_rect = explain_rect.copy()
        explain_filled_rect.set_fill(RED_A,1)
        # Use stretch=True to preserve the dimension that is not modified
        explain_filled_rect.set_height(1,stretch=True)
        # compress the definitions of your objects, this will make it easier to read them.
        explain_line_left, explain_line_bottom = [
            Line(
                    explain_rect.get_corner(start),
                    explain_rect.get_corner(end),
                    color=RED_A
                )
            for start,end in [(DL,UL),(DL,DR)] 
        ]

        self.play(FadeIn(explain_rect))
        self.play(
                GrowFromEdge(explain_line_left, BOTTOM),
                GrowFromEdge(explain_line_bottom, LEFT)
        )

        self.wait(1)
        self.add(explain_filled_rect)
        # This generates a copy of the element in an 
        # attribute called "target" to which we 
        # can indicate when we want.
        explain_filled_rect.generate_target()

        def update_test(mob,alpha):
            # 1. Reset the rectangle to its flat state
            mob.become(mob.target)
            # 2. Set the new height
            mob.set_height(alpha*explain_rect.get_height(),stretch=True)
            # 3. Move to the new place
            mob.next_to(explain_rect.get_bottom(),UP,buff=0)

        self.play(UpdateFromAlphaFunc(
                    explain_filled_rect,
                    update_test
                 ),
        )

        self.wait(2)