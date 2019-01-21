import sys
from collections import Counter
from random import randint

from PyQt5.QtWidgets import QApplication

from PyQtPlot.BarWidget import QBarGraphWidget


class Histogram(QBarGraphWidget):
    def __init__(self, data, flags=None, *args, **kwargs):
        counter = None
        if data is not None:
            counter = Counter(data)

        super().__init__(counter, flags=flags, *args, **kwargs)

    def add_plot(self, data, name="", color=None):
        counter = Counter(data)
        bars = list(range(min(counter.keys()), max(counter.keys())))
        heights = []
        for i in bars:
            if i in counter.keys():
                heights.append(counter[i])
            else:
                heights.append(0)

        super().add_plot({bars[i]: heights[i] for i in range(len(bars))}, name, color)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    hist = Histogram([randint(1980, 2014) for _ in range(randint(200, 500))], name="1")

    hist.horizontal_ax.set_ticks(list(range(1980, 2018)))
    hist.horizontal_ax.set_tick_margin(20)
    hist.horizontal_ax.set_tick_rotation(30)
    # hist.add_plot([randint(1995, 2014) for _ in range(randint(200, 500))], name="2")
    # hist.add_plot([randint(1995, 2014) for _ in range(randint(200, 500))], name="3")
    hist.horizontal_ax.set_label("Год")
    hist.vertical_ax.set_label("Количество")
    hist.set_tooltip_func(lambda x, y, plot_name: f"Количество: {y}\nГод: {x}\nГрафик: {plot_name}")

    hist.show()

    sys.exit(app.exec_())
