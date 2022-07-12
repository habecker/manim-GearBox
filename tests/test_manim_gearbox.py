from manim import *
from manim_gearbox import *

class gear_example(Scene):
    def construct(self):
        # small gear
        gear1=Gear(15, module=0.2, stroke_opacity=0, fill_color=WHITE,fill_opacity=1)
        # larger gear
        gear2=Gear(27, module=0.2, stroke_opacity=0, fill_color=RED, fill_opacity=1)
        # shifting gear1 away from center
        gear1.shift(gear1.rp * 1 *LEFT)
        # position gear2 next to gear1 so that they mesh together
        gear2.mesh_to(gear1,offset=0.2*gear1.m)

        self.add(gear1, gear2)
        self.play(Rotate(gear1, gear1.pitch_angle, rate_func=linear),
                  Rotate(gear2, - gear2.pitch_angle, rate_func=linear),
                  run_time=4)

class gear_example_inner(Scene):
    def construct(self):
        # smaller gear
        gear1 = Gear(15, module=1, stroke_opacity=0, fill_color=WHITE,fill_opacity=0.5, nppc=10)
        # larger gear with inner teeth
        gear2 = Gear(35, module=1,
                     nppc=10,
                     inner_teeth=True, stroke_opacity=0, fill_color=RED, fill_opacity=0.5)
        gear1.shift(gear1.rp * UP*1.01)
        gear2.shift(gear2.rp*UP*0.99)
        gear1.rotate(0.05)
        gear1.mesh_to(gear2,offset=0.25*0,positive_bias=False)

        self.add(gear1)
        self.add(gear2)
        # self.add(Line(start=gear1.get_center(), end=gear2.get_center()))
        self.play(Rotate(gear1, gear1.pitch_angle, rate_func=linear),
                  Rotate(gear2, gear2.pitch_angle, rate_func=linear),
                  run_time=10)

class test_Gear(MovingCameraScene):
    def construct(self):
        gear1 = Gear(10, module=0.5, stroke_opacity=0.3, stroke_width=0.25, fill_color=WHITE, fill_opacity=0.3,
                     h_a=1,h_f=1.2, cutout_teeth_num=5, profile_shift=0)
        circ1 = Circle(radius=gear1.rf, stroke_opacity=0.3,stroke_width=1)
        circ2 = Circle(radius=gear1.ra, stroke_opacity=0.3,stroke_width=1)
        circ3 = Circle(radius=gear1.rp, stroke_opacity=0.3, stroke_color=GREEN, stroke_width=1)
        circ4 = Circle(radius=gear1.rb, stroke_opacity=0.3, stroke_color=BLUE, stroke_width=1)
        grp1 = VGroup(gear1, circ1, circ2, circ3, circ4)
        grid1 = NumberPlane()
        grp1.shift(gear1.rp * LEFT)
        # gear2 = gear1.copy().make_smooth()
        # gear2.set_stroke(color=RED)
        # self.camera.frame.move_to(gear1)
        # self.camera.frame.set(width=2)
        self.add(circ1,circ2,circ3,circ4,grid1,gear1)

class test_Gear_mesh(MovingCameraScene):
    def construct(self):
        m=1
        x=0.3
        gear1 = Gear(10, module=m, stroke_opacity=0, stroke_width=0.5, fill_color=WHITE, fill_opacity=0.5,
                     h_a=1,h_f=1.2,profile_shift=x, nppc=20)
        gear2 = Gear(30, module=m, stroke_opacity=0, stroke_width=0.5, fill_color=WHITE, fill_opacity=0.5,
                     h_a=1, h_f=1.2, profile_shift=0.2,nppc=20,
                     inner_teeth=False)
        rack1 = Rack(21,module=m,h_a=1,h_f=1,
                     fill_color=WHITE, fill_opacity=0.5,
                     stroke_opacity=0, stroke_width=0.5,)
        rack1.rotate_about_origin(PI)
        circ1 = Circle(radius=gear1.rf, stroke_opacity=0.3,stroke_width=1)
        circ2 = Circle(radius=gear1.ra, stroke_opacity=0.3,stroke_width=1)
        circ3 = Circle(radius=gear1.rp, stroke_opacity=0.3, stroke_color=GREEN, stroke_width=1)
        circ4 = Circle(radius=gear1.rb, stroke_opacity=0.3, stroke_color=BLUE, stroke_width=1)
        grp1 = VGroup(gear1,circ1,circ2,circ3,circ4)
        grid1 = NumberPlane()
        grp1.shift(gear1.rp*LEFT*1.2)
        gear2.shift(gear2.rp*LEFT)
        rack1.shift(x*m*RIGHT)

        gear1.rotate(gear1.pitch_angle*0.2)

        ofs_tr = ValueTracker(0.0)
        gear1.mesh_to(gear2,offset=0.3*m,positive_bias=True)


        gear1.add_updater(lambda mob: mob.mesh_to(gear2,offset=ofs_tr.get_value()*m))
        # self.camera.frame.move_to(gear1)
        # self.camera.frame.set(width=2)
        self.add(circ1,circ2,circ3,circ4,grid1,gear1,gear2)


class test_Rack(Scene):
    def construct(self):
        rack1 = Rack(10,module=1, h_a=1.17, stroke_opacity=0,fill_opacity=1,fill_color=RED)
        gear1 = Gear(10, module=1,stroke_opacity=0,fill_opacity=1,fill_color=WHITE)
        gear1.shift(RIGHT*gear1.rp)
        rack1.shift(UP*rack1.pitch*0.5)
        self.add(gear1,rack1)
        self.play(Rotate(gear1, gear1.pitch_angle * 2),
                  rack1.animate.shift(DOWN*rack1.pitch * 2),
                  rate_func=linear, run_time=10)

class test_Gear_inner(MovingCameraScene):
    def construct(self):
        gear1 = Gear(12, module=0.4, inner_teeth=True,
                     cutout_teeth_num=5, profile_shift=0.0,
                     stroke_opacity=1, stroke_width=1, fill_color=WHITE, fill_opacity=0.3, h_a=1,h_f=1)
        circ_gear = Circle(gear1.ra+0.2)
        gear2 = Difference(circ_gear,gear1,stroke_opacity=1, stroke_width=0.3, fill_color=WHITE, fill_opacity=0.3,)
        circ1 = Circle(radius=gear1.rf, stroke_opacity=0.3, stroke_width=1)
        circ2 = Circle(radius=gear1.ra, stroke_opacity=0.3, stroke_color=YELLOW, stroke_width=1)
        circ3 = Circle(radius=gear1.rp, stroke_opacity=0.3, stroke_color=GREEN, stroke_width=1)
        circ4 = Circle(radius=gear1.rb, stroke_opacity=0.3, stroke_color=BLUE, stroke_width=1)
        grid1 = NumberPlane()


        # self.camera.frame.move_to(RIGHT*gear1.ra)
        # self.camera.frame.set(width=2)
        self.add(circ1,circ2,circ3,circ4,grid1,gear1)


# brute force param combination tester
class test_gear_param(Scene):
    def construct(self):
        ha_params = np.array([3,  5,  7,  9, 10]) /10
        hf_params = ha_params * 1.5

        min_tooth = 8
        max_tooth = 40
        tooth_arr = np.arange(min_tooth,max_tooth,3)

        gear_grp = VGroup()

        for tooth in tooth_arr:
            for h_a in ha_params:
                for h_f in hf_params:
                    gear =  Gear(tooth, h_a=h_a,h_f=h_f)
                    print("ha=",h_a,"hf=",h_f,"tooth=",tooth)
                    # gear2 = Gear(tooth, h_a=h_a,h_f=h_f, inner_teeth=True)
                    gear_grp.add(gear)

        self.add(gear_grp)

# this part is used for debugging
# with tempconfig({"quality": "medium_quality", "disable_caching": True}):
#     scene = test_Gear()
#     scene.render()
