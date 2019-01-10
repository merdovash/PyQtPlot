import sys
from collections import Counter
from random import randint

from PyQtPlot.BarWidget import QBarGraphWidget
from PyQt5.QtWidgets import QApplication, QMainWindow


class Histogram(QBarGraphWidget):
    def __init__(self, data, name, flags, *args, **kwargs):
        counter = Counter(data)
        bars = list(range(min(counter.keys()), max(counter.keys())))
        heights = []
        for i in bars:
            if i in counter.keys():
                heights.append(counter[i])
            else:
                heights.append(0)

        super().__init__(bars, heights, name=name, flags=flags, *args, **kwargs)

    def add_plot(self, data, name=""):
        counter = Counter(data)
        bars = list(range(min(counter.keys()), max(counter.keys())))
        heights = []
        for i in bars:
            if i in counter.keys():
                heights.append(counter[i])
            else:
                heights.append(0)

        super().add_plot({bars[i]: heights[i] for i in range(len(bars))}, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    hist = Histogram([randint(1995, 2014) for _ in range(randint(20, 50))], name="1", flags=window)

    hist.horizontal_ax.set_ticks(list(range(1990, 2018)))
    hist.horizontal_ax.set_tick_margin(20)
    hist.horizontal_ax.set_tick_rotation(30)
    # hist.add_plot([randint(1995, 2014) for _ in range(randint(20, 50))], name="2")
    # hist.add_plot([randint(1995, 2014) for _ in range(randint(20, 50))], name="3")
    hist.horizontal_ax.set_label("Год")
    hist.vertical_ax.set_label("Количество")
    hist.set_tooltip_func(lambda value, index, plot_name: f"Количество: {value}\nГод: {index}\nГрафик: {plot_name}")

    window.setCentralWidget(hist)

    window.show()

    sys.exit(app.exec_())