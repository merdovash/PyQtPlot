import sys
from math import sqrt

from PyQt5.QtWidgets import QApplication

from PyQtPlot._Base import _AbstractGraphicView, _Scatter


class QScatter(_AbstractGraphicView):
    _default_plot_size = 8

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

    def add_plot(self, data, name, color=None):
        self.plots[name] = _Scatter(data, name, self, color=self._define_color(color))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QScatter()
    w.grid.show_horizontal(True)
    w.add_plot([x * x for x in range(10)], 'first')
    w.add_plot([sqrt(x) for x in range(25)], 'second')
    # w.vertical_ax.set_ticks(range(25))
    # w.horizontal_ax.set_ticks(range(25))
    w.set_tooltip_func(lambda y, x, name: f"{name}: ({round(x, 2)}, {round(y, 2)})")
    w.show()

    sys.exit(app.exec_())
