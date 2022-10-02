from manimlib import *
from os import system
import numpy as npy
import sympy

class View_re(Scene):
    def construct(self):
        def updateSoluve(h):
            x = sympy.symbols("x")
            func = 1 / (x - 0.5) ** 2 - 6 / x ** 2
            solute = npy.array(sympy.solve(func - h.get_value(), x))
            for i in range(len(solute)):
                solute[i] = sympy.re(solute[i])
            solute.sort()
            return solute

        camera=self.camera.frame

        axes0 = Axes(x_range=[-10,10,5],x_axis_config={"include_tip":True},y_axis_config={"include_tip":True})
        axes0_label=axes0.get_axis_labels(r"x",r"U(x)")
        axes1 = Axes(x_range=[-10,10,1],x_axis_config={"include_tip":True},y_axis_config={"include_tip":True})

        c0 = Circle().scale(0.5)
        c1 = Circle().scale(0.5)
        d0 = SmallDot()
        d1 = SmallDot()
        d2 = SmallDot()
        d3 = SmallDot()
        d4 = SmallDot()
        d5 = SmallDot()

        c0.set_fill(GOLD_C,opacity=1)
        c0.set_stroke(YELLOW,opacity=0.7)
        c1.set_fill(GOLD_C,opacity=1)
        c1.set_stroke(YELLOW,opacity=0.7)
        c1.scale(1/5)
        c2 = c1.copy()

        x=sympy.symbols("x")
        f=1 / (x - 0.5) ** 2 - 6 / x ** 2
        g0=axes1.get_graph(lambda x:1/(x-0.5)**2-6/x**2,x_range=[0.78,10,0.01],color=YELLOW)
        g1=axes1.get_graph(lambda x: 1 / (x + 0.5) ** 2 - 6 / x ** 2, x_range=[-10, -0.78,0.01],color=YELLOW)

        # self.play(FadeIn(c0))
        # self.wait()
        #
        # self.play(FadeOut(c0))
        # self.wait()

        # 添加公式动画
        # text0=Text("原子间相互作用势",font="msyh",font_size=32,)
        # text01 = Text("EAM模型", font="msyh", font_size=32,
        #              t2c={
        #                  "E":RED_C,
        #                  "A":GREEN_A,
        #                  "M":BLUE_A
        #              }
        #              )
        # text02 = Text("EAM(embedded-atom method,嵌入原子方法)模型", font="msyh", font_size=32,
        #               t2c={
        #                   "E": RED_C,
        #                   "A": GREEN_A,
        #                   "M": BLUE_A,
        #                   "embedded":RED_C,
        #                   "atom":GREEN_A,
        #                   "method":BLUE_A,
        #                   "嵌入":RED_C,
        #                   "原子":GREEN_A,
        #                   "方法":BLUE_A
        #               }
        #               )
        #
        # self.play(Write(text0))
        # self.wait()
        # self.play(ReplacementTransform(text0,text01))
        # self.wait()
        # self.play(TransformMatchingStrings(text01,text02))
        # self.wait()
        # self.play(text02.animate.align_on_border(UL))
        # self.wait()
        #
        # tex0=Tex(r"E=",r"\sum_{i} F_i(\rho_{i})",font_size=32,
        #          tex_to_color_map={
        #              r"\sum_{i} F_i(\rho_{i})":RED_C
        # })
        # self.play(Write(tex0))
        # self.wait()
        # tex01=Tex(r"E","=",r"\sum_{i}F_i(\rho_{i})","+",r"\frac{1}{2}\sum_{i,j(i\neq{j})}\phi_{ij}(r_{ij})",font_size=32,
        # tex_to_color_map = {
        #     r"\sum_{i}F_i(\rho_{i})": RED_C,
        #     r"\frac{1}{2}\sum_{i,j(i\neq{j})}\phi_{ij}(r_{ij})":GREEN_A
        # }
        # )
        # self.play(TransformMatchingShapes(tex0,tex01))
        # self.wait()
        # self.play(tex01.animate.next_to(text02,DOWN))
        # self.wait()
        # box_t0=SurroundingRectangle(tex01[2])
        # self.play(Write(box_t0))
        # self.wait()
        # tex1=Tex(r"\rho_{i}=\sum_{j(i\neq{j})}f_{i}(r_{ij})",font_size=32,
        # tex_to_color_map = {
        #     r"\rho_{i}=\sum_{j(i\neq{j})}f_{i}(r_{ij})": RED_C,
        # }
        # )
        # box_t1=SurroundingRectangle(tex1)
        # v_t1=VGroup(box_t1,tex1)
        # self.play(Write(box_t1))
        # self.wait()
        # self.play(Write(tex1))
        # self.wait()
        # self.play(v_t1.animate.next_to(tex01,DOWN))
        # self.wait()
        # box_t01=SurroundingRectangle(tex01[4])
        # self.play(ReplacementTransform(box_t0,box_t01),FadeOut(box_t1))
        # self.wait()
        # tex2=Tex(r"\phi_{AB}(r)=\frac{Z_{A}(r)Z_{B}(r)}{r}",font_size=32,
        # tex_to_color_map = {
        #     r"\phi_{AB}(r)=\frac{Z_{A}(r)Z_{B}(r)}{r}": GREEN_A,
        # }
        # )
        # box_t2=SurroundingRectangle(tex2)
        # v_t2=VGroup(box_t2,tex2)
        # self.play(Write(box_t2))
        # self.wait()
        # self.play(Write(tex2))
        # self.wait()
        # self.play(v_t2.animate.next_to(v_t1,DOWN))
        # self.wait()
        # self.play(FadeOut(box_t2),FadeOut(box_t01))
        # self.wait()
        # tex3=Tex(r"E","=",r"\sum_{i}F_i(\sum_{j(\neq{i})}f_{j}(r_{ij}))","+",r"\frac{1}{2}\sum_{i,j(i\neq{j})}{{Z_{i}(r_{ij})Z_{j}(r_{ij})}\over r_{ij}}",font_size=32,
        # tex_to_color_map = {
        #     r"f_{j}(r_{ij})": RED_C,
        #     r"{Z_{i}(r_{ij})Z_{j}(r_{ij})}":GREEN_A
        # }
        # )
        # tex3.next_to(text02,DOWN)
        # v0=VGroup(tex01,tex1,tex2)
        # self.play(TransformMatchingShapes(v0,tex3))
        # self.wait()
        # tex4=Tex(r"f(r)=n_{s}f_{s}(r)+n_{d}f_{d}(r)",font_size=32,
        # tex_to_color_map = {
        #     r"f(r)=n_{s}f_{s}(r)+n_{d}f_{d}(r)": RED_C,
        # }
        # )
        # box_4=SurroundingRectangle(tex4)
        # box_t30=SurroundingRectangle(tex3[3])
        # self.play(Write(box_t30))
        # self.wait()
        # self.play(Write(box_4))
        # self.wait()
        # self.play(Write(tex4))
        # self.wait()
        # v4=VGroup(box_4,tex4)
        # self.play(v4.animate.next_to(tex3,DOWN))
        # self.wait()
        # tex5 = Tex(r"Z(r)=Z_{0}(1+{\beta}r^{\upsilon})e^{-{\alpha}r}", font_size=32,
        #            tex_to_color_map={
        #                r"Z(r)=Z_{0}(1+{\beta}r^{\upsilon})e^{-{\alpha}r}": GREEN_A,
        #            }
        #            )
        # box_t31=SurroundingRectangle(tex3[7])
        # box_5=SurroundingRectangle(tex5)
        # v5=VGroup(box_5,tex5)
        # self.play(ReplacementTransform(box_t30,box_t31),FadeOut(box_4))
        # self.wait()
        # self.play(Write(box_5))
        # self.wait()
        # self.play(Write(tex5))
        # self.wait()
        # self.play(v5.animate.next_to(tex4,DOWN))
        # self.wait()
        # self.play(FadeOut(box_5),FadeOut(box_t31))
        # self.wait()
        # v1=VGroup(text02,tex3,tex4,tex5)
        # self.play(v1.animate.scale(0.8,about_point=v1.get_corner(UL)))
        # self.wait()

        text_cu = Tex(r"Cu", font_size=32)
        text_cu.next_to(c0, DL)
        text_cu.add_updater(lambda t: t.next_to(c0, DL))
        self.play(FadeIn(c0),Write(text_cu))
        self.wait()
        self.add(axes0, c0)
        self.play(ShowCreation(axes0, lag_ratio=0.25),ShowCreation(axes0_label))
        self.wait()
        self.play(c0.animate.scale(1/5),Transform(axes0,axes1))
        self.wait()
        vg=VGroup(g1,g0)
        # self.play(TransformMatchingShapes(v1,vg))
        # self.wait()
        self.play(FadeIn(vg),run_time=0.5)
        self.wait()
        self.play(FadeOut(vg),run_time=0.5)
        self.wait()
        self.play(c0.animate.shift(LEFT*2),c1.animate.shift(RIGHT*2))
        self.wait()
        self.play(c0.animate.shift(RIGHT*2),c1.animate.shift(RIGHT*2))
        self.wait()
        self.play(FadeIn(g0),run_time=0.5)
        self.wait()
        # self.play(FadeOut(c2),FadeOut(g1))
        # self.wait()
        v0 = VGroup(axes0, c0, c1, g0)
        self.add(axes0,v0,c0,c1,g0)
        self.play(camera.animate.scale(0.67,about_point=axes0.get_corner(UR)).shift(RIGHT*2))
        self.wait()

        E0=-2
        E_end=-0.1
        bias=0.03

        solute0=ValueTracker()
        solute1=ValueTracker()
        h =ValueTracker(E0)
        solute0.set_value(updateSoluve(h)[-1]+bias)
        solute1.set_value(updateSoluve(h)[-2]+bias)
        d0.move_arc_center_to(axes0.c2p(solute0.get_value(),E0))
        d1.move_arc_center_to(axes0.c2p(solute1.get_value(),E0))
        d2.move_arc_center_to(axes0.c2p((solute0.get_value()+solute1.get_value())/2,E0))
        d3.match_x(d2)
        d3.set_y(axes0.c2p(0,0)[1])
        d4.match_x(d3)
        d4.match_y(d0)
        d5.match_x(d2)
        d5.match_y(axes0.get_origin())
        l0=Line(d0.get_center(),d1.get_center())
        l1=DashedLine(d3.get_center(),d4.get_center())
        l2=Line(axes0.c2p(0,0),d5.get_center())
        l3=DashedLine(d2.get_center(),d5.get_center())

        b0=always_redraw(Brace,l2,UP)
        text,number=label=VGroup(Tex(r"x"),DecimalNumber(l2.length_over_dim(0)).set_opacity(0))
        label.arrange(UP)
        b0.put_at_tip(label)
        tria = Triangle().set_color(RED_C).scale(0.05).rotate(npy.pi).next_to(d5,UP,buff=0)
        tria.add_updater(lambda t: t.next_to(d5, UP,buff=0))

        self.add(l2,axes0,d2, c0, c1, d0, d1, l0)
        self.play(ShowCreation(d0),ShowCreation(d1),ShowCreation(d2),ShowCreation(d3),ShowCreation(d4),ShowCreation(l1),ShowCreation(l0),
                  c1.animate.move_arc_center_to(axes0.c2p((solute0.get_value()+solute1.get_value()+0.2)/2)))
        self.wait()

        axes2 = Axes(x_range=[0,3.3],y_range=[0,4],x_axis_config={"include_tip":True},y_axis_config={"include_tip":True}).scale(0.3).to_corner(UR).shift(DOWN*0.4+RIGHT*1.4)
        axes2_label=axes2.get_axis_labels(r"\varepsilon_{k}",r"x").shift(UP*0.2)
        axes2_label[0].scale(0.5).shift(RIGHT*1.5)
        axes2_label[1].scale(0.5).shift(LEFT*0.7)

        d6=SmallDot(axes2.c2p(h.get_value()+3,axes0.p2c(d2.get_center())[0]-0.4))
        path0 = TracedPath(d6.get_center)
        self.add(axes2,axes2_label,l3,label,d5,tria,c1,l0)
        self.play(ShowCreation(d5),ShowCreation(tria),ShowCreation(l3),ShowCreation(b0),ShowCreation(label),ShowCreation(d6),ShowCreation(axes2),ShowCreation(axes2_label))
        self.wait()



        self.add(axes0, c0,l3, c1,tria,d5, d0, d1, d2,d6, l0,b0,number,text,path0)
        solute0.add_updater(lambda s:s.set_value(updateSoluve(h)[-1]+bias),0)
        solute1.add_updater(lambda s:s.set_value(updateSoluve(h)[-2]+bias),0)
        d0.add_updater(lambda d:d.move_arc_center_to(axes0.c2p(solute0.get_value(),h.get_value())),1)
        d1.add_updater(lambda d:d.move_arc_center_to(axes0.c2p(solute1.get_value(),h.get_value())),1)
        d2.add_updater(lambda d:d.move_arc_center_to(axes0.c2p((solute0.get_value()+solute1.get_value())/2,h.get_value())),2)
        d3.add_updater(lambda d:d.move_arc_center_to(axes0.c2p((solute0.get_value()+solute1.get_value())/2
            +(solute0.get_value()-solute1.get_value())/2*npy.cos(((h.get_value()-2)*40)*h.get_value()+1.8)
                                                    ,0)),1)
        d4.add_updater(lambda d:d.match_x(d3),2)
        d4.add_updater(lambda d:d.match_y(d0),2)
        d5.add_updater(lambda d:d.match_x(d2),3)
        d6.add_updater(lambda d:d.move_arc_center_to(axes2.c2p(h.get_value()+3,axes0.p2c(d2.get_center())[0]-0.6)))
        l0.add_updater(lambda l:l.become(Line(d0.get_center(),d1.get_center())),2)
        l1.add_updater(lambda l:l.become(DashedLine(d3.get_center(),d4.get_center())),2)
        c1.add_updater(lambda c:c.match_x(d3),2)
        l2.add_updater(lambda l:l.put_start_and_end_on(axes0.c2p(0,0),d5.get_center()),3)
        l3.add_updater(lambda l:l.become(DashedLine(d2.get_center(),d5.get_center())),4)
        b0.add_updater(lambda b: b.become(Brace(l2, UP)), 2)
        number.add_updater(lambda n: n.set_value(l2.length_over_dim(0)))
        text.add_updater(lambda t: t.next_to(number, DOWN))
        label.add_updater(lambda l: l.arrange(UP))
        always(b0.put_at_tip, label)



        self.play(c1.animate.move_to(axes0.c2p((solute0.get_value()+solute1.get_value())/2
            +(solute0.get_value()-solute1.get_value())/2*npy.cos(((h.get_value()-2)*20)*h.get_value()+1.8)
                                                    ,0)), run_time=0.1)
        self.play(h.animate.set_value(E_end),solute0.animate.set_value(h.get_value()),solute1.animate.set_value(h.get_value()),rate_func=linear,run_time=18)
        self.wait()

        self.play(camera.animate.scale(0.5, about_point=axes2.get_corner(UR)))
        self.wait()

        tex0 = Tex(r"E=\varepsilon_{k}+U", font_size=20).next_to(camera.get_corner(UP), DR).shift(LEFT*0.5)
        tex1 = Tex(r"\overline{\varepsilon_{k}}=k_{B}T", font_size=20).next_to(tex0, DOWN)
        tex=VGroup(tex0,tex1,axes2_label[0])
        self.play(Write(tex0))
        self.play(Write(tex1))
        d6.suspend_updating()
        tex.lock_data(r"T")
        self.play(TransformMatchingShapes(tex,Tex(r"T").match_width(axes2_label[0]).scale(0.7).move_to(axes2_label[0])))
        tex2 = Tex(r"l=2\sqrt{2}x", font_size=20).next_to(camera.get_corner(UP), DR).shift(LEFT * 0.5)
        tex_1=VGroup(tex2,axes2_label[1])
        self.play(Write(tex2))
        self.play(TransformMatchingShapes(tex_1,Tex(r"l").match_width(axes2_label[1]).scale(0.5).move_to(axes2_label[1])))

        Delta_T=ValueTracker(int(12*len(path0.get_all_points())/20)-2)
        num_line=NumberLine(x_range=[201,Delta_T.get_value(),400], include_tip=True).set_width(camera.get_width()).scale(0.4)
        num_line.next_to(camera.get_edge_center(UP), DOWN).shift(LEFT*0.3)
        num_line_tex=Tex(r"\Delta T",font_size=15).next_to(num_line,DR,buff=0.1)
        dot_Taxis = SmallDot().set_opacity(0)
        tria_t = Triangle().set_width(camera.get_width()).scale(0.005).rotate(npy.pi).next_to(dot_Taxis, UP, buff=0)
        dot_Taxis.add_updater(lambda d: d.become(SmallDot(num_line.n2p(Delta_T.get_value())).set_opacity(0)))
        tria_t.add_updater(lambda t: t.next_to(dot_Taxis, UP, buff=0))

        path_dot0=SmallDot(path0.get_all_points()[250])
        path_dot1_list=[]
        for i in range(int(15*len(path0.get_all_points())/20)-1):
            path_dot1_list.append(SmallDot(path0.get_all_points()[15+i+1]))
        path_dot1=path_dot1_list[int(Delta_T.get_value())]
        l_pd=Line(path_dot0,path_dot1).set_stroke(width=1.5).set_color(RED)

        lT0=axes2.get_v_line(path_dot0.get_center())
        lT1=axes2.get_v_line(path_dot1.get_center())
        print(int(Delta_T.get_value()))
        self.play(Write(path_dot0),Write(path_dot1),Write(l_pd),Write(num_line),Write(num_line_tex),Write(tria_t),Write(dot_Taxis),Write(lT0),Write(lT1))#
        path_dot1.add_updater(lambda d:d.become(path_dot1_list[int(Delta_T.get_value())]))
        l_pd.add_updater(lambda l:l.become(Line(path_dot0,path_dot1).set_stroke(width=1.5).set_color(RED)))
        lT1.add_updater(lambda l:l.become(axes2.get_v_line(path_dot1.get_center())))

        b1 = Brace(l_pd, DOWN)
        text0, number0 = label0 = VGroup(Tex(r"\Delta T",font_size=15), DecimalNumber(l_pd.length_over_dim(0)).set_opacity(0))
        label0.arrange(DOWN)
        b1.put_at_tip(label0,buff=0.1)
        b1.add_updater(lambda b: b.become(Brace(l_pd,DOWN).shift(DOWN*0.3).stretch_to_fit_height(0.1)))
        number0.add_updater(lambda n: n.set_value(l_pd.length_over_dim(0)))
        text0.add_updater(lambda t: t.next_to(number0,UP,buff=1.3))
        label0.add_updater(lambda l: l.arrange(DOWN))
        b1.add_updater(lambda b1:b1.put_at_tip(label0,buff=0.1))

        # T_num=DecimalNumber().set_width(camera.get_width()).scale(0.1)
        # T_num.add_updater(lambda n:n.set_value(int(Delta_T.get_value())))

        # T_num.next_to(num_line, DOWN)
        # self.add(T_num)
        self.play(Write(label0),Write(b1))
        self.play(Delta_T.animate.set_value(251),run_time=5)







if __name__ == "__main__":
    system("manimgl 铜晶胞伸长_改_0.py View1 -w -n23")#-n23-n27-31