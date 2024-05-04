from tkinter import *
from tkinter import ttk

from curve.b_spline import b_spline
from curve.bezier import bezier
from curve.hermite import hermite_curve
from lines.Wu import Wu
from lines.Bresenham import Bresenham
from lines.DDA import DDA
from rectangle.EBresenham import EBresenham
from rectangle.Hyperbola import draw_hyperbola
from rectangle.Parabola import plot_parabola


def dda_algorithm(event_1, event_2):
    return DDA(event_1, event_2)


def bresenham_algorithm(event_1, event_2):
    return Bresenham(event_1, event_2)


def bresenham_circle_algorithm(event_1, event_2):
    return EBresenham(event_1, event_2)


def midpoint_circle_algorithm(event_1, event_2):
    return EBresenham(event_1, event_2, circle=True)


def bresenham_parabola_algorithm(event_1, event_2):
    return plot_parabola(event_1, event_2)


def bresenham_hyperbola_algorithm(event_1, event_2):
    return draw_hyperbola(event_1, event_2)


def hermite_algorithm(event_1, event_2):
    return hermite_curve(event_1, event_2, (int(x_1_text.get()), int(y_1_text.get())), (int(x_2_text.get()), int(y_2_text.get())))


def wu_algorithm(event_1, event_2):
    return Wu(event_1, event_2)


def bspline_algorithm(event_1, event_2):
    return b_spline(event_1, event_2, (int(x_1_text.get()), int(y_1_text.get())), (int(x_2_text.get()), int(y_2_text.get())))


def bezier_algorithm(event_1, event_2):
    return bezier(event_1, event_2, (int(x_1_text.get()), int(y_1_text.get())), (int(x_2_text.get()), int(y_2_text.get())))


def get_gray_color(transparency):
    gray_level = int(255 * transparency)
    color = f"#{gray_level:02X}{gray_level:02X}{gray_level:02X}"
    return color


def draw_figure(event):
    global event_1, event_2, first_click

    if first_click:
        print('Обрабатываем первый клик')
        event_1 = event
        first_click = False
    else:
        print('Обрабатываем второй клик')
        event_2 = event
        first_click = True

        selected_figure = figure_selection.get()
        algorithm = algorithm_box.get()

        points = []

        # Логика вызова соответствующего алгоритма для выбранной фигуры
        if selected_figure == "line":
            if algorithm == "DDA":
                points = dda_algorithm(event_1, event_2)
            elif algorithm == "Bresenham":
                points = bresenham_algorithm(event_1, event_2)
            elif algorithm == "Wu's line algorithm":
                points = wu_algorithm(event_1, event_2)
        elif selected_figure == "ellipse":
            if algorithm == "Bresenham":
                points = bresenham_circle_algorithm(event_1, event_2)
            elif algorithm == "Circle":
                points = midpoint_circle_algorithm(event_1, event_2)
        elif selected_figure == "parabola":
            if algorithm == "Bresenham":
                points = bresenham_parabola_algorithm(event_1, event_2)
        elif selected_figure == "hyperbola":
            if algorithm == "Bresenham":
                points = bresenham_hyperbola_algorithm(event_1, event_2)
        elif selected_figure == "curve":
            if algorithm == "Hermite":
                points = hermite_algorithm(event_1, event_2)
            elif algorithm == "Bezier":
                points = bezier_algorithm(event_1, event_2)
            elif algorithm == "B-spline":
                points = bspline_algorithm(event_1, event_2)

        # Отрисовка полученных точек на холсте
        for point in points:
            gray_color = get_gray_color(point[2])
            print(gray_color)
            canvas.create_rectangle(point[0], point[1], point[0]+1, point[1]+1, width=1, fill=gray_color, outline='')


def clear_canvas():
    canvas.delete("all")


def update_algorithms():
    selected_figure = figure_selection.get()
    if selected_figure == "line":
        algorithm_box["values"] = ["DDA", "Bresenham", "Wu's line algorithm"]
        algorithm_box.current(0)
    elif selected_figure == "ellipse":
        algorithm_box["values"] = ["Bresenham", "Cirlce"]
        algorithm_box.current(0)
    elif selected_figure == "parabola":
        algorithm_box["values"] = ["Bresenham"]
        algorithm_box.current(0)
    elif selected_figure == "hyperbola":
        algorithm_box["values"] = ["Bresenham"]
        algorithm_box.current(0)
    elif selected_figure == "curve":
        algorithm_box["values"] = ["Hermite", "Bezier", "B-spline"]
        algorithm_box.current(0)


root = Tk()
root.title("Vector Editor")

# Создание фреймов
buttons_frame = Frame(root)
buttons_frame.pack(side=TOP)

canvas_frame = Frame(root)
canvas_frame.pack(side=BOTTOM, expand=True, fill=BOTH)

figure_frame = Frame(buttons_frame)
figure_frame.grid(row=2, column=0)

line_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
line_frame.grid(row=0, column=0, padx=2, pady=2)

circle_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1, padx=2, pady=2)
circle_frame.grid(row=0, column=1)

parabola_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
parabola_frame.grid(row=0, column=2, padx=2, pady=2)

hyperbola_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
hyperbola_frame.grid(row=0, column=3, padx=2, pady=2)

curve_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
curve_frame.grid(row=0, column=4, padx=2, pady=2)

figure_selection = StringVar()

line_radiobutton = Radiobutton(line_frame, text="Line", variable=figure_selection, value="line", command=update_algorithms)
line_radiobutton.pack()
circle_radiobutton = Radiobutton(circle_frame, text="Ellipse", variable=figure_selection, value="ellipse", command=update_algorithms)
circle_radiobutton.pack()
parabola_radiobutton = Radiobutton(parabola_frame, text="Parabola", variable=figure_selection, value="parabola", command=update_algorithms)
parabola_radiobutton.pack()
hyperbola_radiobutton = Radiobutton(hyperbola_frame, text="Hyperbola", variable=figure_selection, value="hyperbola", command=update_algorithms)
hyperbola_radiobutton.pack()
curve_radiobutton = Radiobutton(curve_frame, text="Curve", variable=figure_selection, value="curve", command=update_algorithms)
curve_radiobutton.pack()

# Создание выпадающего списка для выбора алгоритма
algorithm_label = Label(buttons_frame, text="Algorithm:")
algorithm_label.grid(row=0, column=1, padx=5, pady=5)
algorithm_box = ttk.Combobox(buttons_frame, state="readonly")
algorithm_box.grid(row=0, column=2, padx=5, pady=5)

# Создание полей ввода для координат точек
x_1_label = Label(buttons_frame, text="X1:")
x_1_label.grid(row=1, column=0, padx=5, pady=5)
x_1_text = Text(buttons_frame, height=1, width=5)
x_1_text.grid(row=1, column=1, padx=5, pady=5)

y_1_label = Label(buttons_frame, text="Y1:")
y_1_label.grid(row=1, column=2, padx=5, pady=5)
y_1_text = Text(buttons_frame, height=1, width=5)
y_1_text.grid(row=1, column=3, padx=5, pady=5)

x_2_label = Label(buttons_frame, text="X2:")
x_2_label.grid(row=1, column=4, padx=5, pady=5)
x_2_text = Text(buttons_frame, height=1, width=5)
x_2_text.grid(row=1, column=5, padx=5, pady=5)

y_2_label = Label(buttons_frame, text="Y2:")
y_2_label.grid(row=1, column=6, padx=5, pady=5)
y_2_text = Text(buttons_frame, height=1, width=5)
y_2_text.grid(row=1, column=7, padx=5, pady=5)

# Создание кнопки для очистки холста
clear_button = Button(buttons_frame, text="Clear", command=clear_canvas)
clear_button.grid(row=1, column=8, padx=5, pady=5)

# Создание холста для рисования
canvas = Canvas(canvas_frame, bg="white")
canvas.pack(expand=True, fill=BOTH)
canvas.bind("<Button-1>", draw_figure)


# selected_option.trace("w", lambda *args: update_algorithms())
first_click = True
# Запуск основного цикла программы
root.mainloop()