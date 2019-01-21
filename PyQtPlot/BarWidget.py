from typing import List, Dict

from PyQt5.QtGui import QColor

from PyQtPlot._Base import _Bar, _AbstractGraphicView

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class QBarGraphWidget(_AbstractGraphicView):
    _default_plot_size = 0.8
    plot_type = _Bar

    def __init__(self, data=None, flags=None, *args, **kwargs):
        _AbstractGraphicView.__init__(self, flags, *args, **kwargs)
        if data is not None:
            self.add_plot(data, kwargs.get('name'), color=kwargs.get('color', None))

        # if len(heights):
        #     self.vertical_ax.set_ticks(range(0, max(heights) + 1, max(int(max(heights) / 20), 1)))
        # else:
        #     self.vertical_ax.set_ticks([0, 1])
        #
        # self.horizontal_ax.set_ticks(bars)

    def add_plot(self, plot: Dict[int, int], name: str, color: QColor = None):
        color = self._define_color(color)
        self.plots[name] = _Bar(plot, name, self, color=color)

        plots: List[_Bar] = list(self.plots.values())
        for index, p in enumerate(plots):
            p.set_nested_width(p.real_width() / len(plots))
            if index > 0:
                p.set_offset(sum(map(lambda x: x.width(), plots[:index])))
