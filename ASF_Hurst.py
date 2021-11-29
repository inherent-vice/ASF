from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn
import pandas as pd

data_csv = "C:/Devs/ASF/GOOG.csv"


def create_dataframe(data_csv):
    goog = pd.read_csv(data_csv, index_col="Date")
    goog.index = pd.to_datetime(goog.index)
    return goog


def hurst(ts):
    lags = range(2, 100)
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]
    poly = polyfit(log(lags), log(tau), 1)
    return poly[0] * 2.0


gbm = log(cumsum(randn(100000)) + 1000)
mr = log(randn(100000) + 1000)
tr = log(cumsum(randn(100000) + 1) + 1000)

print("Hurst(GBM):   %s" % hurst(gbm))
print("Hurst(MR):    %s" % hurst(mr))
print("Hurst(TR):    %s" % hurst(tr))

goog = create_dataframe(data_csv)
print("Hurst(GOOG):  %s" % hurst(goog["Adj Close"].values))
