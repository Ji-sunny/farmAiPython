from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import math
from dbmodule import dbModule

oracle_db = dbModule.Database()


# 단순회귀분석
def simple_reg(table_name, col_X, col_y, pred_cols_X):
    data = oracle_db.read_data_all(table_name)
    X = data[col_X]
    y = data[col_y]

    result = stats.linregress(X,y)

    pvalue = result.pvalue

    return scores, pred_result, pvalue


# 다중회귀분석
def multi_reg(table_name, cols_X, col_y, pred_cols_X):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

    # 모형 학습
    model = LinearRegression()
    model.fit(train_X, train_y)


    # 입력받은 데이터값의 예측 결과값
    pred_cols_X = pd.dataFrame(pred_cols_X, columns=cols_X)
    pred_col_y = model.predict(pred_cols_X)

    pred_result = []
    for i, pred in enumerate(pred_col_y):
        a = {"data": "data"+i, col_y: pred}
        pred_result.append(a)

    # 모형 평가
    # 결정계수
    r2_score = model.score(train_X, train_y)
    # rmse
    rmse = math.sqrt(mean_squared_error(train_y, model.predict(train_X)))
    # 상관계수
    cor = test_y.corr(pred_col_y)

    return pred_result, r2_score, rmse, cor


# 포뮬러
def formula_reg():


    return scores, pred_result



#r