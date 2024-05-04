from tkinter import *
from tkinter import ttk
from lines import DDA
from lines import Bresenham
from lines import Wu

from rectangle.EBresenham import EBresenham
from rectangle.Hyperbola import draw_hyperbola
from rectangle.Parabola import plot_parabola

from curve.hermite import hermite_curve
from curve.bezier import bezier
from curve.b_spline import b_spline


window = Tk()
window.title("Graphical Editor")
window.geometry("800x860")

buttons_frame = Frame(window)
buttons_frame.grid(row=1, column=0)
canvas = Canvas(window, width=800, height=500, background="white")
canvas.grid(row=0, column=0)

clear_canvas_button = Button(buttons_frame, text="Clear canvas")
clear_canvas_button.grid(row=3, column=0)

vector_frame = Frame(window, pady=5)
vector_frame.grid(row=3, column=0)

x_1_label = Label(vector_frame, text="x_1")
x_1_label.grid(row=0, column=0)
x_1_text = Text(vector_frame, height=1, width=4)
x_1_text.grid(row=0, column=1)

y_1_label = Label(vector_frame, text="y_1")
y_1_label.grid(row=0, column=2)
y_1_text = Text(vector_frame, height=1, width=4)
y_1_text.grid(row=0, column=3)

x_2_label = Label(vector_frame, text="x_2")
x_2_label.grid(row=1, column=0)
x_2_text = Text(vector_frame, height=1, width=4)
x_2_text.grid(row=1, column=1)

y_2_label = Label(vector_frame, text="y_2")
y_2_label.grid(row=1, column=2)
y_2_text = Text(vector_frame, height=1, width=4)
y_2_text.grid(row=1, column=3)


selected_option = StringVar(value="line")

radiobutton_frame = Frame(buttons_frame)
radiobutton_frame.grid(row=1, column=0)

line_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Line", value="line")
circle_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Circle", value="circle")
parabola_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Parabola", value="parabola")
hyperbola_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Hyperbola", value="hyperbola")
curve_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Curve", value="Curve")

circle_radiobutton.grid(row=0, column=1)
line_radiobutton.grid(row=0, column=0)
parabola_radiobutton.grid(row=0, column=2)
hyperbola_radiobutton.grid(row=0, column=3)
curve_radiobutton.grid(row=0, column=4)
figure_frame = Frame(buttons_frame)
figure_frame.grid(row=2, column=0)
line_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
line_frame.grid(row=0, column=0, padx=2, pady=2)
line_label = Label(line_frame, text="Lines", font="Arial")
line_label.grid()
algorithms = ["DDA", "Bresenham", "Wu's line algorithm"]
line_box = ttk.Combobox(line_frame, values=algorithms, state="readonly")
line_box.current(0)
line_box.grid()
circle_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
circle_frame.grid(row=0, column=1, padx=2, pady=2)
circle_label = Label(circle_frame, text="Ellipse", font='Arial')
circle_label.grid()
circle_box = ttk.Combobox(circle_frame, values=['Bresenham', 'Circle'], state="readonly")
circle_box.current(0)
circle_box.grid()
parabola_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
parabola_frame.grid(row=0, column=2, padx=2, pady=2)
parabola_label = Label(parabola_frame, text="Parabola", font='Arial')
parabola_label.grid()
parabola_box = ttk.Combobox(parabola_frame, values=['Bresenham'], state="readonly")
parabola_box.current(0)
parabola_box.grid()
hyperbola_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
hyperbola_frame.grid(row=0, column=3, padx=2, pady=2)
hyperbola_label = Label(hyperbola_frame, text="Hyperbola", font='Arial')
hyperbola_label.grid()
hyperbola_box = ttk.Combobox(hyperbola_frame, values=['Bresenham'], state="readonly")
hyperbola_box.current(0)
hyperbola_box.grid()
curve_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
curve_frame.grid(row=0, column=4, padx=2, pady=2)
curve_label = Label(curve_frame, text="Curve", font="Arial")
curve_label.grid()
curve_box = ttk.Combobox(curve_frame, values=['Hermite', 'Bezier', 'B-spline'], state="readonly")
curve_box.current(0)
curve_box.grid()
draw = list()


def figure_click(event):

    if len(draw) == 2:
        draw.clear()

    draw.append(event)
    if len(draw) == 1:
        return
    if selected_option.get() == 'line':
        line_click(event)
    elif selected_option.get() == 'circle':
        circle_click(event)
    elif selected_option.get() == 'parabola':
        parabola_click(event)
    elif selected_option.get() == 'hyperbola':
        hyperbola_click(event)
    elif selected_option.get() in 'Curve':
        curve_click(event)


def curve_click(event):
    pixels = []
    if curve_box.get() == 'Hermite':
        pixels = hermite_curve(draw[0], draw[1],
                               (int(x_1_text.get("1.0", "end-1c")), int(y_1_text.get("1.0", "end-1c"))),
                               (int(x_2_text.get("1.0", "end-1c")), int(y_2_text.get("1.0", "end-1c"))))
    elif curve_box.get() == 'Bezier':
        pixels = bezier(draw[0], draw[1], (int(x_1_text.get("1.0", "end-1c")), int(y_1_text.get("1.0", "end-1c"))),
                        (int(x_2_text.get("1.0", "end-1c")), int(y_2_text.get("1.0", "end-1c"))))
    elif curve_box.get() =='B-spline':
        pixels = b_spline(draw[0], draw[1], (int(x_1_text.get("1.0", "end-1c")), int(y_1_text.get("1.0", "end-1c"))),
                        (int(x_2_text.get("1.0", "end-1c")), int(y_2_text.get("1.0", "end-1c"))))

    for i in pixels:
        canvas.create_rectangle(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")


def hyperbola_click(event):
    pixels = draw_hyperbola(draw[0], draw[1])

    for i in pixels:
        canvas.create_rectangle(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")


def parabola_click(event):
    pixels = plot_parabola(draw[0], draw[1])

    for i in pixels:
        canvas.create_rectangle(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")


def circle_click(event):
    if circle_box.get() == 'Circle':
        pixels = EBresenham(draw[0], draw[1], circle=True)
    else:
        pixels = EBresenham(draw[0], draw[1])

    for i in pixels:
        canvas.create_rectangle(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")


def line_click(event):
    points = list()
    if line_box.get() == "DDA":
        points = DDA.DDA(draw[0], draw[1])
    elif line_box.get() == "Bresenham":
        points = Bresenham.Bresenham(draw[0], draw[1])

    for i in points:
        canvas.create_rectangle(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")

    if line_box.get() == "Wu's line algorithm":
        points, additional, change_flag = Wu.Wu(draw[0], draw[1])
        s1 = 1 if points[-1][0] > points[0][0] else -1
        s2 = 1 if points[-1][1] > points[0][1] else -1

        k = (points[-1][1] - points[0][1]) / (points[-1][0] - points[0][0])
        b = points[-1][1] - points[-1][0] * k
        for i in range(len(points)):
            if change_flag:
                additional[i] = (
                    additional[i][0] - 10 * s1, additional[i][1], abs(points[i][0] * k + b - points[i][1]))
            else:
                additional[i] = (
                    additional[i][0], additional[i][1] - 10 * s2, abs(points[i][0] * k + b - points[i][1]))

        for i in range(len(points)):
            color_1 = "#%02x%02x%02x" % (
                abs(int(255 * additional[i][2])), abs(int(255 * additional[i][2])),
                abs(int(255 * additional[i][2])))

            color_2 = "#%02x%02x%02x" % (
                abs(int(255 * (1 - additional[i][2]))), abs(int(255 * (1 - additional[i][2]))),
                abs(int(255 * (1 - additional[i][2]))))

            canvas.create_rectangle(points[i][0], points[i][1], points[i][0] + 1, points[i][1] + 1, fill=color_1)
            canvas.create_rectangle(additional[i][0], additional[i][1], additional[i][0] + 1, additional[i][1] + 1,
                                    fill=color_2)


def clear_canvas(event):
    draw.clear()
    canvas.delete("all")

canvas.bind("<Button-1>", figure_click)
clear_canvas_button.bind("<Button-1>", clear_canvas)

window.mainloop()
