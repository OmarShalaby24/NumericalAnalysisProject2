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

        print(self.list)
        point1 = [-0.64, 3.1]
        point2 = [1.87, 3.36]
        point3 = [4.45, 2.86]
        points = self.list[0]
        i = 0
        print(len(points))
        while i < len(points) - 1:
            x, y = self.hanging_line(points[i], points[i + 1])
            plt.plot(points[i][0], points[i][1], 'o')
            plt.plot(points[i + 1][0], points[i + 1][1], 'o')
            plt.plot(x, y)
            i = i + 1

        plt.show()

    def draw2(self):

        point1 = [-0.64, 3.1]
        point2 = [1.87, 3.36]
        point3 = [4.45, 2.86]
        cnt = 0
        points = self.list

        while cnt < len(self.list):
            window = Tk()
            # window=windwos[cnt]
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
                print("j")
                x, y = self.hanging_line(points[i], points[i + 1])
                plot.plot(x, y)
                i = i + 1

            plot.plot(x_list, y_list, 'o')

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.get_tk_widget().pack()
            window.mainloop()
            cnt = cnt + 1