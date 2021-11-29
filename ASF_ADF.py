import pandas as pd
import statsmodels.tsa.stattools as ts

# 오디오 채널로
def create_dataframe(data_csv):
    goog = pd.read_csv(data_csv, index_col="Date")
    goog.index = pd.to_datetime(goog.index)
    return goog


# TODO: 함수 이름 길이 줄이기
def augmented_dickey_fuller(goog):
    adf = ts.adfuller(goog["Adj Close"], 1)
    print(adf)


# 
if __name__ == "__main__":
    data_csv = "C:/Devs/ASF/GOOG.csv"
    goog_df = create_dataframe(data_csv)
    goog_adf = augmented_dickey_fuller(goog_df)
