import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd              
import pandas_datareader.data as web
import pprint
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm 


def plot_price_series(df, ts1, ts2):
    months = mdates.MonthLocator()
    fig, ax = plt.subplots()
    ax.plot(df.index, df[ts1], label=ts1)
    ax.plot(df.index, df[ts2], label=ts2)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.set_xlim(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 11, 1))
    ax.grid(True)
    fig.autofmt_xdate()

    plt.xlabel("Month/Year")
    plt.ylabel("Price ($)")
    plt.title("%s and %s Daily Prices" % (ts1, ts2))
    plt.legend()
    plt.show()


def plot_scatter_series(df, ts1, ts2):
    plt.xlabel("%s Price ($)" % ts1)
    plt.ylabel("%s Price ($)" % ts2)
    plt.title("%s and %s Price Scatterplot" % (ts1, ts2))
    plt.scatter(df[ts1], df[ts2])
    plt.show()


def plot_residuals(df):
    months = mdates.MonthLocator()
    fig, ax = plt.subplots()
    ax.plot(df.index, df["res"], label="Residuals")
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.set_xlim(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 11, 1))
    ax.grid(True)
    fig.autofmt_xdate()

    plt.xlabel("Month/Year")
    plt.ylabel("Price ($)")
    plt.title("Residual Plot")
    plt.legend()

    plt.plot(df["res"])
    plt.show()


if __name__ == "__main__":
    start = datetime.datetime(2021, 1, 1)
    end = datetime.datetime(2021, 11, 1)

    XOM = web.DataReader("XOM", "yahoo", start, end)
    CVX = web.DataReader("CVX", "yahoo", start, end)

    df = pd.DataFrame(index=XOM.index)
    df["XOM"] = XOM["Adj Close"]
    df["CVX"] = CVX["Adj Close"]

    plot_price_series(df, "XOM", "CVX")

    plot_scatter_series(df, "XOM", "CVX")

    res = sm.OLS(endog=df["CVX"], exog=df["XOM"]).fit()
    df["res"] = res.resid

    plot_residuals(df)

    cadf = ts.adfuller(df["res"])
    pprint.pprint(cadf)
