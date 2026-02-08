import matplotlib.pyplot as plt
import seaborn as sns

def line_plot(series, title, path):
    plt.figure(figsize=(10,5))
    series.plot()
    plt.title(title)
    plt.savefig(path)
    plt.close()

def bar_plot(series, title, path):
    series.plot(kind='bar')
    plt.title(title)
    plt.savefig(path)
    plt.close()
