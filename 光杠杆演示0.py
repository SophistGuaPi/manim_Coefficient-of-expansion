from manimlib import *
from os import system
import numpy as npy

class View0(Scene):
    def construct(self):
        mirro_rect=Rectangle(0.1,2)
        mirro_Line=[Line(start=mirro_rect.get_left()).set_angle(-(3/4)*npy.pi).scale(0.1,about_point=mirro_rect.get_left()).
                        shift(i*mirro_rect.get_height()/9*UP)
                    for i in range(-4,5)]
        mirro=VGroup(mirro_rect)
        for i in mirro_Line:
            mirro=VGroup(mirro,i)

        lever_l=VGroup(Rectangle(2,0.2).next_to(mirro_rect.get_corner(DR),DL,buff=0),mirro)
        d0=SmallDot(lever_l.get_corner(DR))
        trig=Triangle().scale(0.3).next_to(d0,DOWN,buff=0)
        lever=VGroup(d0,trig,lever_l)
        eyes=SVGMobject("eye.svg")
        eyes.match_width(lever)

        mirro_normal=DashedLine(start=mirro_rect.get_right()).set_angle(0)
        lever_l=VGroup(lever_l,mirro_normal)
        lever=VGroup(d0,trig,lever_l)



        self.add(lever,eyes)


if __name__ == "__main__":
    system("manimgl 光杠杆演示0.py View0 -p -l ")