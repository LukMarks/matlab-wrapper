import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel


class Plotter:

    @classmethod
    def line_plot(cls, time_series:list[int|float], result_series:[list[int|float]],
                  legend:dict=None, titles:dict=None) -> [plt.figure, plt.plot]:

        fig, chart = plt.subplot()
        chart.plot(time_series, result_series)

        chart.set(xlabel=titles.get("xlabel"), ylabel = titles.get("ylabel"),
                  title = titles.get("plotTitle"))

        chart.grid()

        return fig, chart

    @classmethod
    def show_all_plot(cls):
        plt.show()