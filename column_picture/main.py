from manim import *
class MatA(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[0, -1], 
                  [1, 0]]
        matrix_tex = MathTex("A = \\begin{bmatrix}0&-1 \\\\ 1&0\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        vect = self.get_vector([1,-2], color = PURPLE_A)
        self.add_transformable_mobject(vect,unit_square)
        self.add(matrix_tex)
        # self.wait()
        self.apply_matrix(matrix)
        self.wait()

class MatB(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[2, 0], 
                  [0, 2]]
        matrix_tex = MathTex("B = \\begin{bmatrix}2&0 \\\\ 0&2\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        vect = self.get_vector([1,-2], color = PURPLE_A)
        self.add_transformable_mobject(vect,unit_square)
        self.add(matrix_tex)
        # self.wait()
        self.apply_matrix(matrix)
        self.wait()

class MatC(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, 1], 
                  [0, 1]]
        matrix_tex = MathTex("C = \\begin{bmatrix}1&1 \\\\ 0&1\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        vect = self.get_vector([1,-2], color = PURPLE_A)
        self.add_transformable_mobject(vect,unit_square)
        self.add(matrix_tex)
        # self.wait()
        self.apply_matrix(matrix)
        self.wait()

class MatD(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, -1], 
                  [-1, 1]]
        matrix_tex = MathTex("D = \\begin{bmatrix}1&-1 \\\\ -1&1\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        vect = self.get_vector([1,-2], color = PURPLE_A)
        self.add_transformable_mobject(vect,unit_square)
        self.add(matrix_tex)
        # self.wait()
        self.apply_matrix(matrix)
        self.wait()

class MatE(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[0, -2], 
                  [2, 0]]
        # matrix_tex = MathTex("E = \\begin{bmatrix}0&-2 \\\\ -2&0\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        vect = self.get_vector([1,-2], color = PURPLE_A)
        self.add_transformable_mobject(vect,unit_square)
        # self.add(matrix_tex)
        # self.wait()
        self.apply_matrix(matrix)
        self.wait()
