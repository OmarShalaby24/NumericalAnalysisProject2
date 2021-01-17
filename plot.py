import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.pyplot as plt


class plot:
    def __init__(self, list):
        self.list = list

    def hanging_line(self, point1, point2):

        a = (point2[1] - point1[1]) / (np.cosh(point2[0]) - np.cosh(point1[0]))
        b = point1[1] - a * np.cosh(point1[0])
        x = np.linspace(point1[0], point2[0], 100)
        y = a * np.cosh(x) + b

        return (x, y)

    def draw(self):

        cnt = 0
        while cnt < len(self.list):
            window = Tk()
            points = self.list[cnt]
            x_list = []
            y_list = []
            for point in points:
                x_list.append(point[0])
                y_list.append(point[1])

            fig = Figure(figsize=(10, 6), dpi=100)
            plot = fig.add_subplot(1, 1, 1)
            i = 0
            while i < len(points) - 1:
                x, y = self.hanging_line(points[i], points[i + 1])
                plot.plot(x, y)
                i = i + 1

            plot.plot(x_list, y_list, 'o')
            plot.set_title('Number of iterations for variable vs obtained root')
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.get_tk_widget().pack()
            cnt = cnt + 1
