from manim import *
import numpy as np

RECT_NUM = 100
EQP_TYPE = "center"


# Функция для вычисления интегральных сумм
def calculate_integral_sum_evenly(point_a, point_b, n, sum_type, int_func):
    equip = np.linspace(point_a, point_b, n + 1)  # Получение оснащения
    step_size = (point_b - point_a) / n  # Расчет шага
    if sum_type.lower() == "left":
        equip = equip[:-1]
    elif sum_type.lower() == "right":
        equip = equip[1:]
    elif sum_type.lower() == "center":
        equip = equip[:-1] + step_size / 2
    else:
        print("Invalid equipment type!")
        return 0
    return np.sum(int_func(equip)) * step_size


# Заданная функция
def func(x):
    return np.power(x, 3)


# Класс сцены для визуализации
class IntegralScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE # Установление фона
        # Задание параметров осей
        axes = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 1, 0.1],
            x_length=6,
            y_length=6,
            color=BLACK,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.1, 0.1),
                "font_size": 24,
                "color": BLACK,
            },
            tips=False,
        )
        axes.color = BLACK
        # self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.add(axes)

        # Построение графика
        func_graph = axes.plot(
            func,
            color=ORANGE,
        )
        func_label = axes.get_graph_label(func_graph, "y=x^3")
        self.add(func_label)
        # self.play(FadeIn(func_label, run_time=0.25))
        self.add(func_graph)
        # self.play(Write(func_graph, run_time=0.75))
        # self.wait(0.25)

        # Визуализация расчета площади
        riemann_rectangles = axes.get_riemann_rectangles(
            func_graph,
            dx=1 / RECT_NUM,
            fill_opacity=0.75,
            input_sample_type=EQP_TYPE,
            color=np.array([DARK_BLUE, GREEN_E]),
            stroke_width=0.25,
            stroke_color=WHITE
        )
        rect_num_txt = Tex(f"$N = {RECT_NUM}$", font_size=50, color=DARK_BLUE).align_on_border(LEFT)
        integral_sum = calculate_integral_sum_evenly(0, 1, RECT_NUM, EQP_TYPE, func)
        integral_sum_txt = Tex(f"$I = {round(integral_sum, 8)}$", font_size=50, color=GREEN_E).align_on_border(RIGHT)

        self.add(rect_num_txt)
        # self.play(Write(rect_num_txt, run_time=0.25))
        self.add(riemann_rectangles)
        # self.play(Write(riemann_rectangles, run_time=0.75))
        self.add(integral_sum_txt)
        # self.play(Write(integral_sum_txt, run_time=0.25))
        # self.wait(0.5)
