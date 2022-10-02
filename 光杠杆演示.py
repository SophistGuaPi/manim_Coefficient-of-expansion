from manimlib import *
from os import system

class View0(Scene):
    def construct(self):
        d0 = Dot()
        d1 = Dot().shift(RIGHT * 2)
        d2 = Dot().shift(LEFT * 4)
        d3 = Dot().shift(DOWN + RIGHT * 2)
        d4 = Dot().shift(LEFT * 4 + UP * 2)
        l0_0=Line(d0,d1)
        l0_1=Line(d0,d2)
        l1_0=Line(d0,d3)
        l1_1=Line(d0,d4)
        l0=VGroup(l0_0,l0_1)
        l1=VGroup(l1_0,l1_1)
        l2 = Arrow(d1, d3, buff=0)
        l3 = Arrow(d2, d4, buff=0)
        v0 = VGroup(d0, d1, d2, d3, d4)

        d1_0 = Dot().shift((d1.get_center() - d0.get_center()) / 5).set_opacity(0)
        d2_0 = Dot().shift((d2.get_center() - d0.get_center()) / 5).set_opacity(0)
        d3_0 = Dot().shift((d3.get_center() - d0.get_center()) / 5).set_opacity(0)
        d4_0 = Dot().shift((d4.get_center() - d0.get_center()) / 5).set_opacity(0)
        arc0 = ArcBetweenPoints(d3_0.get_center(), d1_0.get_center())
        arc1 = ArcBetweenPoints(d4_0.get_center(), d2_0.get_center())

        d1_0.add_updater(lambda d:d.become(Dot().shift((d1.get_center() - d0.get_center()) / 5).set_opacity(0).shift(RIGHT)))
        d2_0.add_updater(lambda d: d.become(Dot().shift((d2.get_center() - d0.get_center()) / 5).set_opacity(0).shift(RIGHT)))
        d3_0.add_updater(lambda d: d.become(Dot().shift((d3.get_center() - d0.get_center()) / 5).set_opacity(0).shift(RIGHT)))
        d4_0.add_updater(lambda d: d.become(Dot().shift((d4.get_center() - d0.get_center()) / 5).set_opacity(0).shift(RIGHT)))
        arc0.add_updater(lambda a:a.become(ArcBetweenPoints(d3_0.get_center(), d1_0.get_center())))
        arc1.add_updater(lambda a:a.become(ArcBetweenPoints(d4_0.get_center(), d2_0.get_center())))
        v_arc=VGroup(d1_0,d2_0,d3_0,d4_0,arc0,arc1).shift(LEFT)
        v1 = VGroup(v0, d1_0, d2_0, d3_0, d4_0, l0, l1, l2, l3).shift(RIGHT)

        rect=Rectangle(height=0.2,width=6)
        triang=Triangle().scale(0.5)

        self.play(ShowCreation(rect))
        self.play(FadeIn(triang.next_to(rect,DOWN,0.1)))
        self.play(triang.animate.next_to(d0,DOWN,0.1))
        self.play(Write(l2))
        self.play(ShowCreation(v0),Write(l0),Write(l1))
        self.play(Write(l3))
        triang.add_updater(lambda t: t.become(Triangle().scale(0.5)).next_to(d0, DOWN, 0.1))

        l1.add_updater(lambda l:l.become(Line(d3,d4)))
        l2.add_updater(lambda a:a.become(Arrow(d1, d3, buff=0)))
        l3.add_updater(lambda a: a.become(Arrow(d2, d4, buff=0)))

        b0 = Brace(l2,RIGHT)
        b1 = Brace(l3,LEFT)
        text0, number0 = label0 = VGroup(Tex(r"F_1="), DecimalNumber(l2.length_over_dim(1)))
        text1, number1 = label1 = VGroup(Tex(r"F_2="), DecimalNumber(l3.length_over_dim(1)))
        label0.arrange(RIGHT)
        label1.arrange(RIGHT)
        b0.put_at_tip(label0)
        b1.put_at_tip(label1)
        self.play(ShowCreation(b0),ShowCreation(b1),Write(label0),Write(label1))

        b0.add_updater(lambda b:b.become(Brace(l2,RIGHT)))
        b1.add_updater(lambda b: b.become(Brace(l3,LEFT)))
        number0.add_updater(lambda n: n.set_value(l2.length_over_dim(1)))
        number1.add_updater(lambda n: n.set_value(l3.length_over_dim(1)))
        b0.add_updater(lambda b:b.put_at_tip(label0))
        b1.add_updater(lambda b: b.put_at_tip(label1))
        self.play(Write(v_arc))
        self.play(d3.animate.shift(DOWN),d4.animate.shift(UP*2))

        d3_1=Dot(d3.get_center()+UP*1e-4)
        d4_1=Dot(d4.get_center()+DOWN*1e-4)
        dl0=DashedLine(d3,d3_1)
        dl1=DashedLine(d4,d4_1)
        dl2=DashedLine(d3_1,d4_1)
        self.play(Write(d3_1),Write(d4_1),Write(dl0),Write(dl1),Write(dl2))

        b0_1 = Brace(dl0, RIGHT)
        b1_1 = Brace(dl1, LEFT)
        text0_1, number0_1 = label0_1 = VGroup(Tex(r"\Delta F_1="), DecimalNumber(dl0.length_over_dim(1)))
        text1_1, number1_1 = label1_1 = VGroup(Tex(r"\Delta F_2="), DecimalNumber(dl1.length_over_dim(1)))
        label0_1.arrange(RIGHT)
        label1_1.arrange(RIGHT)
        b0_1.put_at_tip(label0_1)
        b1_1.put_at_tip(label1_1)
        self.play(ShowCreation(b0_1), ShowCreation(b1_1), Write(label0_1), Write(label1_1))

        dl0.add_updater(lambda l:l.become(DashedLine(d3,d3_1)))
        dl1.add_updater(lambda l:l.become(DashedLine(d4, d4_1)))
        dl2.add_updater(lambda l:l.become(DashedLine(d3_1,d4_1)))
        b0_1.add_updater(lambda b: b.become(Brace(dl0, RIGHT)))
        b1_1.add_updater(lambda b: b.become(Brace(dl1, LEFT)))
        number0_1.add_updater(lambda n: n.set_value(dl0.length_over_dim(1)))
        number1_1.add_updater(lambda n: n.set_value(dl1.length_over_dim(1)))
        b0_1.add_updater(lambda b: b.put_at_tip(label0_1))
        b1_1.add_updater(lambda b: b.put_at_tip(label1_1))

        self.play(d3.animate.shift(UP*1), d4.animate.shift(DOWN * 2))

        b2_0 = Brace(l0_0, UP)
        b3_0 = Brace(l0_1, DOWN)
        text2_0, number2_0 = label2_0 = VGroup(Tex(r"l_1="), DecimalNumber(l0_0.length_over_dim(0)))
        text3_0, number3_0 = label3_0 = VGroup(Tex(r"l_2="), DecimalNumber(l0_1.length_over_dim(0)))
        label2_0.arrange(RIGHT)
        label3_0.arrange(RIGHT)
        b2_0.put_at_tip(label2_0)
        b3_0.put_at_tip(label3_0)

        b2_0.add_updater(lambda b:b.become(Brace(l0_0, UP)))
        b3_0.add_updater(lambda b: b.become(Brace(l0_1, DOWN)))
        number2_0.add_updater(lambda n: n.set_value(l0_0.length_over_dim(0)))
        number3_0.add_updater(lambda n: n.set_value(l0_1.length_over_dim(0)))
        b2_0.add_updater(lambda b:b.put_at_tip(label2_0))
        b3_0.add_updater(lambda b: b.put_at_tip(label3_0))

        self.play(ShowCreation(b2_0), ShowCreation(b3_0), Write(label2_0), Write(label3_0))

        l0_0.add_updater(lambda l: l.become(Line(d0, d1)))
        l0_1.add_updater(lambda l: l.become(Line(d0, d2)))
        l1_0.add_updater(lambda l: l.become(Line(d0, d3)))
        l1_1.add_updater(lambda l: l.become(Line(d0, d4)))
        l0.add_updater(lambda l:l.become(VGroup(l0_0,l0_1)))
        l1.add_updater(lambda l: l.become(VGroup(l1_0, l1_1)))
        # d4.add_updater(lambda d:d.become(Dot().shift(d4.get_center()+)))
        d4.add_updater(lambda d: d.match_y(Dot().shift(d0.get_center()+
            (d0.get_center()-d3.get_center())/(l0_0.length_over_dim(0)/l0_1.length_over_dim(0)))))
        d4_1.add_updater(lambda d:d.match_y(Dot().shift(d0.get_center()+
            (d0.get_center()-d3_1.get_center())/(l0_0.length_over_dim(0)/l0_1.length_over_dim(0)))))

        self.play(Uncreate(v_arc))
        self.play(d0.animate.shift(LEFT*1.5))

        text4=Text("杠杆原理(相似三角形)：",font="msyh",font_size=32)
        tex0=Tex(r"\frac{F_1}{F_2}","=",r"\frac{l_1}{l_2}")
        tex1 = Tex(r"\frac{\Delta F_1}{\Delta F_2}","=",r"\frac{l_1}{l_2}")
        text4.next_to(v1,DOWN,buff=1.5).shift(LEFT*2)
        tex0.next_to(text4,RIGHT)
        tex1.next_to(text4,RIGHT)
        v_text=VGroup(text0,text1,text2_0,text3_0)


        self.play(Write(text4))
        self.play(TransformMatchingShapes(v_text.copy(),tex0))
        self.play(TransformMatchingTex(tex0,tex1,key_map={r"":r"\Delta F"}))
        self.wait(2)

        self.clear()





if __name__ == "__main__":
    system("manimgl 光杠杆演示.py View0 -w")