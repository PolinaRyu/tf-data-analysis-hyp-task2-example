import pandas as pd
import numpy as np
from scipy import stats

chat_id = 503882767 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    if stats.kstest(y,x).pvalue < 0.06:
        flag = True
    else:
        flag = False
    
    return flag
