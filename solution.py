import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 775883383 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt

    SE = np.sqrt((p_control * (1 - p_control) / x_cnt) + (p_test * (1 - p_test) / y_cnt))
    Z = (p_test - p_control) / SE

    alpha = 0.02
    z_critical = norm.ppf(1 - alpha / 2)

    return abs(Z) > z_critical # Ваш ответ, True или False
