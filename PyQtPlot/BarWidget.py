from typing import List, Dict

from PyQt5.QtGui import QColor

from PyQtPlot._Base import _Plot, _AbstractGraphicView

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class QBarGraphWidget(_AbstractGraphicView):
    _default_plot_size = 0.8

    def __init__(self, bars, heights, flags, name="", *args, **kwargs):
        assert len(bars) == len(heights)
        _AbstractGraphicView.__init__(self, flags, *args, **kwargs)

        self.bars = bars
        self.heights = heights

        self.add_plot({bars[i]: heights[i] for i in range(len(bars))}, name, color=kwargs.get('color', None))

        # if len(heights):
        #     self.vertical_ax.set_ticks(range(0, max(heights) + 1, max(int(max(heights) / 20), 1)))
        # else:
        #     self.vertical_ax.set_ticks([0, 1])
        #
        # self.horizontal_ax.set_ticks(bars)

    def add_plot(self, plot: Dict[int, int], name: str, color: QColor = None):
        color = self._define_color(color)
        self.plots[name] = _Plot(plot, name, self, color=color)

        plots: List[_Plot] = list(self.plots.values())
        for index, p in enumerate(plots):
            p.set_nested_width(p.real_width() / len(plots))
            if index > 0:
                p.set_offset(sum(map(lambda x: x.width(), plots[:index])))
