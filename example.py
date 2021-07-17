from manimlib.imports import *


class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        triangle1=Polygon(np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1]))
        triangle2=Polygon(np.array([1, -1, 0]),np.array([0,1,0]),np.array([0,0,1]))
        invalid_polygon = [
                   (0, 0, 0),  # P1
                   (1, 1, 0),  # P2
                   (2, 0, 0),  # P3
                   (2, 1, 0),  # P4
                   (1, -1, 0),  # P5
                   (1, -1, 0)  # P6
                ]

        hexagon = Polygon(*invalid_polygon)
        #Showing shapes
        self.play(ShowCreation(circle))
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(hexagon))
        self.play(Transform(hexagon, triangle2))
        self.play(FadeOut(circle))


class PlotFunctions(GraphScene):
    # CONFIG = {
    #     "x_min": -10,
    #     "x_max": 10,
    #     "y_min": -1.5,
    #     "y_max": 1.5,
    #     # "graph_origin": ORIGIN,
    #     # "function_color": RED,
    #     # "axes_color": GREEN,
    #     # "x_labeled_nums": range(-10, 12, 2),
    #
    # }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(lambda x: np.sin(x))
        func_graph2 = self.get_graph(lambda x: np.cos(x))
        self.set_graph_label(func_graph, label="x^{2}")
        self.set_graph_label(func_graph2, label="x^{2}")
        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))