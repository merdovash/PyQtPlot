from PyQt5.QtWidgets import QApplication

from PyQtPlot._Base import _AbstractGraphicView, _Line


class PlotWidget(_AbstractGraphicView):
    plot_type = _Line

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)


if __name__ == '__main__':
    import sys
    from random import randint

    app = QApplication(sys.argv)

    w = PlotWidget()
    w.add_plot({x: pow(x, 1.2) for x in range(20)}, 'x^1.2')
    w.add_plot({x: pow(x, 0.8) for x in range(70)}, 'x^0.8')
    w.add_plot({x: randint(0,x//2) for x in range(70)}, 'random')
    w.set_tooltip_func(lambda x, y, name: f"{name}")
    w.show()

    sys.exit(app.exec_())
