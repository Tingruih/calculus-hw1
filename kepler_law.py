import numpy as np

def period_vs_distance_fit(distances, periods):

    # 將距離和週期資料取對數，轉換為線性模型
    log_distances = np.log(distances)
    log_periods = np.log(periods)
    
    # 使用 polyfit 對線性模型進行擬合，得到 [b, log(a)]
    # 在 log-log 空間中，b 是斜率，log(a) 是截距
    params = np.polyfit(log_distances, log_periods, 1)
    
    # 從擬合結果中提取參數
    b = params[0]  # 斜率即為指數 b
    log_a = params[1]  # 截距為 log(a)
    
    # 從 log(a) 計算 a 值
    a = np.exp(log_a)

    return a, b  
