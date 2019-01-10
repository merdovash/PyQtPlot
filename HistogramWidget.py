from collections import Counter

from Client.MyQt.Widgets.Graph.BarWidget import QBarGraphWidget


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
