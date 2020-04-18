import pandas as pd

pd.options.display.html.table_schema = True
pd.options.display.max_rows = None


iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df1 = pd.read_csv(iris_url)

df1

import matplotlib
matplotlib.use('Qt5Agg')
# This should be done before `import matplotlib.pyplot`
# 'Qt4Agg' for PyQt4 or PySide, 'Qt5Agg' for PyQt5
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))
plt.show()
