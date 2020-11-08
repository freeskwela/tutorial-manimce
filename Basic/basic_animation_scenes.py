
from math import log
from manim.animation.transform import ApplyMethod
from manim.constants import *
from manim.scene.scene import Scene
from manim.mobject.types.image_mobject import Image, ImageMobject
from manim.mobject.svg.svg_mobject import SVGMobject
from manim.mobject.svg.text_mobject import Text
from manim.mobject.svg.tex_mobject import Tex
from manim.mobject.geometry import Rectangle, Square
from manim.animation.creation import DrawBorderThenFill, ShowCreation
from manim.animation.fading import FadeInFrom
from manim.animation.movement import Animation
from manim.animation.composition import AnimationGroup
from manim.utils.color import BLACK, DARKER_GREY, DARK_GRAY
from manim.utils.rate_functions import linear, smooth, double_smooth


class FiveDAnimation(Scene):
    def construct(self):
        FIVED_YELLOW = "#FFA500"
        FIVED_GRAY = "#0D0D0D"

        bgnd = ImageMobject(filename_or_array="empty_board_1920x1080.tif")
        logo = SVGMobject(file_name="fived")
        text = Text("FIVED", font="Montserrat", size=1.5, color=FIVED_GRAY)

        bot = logo[0].set_color(FIVED_GRAY)
        top = logo[1].set_color(FIVED_GRAY)
        mid = logo[2].set_color(FIVED_YELLOW)

        frame = Square().scale(1.25)
        frame.set_stroke(color=FIVED_GRAY, width=6)

        mid_anim = DrawBorderThenFill(
            vmobject=mid,
            run_time=3,
            rate_func=double_smooth,
            stroke_width=6,
            stroke_color=FIVED_YELLOW,
            )

        bot_anim = DrawBorderThenFill(
            vmobject=bot,
            run_time=3,
            rate_func=double_smooth,
            stroke_width=1,
            stroke_color=DARK_GRAY,
            )
        
        top_anim = DrawBorderThenFill(
            vmobject=top,
            run_time=3,
            rate_func=double_smooth,
            stroke_width=1,
            stroke_color=DARK_GRAY,
            )
        
        txt_anim = DrawBorderThenFill(
            vmobject=text,
            run_time=3,
            rate_func=double_smooth,
            stroke_width=1,
            stroke_color=DARK_GRAY,
            )

        frame_create = DrawBorderThenFill(
            vmobject=frame,
            run_time=3,
            rate_func=double_smooth,
            stroke_width=1,
            stroke_color=DARK_GRAY,
            )
        
        self.add(bgnd)  # add background
        self.play(frame_create, bot_anim, top_anim, mid_anim)
        self.wait()
        self.play(ApplyMethod(logo.shift, UP * 2), ApplyMethod(frame.shift, UP * 2), run_time=1)
        self.play(txt_anim)
        self.wait()
