
from manim.scene.scene import Scene
from manim.mobject.svg.text_mobject import Text
from manim.mobject.svg.tex_mobject import (Tex, MathTex)
from manim.constants import UP, DOWN


class BasicTextComparison(Scene):
    # scene construction method
    def construct(self):
        normal_text = Text("Text : a^2 + b^2 = c^2")  # normal text object
        normal_mode = Tex("Tex (Normal-Mode): a\\textsuperscript{2} + b\\textsuperscript{2} = c\\textsuperscript{2}")  # LaTeX normal
        math_mode   = Tex("Tex (Math-Mode): $a^2 + b^2 = c^2$")  # LaTeX Math-mode
        manim_math  = MathTex("MathTex : a^2 + b^2 = c^2")  # Manim MathLaTeX

        # position objects (default: center)
        normal_text.shift(UP * 3)
        normal_mode.shift(UP)
        math_mode.shift(DOWN)
        manim_math.shift(DOWN * 3)

        self.add(normal_text, normal_mode, math_mode, manim_math)  # add objects to the scene canvas
        self.wait(3)  # 3 second pause (default: 1 sec)


class BasicTextNormal(Scene):
    def construct(self):
        txt = Text("a^2 + b^2 = c^2")
        self.add(txt)
        self.wait()


class BasicTextNormalModeLatex(Scene):
    def construct(self):
        txt = Tex("a\\textsuperscript{2} + b\\textsuperscript{2} = c\\textsuperscript{2}")
        self.add(txt)
        self.wait()


class BasicTextMathModeLatex(Scene):
    def construct(self):
        txt = Tex("$a^2 + b^2 = c^2$")
        self.add(txt)
        self.wait()


class BasicTextMathTex(Scene):
    def construct(self):
        txt = MathTex("a^2 + b^2 = c^2")
        self.add(txt)
        self.wait()
