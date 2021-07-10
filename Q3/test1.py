import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.date_range(end='2016-03-31', periods=250, freq='D')

np.random.seed([3, 1415])
ranges = pd.DataFrame((np.random.choice(range(100), (2, 10)) +
                       np.array([[0], [150]])),
                      columns=list('ABCDEFGHIJ'))

df = pd.DataFrame(index=ts)
count = 1
for i, c in ranges.iteritems():
    s, e = c
    df.loc[ts[s]:ts[e], i] = count
    count += 1

df.plot()
plt.show()