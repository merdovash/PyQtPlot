import sys
from collections import defaultdict
from random import randint
from typing import Dict, List

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

from PyQtPlot.BarWidget import QBarGraphWidget
from PyQtPlot._Base import _Bar


class QStackedBarWidget(QBarGraphWidget):
    def add_plot(self, plot: Dict[int, int], name: str, color: QColor = None):
        color = self._define_color(color)
        self.plots[name] = _Bar(plot, name, self, color=color, stacked=True)

        summer = defaultdict(int)
        for name in self.plots:
            for key, value in self.plots[name].data.items():
                summer[key] += value

        self.vertical_ax.set_ticks(range(0, max(summer.values())))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    sbw = QStackedBarWidget()
    sbw.add_plot({year: randint(0, 10) for year in range(1999, 2018)}, name='ok')
    sbw.add_plot({year: randint(0, 10) for year in range(1999, 2018)}, name='old')
    sbw.add_plot({year: randint(0, 10) for year in range(1999, 2018)}, name='missing')
    sbw.horizontal_ax.set_ticks(range(1999, 2018))
    sbw.set_tooltip_func(lambda x, y, name: f'{name}: x={x}, y={y}')
    sbw.show()

    sys.exit(app.exec_())
