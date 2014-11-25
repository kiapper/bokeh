import numpy as np
import pandas as pd

from bokeh.sampledata.iris import flowers
from bokeh.charts import Scatter

# we fill a df with the data of interest and create a groupby pandas object
df = flowers[["petal_length", "petal_width", "species"]]
xyvalues = g = df.groupby("species")

# here we only drop that groupby object into a dict ..
from collections import OrderedDict
pdict = OrderedDict()

for i in g.groups.keys():
    labels = g.get_group(i).columns
    xname = labels[0]
    yname = labels[1]
    x = getattr(g.get_group(i), xname)
    y = getattr(g.get_group(i), yname)
    pdict[i] = zip(x, y)

#xyvalues = pdict
#xyvalues = pd.DataFrame(xyvalues)
#xyvalues = xyvalues.values()
#xyvalues = np.array(xyvalues.values())

scatter = Scatter(xyvalues, filename="iris_scatter.html", ylabel='petal_width',  facet=False)
scatter.title("iris dataset, gp_by_input").legend("top_left").width(600).height(400).show()
