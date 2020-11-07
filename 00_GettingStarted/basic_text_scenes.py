
from manim.scene.scene import Scene
from manim.mobject.svg.tex_mobject import Tex
from manim.mobject.svg.text_mobject import Text


class BasicAddText(Scene):
    def construct(self):  # scene construction method
        txt = Text("This is a text!")  # text object
        self.add(txt)  # displays the object into the scene
        self.wait(3)  # pause for 3 seconds


class BasicAddLatexText(Scene):
    def construct(self):  # scene construction method
        txt = Tex("This is a LATEX rendered text!")  # LATEX rendered text object
        self.add(txt)  # displays the object into the scene
        self.wait(3)  # pause for 3 seconds
