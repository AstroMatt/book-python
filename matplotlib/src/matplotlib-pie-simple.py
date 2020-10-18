import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, values):
    absolute = int(pct / 100. * np.sum(values))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, auto_texts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                   textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(auto_texts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()
