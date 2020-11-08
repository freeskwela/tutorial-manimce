
from manim.constants import *
from manim.scene.scene import Scene
from manim.mobject.types.image_mobject import Image, ImageMobject
from manim.mobject.svg.svg_mobject import SVGMobject
from manim.mobject.svg.text_mobject import Text
from manim.mobject.svg.tex_mobject import Tex
from manim.mobject.geometry import Rectangle, Square
from manim.animation.creation import DrawBorderThenFill, ShowCreation
from manim.animation.fading import FadeInFrom, FadeOut, FadeOutAndShift, VFadeOut
from manim.animation.movement import Animation
from manim.animation.transform import ApplyMethod, FadeToColor, ReplacementTransform
from manim.animation.composition import AnimationGroup, LaggedStart
from manim.utils.color import BLACK, DARKER_GREY, DARK_GRAY
from manim.utils.rate_functions import linear, smooth, double_smooth
from typing_extensions import runtime


class FiveDAnimation(Scene):
    def construct(self):
        FIVED_YELLOW = "#FFA500"
        FIVED_GRAY = "#0D0D0D"
        LOGO_UP = 1.5

        bgnd = ImageMobject(filename_or_array="empty_board_1920x1080.tif")
        logo = SVGMobject(file_name="fived")
        text = SVGMobject(file_name="fived_text", stroke_width=0.15)

        bot = logo[0].set_color(FIVED_GRAY)
        top = logo[1].set_color(FIVED_GRAY)
        mid = logo[2].set_color(FIVED_YELLOW)

        frame = Square().scale(1.15)
        frame.set_stroke(color=FIVED_GRAY, width=6)

        text.set_color(FIVED_GRAY)
        text.scale(0.27)
        text.shift(LEFT * 0.15)

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
                stroke_width=1.5,
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
        self.play(ApplyMethod(logo.shift, UP*LOGO_UP), ApplyMethod(frame.shift, UP*LOGO_UP), run_time=1)
        self.play(txt_anim)
        self.wait()

        ps_anim = FadeToColor(text[4], FIVED_YELLOW)

        self.play(ps_anim)

        d = text[4].copy()
        self.add(d)

        self.play(
            VFadeOut(logo, direction=UP, run_time=0.5),
            VFadeOut(frame, run_time=0.5),
            VFadeOut(text, direction=DOWN, run_time=0.5),
            ApplyMethod(d.shift, LEFT, run_time=0.75)
            )

        self.play(ApplyMethod(d.scale, 240), run_time=0.5)
        self.wait()
        self.remove(bgnd)
        self.play(FadeOut(d), run_time=0.5)
        self.wait()
