from manim import *
import numpy as np


class ParallelogramAnimation1(Scene):
    def construct(self):
        # Define vectors and parallelogram
        plane = NumberPlane(y_range=(-9,9))
        self.add(plane)
        vector1 = Vector([2,1])
        vector2 = Vector([3,0])
        parallelogram = Polygon(vector1.get_start(), vector1.get_end(), vector1.get_end() + vector2.get_end(), vector2.get_end(), fill_opacity=0.5, fill_color=YELLOW)

        # Display the vectors and parallelogram
        self.play(Create(vector1), Create(vector2))
        self.play(Create(parallelogram))
        arVal1 = np.linalg.norm(np.cross(vector1.get_vector(),vector2.get_vector()))

        area_text = DecimalNumber(arVal1).next_to(parallelogram)
        self.add(area_text)
        # Function to update parallelogram area
        def update_area(parallelogram):
            parallelogram.become(Polygon(vector1.get_start(), vector1.get_end(), vector1.get_end() + vector2.get_end(), vector2.get_end(), fill_opacity=0.5, fill_color=YELLOW))
            area_text.next_to(parallelogram)  # Update the position of the area text
            arVal = np.linalg.norm(np.cross(vector1.get_vector(),vector2.get_vector()))
            area_text.set_value(arVal)  # Update the displayed area value
        
        # Create and add the area text label
        

        # Animate the change in angle and area
        for angle in range(0, 181, 5):  # Change angle in steps of 5 degrees
            angle_in_radians = angle * DEGREES
            self.play(
                Rotate(vector2, angle_in_radians - vector2.get_angle(), about_point=vector1.get_start()),
                UpdateFromFunc(parallelogram, update_area)
            )
            self.wait(0.1)  # Add a short pause for each step

        self.wait(2)  # Add a final pause


class ProjectionAnimation(Scene):
    def construct(self):
        # Define vectors A and B
        plane = NumberPlane(y_range=(-9,9))
        self.add(plane)
        vector_A = Vector([2, 0], color=BLUE)
        vector_B = Vector([3, -1], color=GREEN)

        # Calculate projections
        projection_A_onto_B = np.dot(vector_A.get_vector(), vector_B.get_vector())/(np.dot(vector_B.get_vector(),vector_B.get_vector())) * vector_B.get_vector()
        projection_B_onto_A = np.dot(vector_B.get_vector(), vector_A.get_vector())/(np.dot(vector_A.get_vector(),vector_A.get_vector())) * vector_A.get_vector()

        # Create vector representations of the projections
        proj_vector_A_onto_B = Vector(projection_A_onto_B, color=RED)
        proj_vector_B_onto_A = Vector(projection_B_onto_A, color=YELLOW)

        # Display vectors A and B
        self.play(Create(vector_A), Create(vector_B))

        # Display projections and labels
        self.play(Create(proj_vector_A_onto_B), Create(proj_vector_B_onto_A))
        projection_A_label = MathTex("A_{\\text{proj onto B}}")
        projection_B_label = MathTex("B_{\\text{proj onto A}}")
        projection_A_label.next_to(proj_vector_A_onto_B, LEFT)
        projection_B_label.next_to(proj_vector_B_onto_A, RIGHT)
        self.play(Write(projection_A_label), Write(projection_B_label))
        def update_projA(proj_vector_A_onto_B):
            projection_A_onto_B = np.dot(vector_A.get_vector(), vector_B.get_vector())/(np.dot(vector_B.get_vector(),vector_B.get_vector())) * vector_B.get_vector()
            proj_vector_A_onto_B.become(Vector(projection_A_onto_B, color=RED))
            projection_A_label.next_to(proj_vector_A_onto_B, LEFT)

        def update_projB(proj_vector_B_onto_A):
            projection_B_onto_A = np.dot(vector_B.get_vector(), vector_A.get_vector())/(np.dot(vector_A.get_vector(),vector_A.get_vector())) * vector_A.get_vector()
            proj_vector_B_onto_A.become(Vector(projection_B_onto_A, color=YELLOW))
            projection_B_label.next_to(proj_vector_B_onto_A, RIGHT)


        # Animate the change in angle and projections
        for angle in range(0, 181, 5):  # Change angle in steps of 5 degrees
            angle_in_radians = angle * DEGREES
            self.play(
                Rotate(vector_A, angle_in_radians - vector_A.get_angle(), about_point=ORIGIN),
                UpdateFromFunc(proj_vector_A_onto_B, update_projA),
                UpdateFromFunc(proj_vector_B_onto_A, update_projB)
                # Rotate(vector_B, angle_in_radians - vector_B.get_angle(), about_point=ORIGIN)
                
                
            )
      
            self.wait(0.1)  # Add a short pause for each step

        self.wait(2)  # Add a final pause

class ThreeDVectorProjection(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(0.5)
        # Define 3D vectors
        vector_A = Vector(np.array([2, 1, 2]), color=BLUE)
        vector_B = Vector(np.array([3, -1, 1]), color=GREEN)
        self.play(Create(vector_A),Create(vector_B))
        parallelogram = Polygon(vector_A.get_start(), vector_A.get_end(), vector_A.get_end() + vector_B.get_end(), vector_B.get_end(), fill_opacity=0.5, fill_color=RED)
        self.play(Create(parallelogram))
        self.wait(1.5)
        vecA_xy = Vector(np.array([vector_A.get_end()[0], vector_A.get_end()[1], 0]), color=BLUE)
        vecB_xy = Vector(np.array([vector_B.get_end()[0], vector_B.get_end()[1], 0]), color=GREEN)

        parall_xy = Polygon(vecA_xy.get_start(), vecA_xy.get_end(), vecA_xy.get_end() + vecB_xy.get_end(), vecB_xy.get_end(), fill_opacity=0.5, fill_color=BLUE)

        vecA_yz = Vector(np.array([0, vector_A.get_end()[1], vector_A.get_end()[2]]), color=BLUE)
        VecB_yz = Vector(np.array([0, vector_B.get_end()[1], vector_B.get_end()[2]]), color=GREEN)

        parallel_yz = Polygon(vecA_yz.get_start(), vecA_yz.get_end(), vecA_yz.get_end() + VecB_yz.get_end(), VecB_yz.get_end(), fill_opacity=0.5, fill_color=BLUE)

        vexA_xz = Vector(np.array([vector_A.get_end()[0], 0, vector_A.get_end()[2]]), color=BLUE)
        vecB_xz = Vector(np.array([vector_B.get_end()[0], 0, vector_B.get_end()[2]]), color=GREEN)

        parallel_xz = Polygon(vexA_xz.get_start(), vexA_xz.get_end(), vexA_xz.get_end() + vecB_xz.get_end(), vecB_xz.get_end(), fill_opacity=0.5, fill_color=BLUE)

        self.play(Create(parall_xy), Create(parallel_yz), Create(parallel_xz))
        self.wait(25)


