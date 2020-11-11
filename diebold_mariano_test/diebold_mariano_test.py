import math

from scipy.stats import norm
from scipy.stats import t


def MSE(T, ori_list, alg_list):
    """
    使用 MSE 作为误差函数。
    :param T: 在计算 g(e{it}) 时的求和上标T
    :param ori_list: 原始时间序列
    :param alg_list: 要比较的的算法
    :return: 返回 g(e{it})
    """
    # ret = 0
    # for t in range(T):
    #     ret += pow((alg_list[t] - ori_list[t]), 2)

    # for t in range(T):
    ret = pow((alg_list[T - 1] - ori_list[T - 1]), 2)
    return ret


def MAE(T, ori_list, alg_list):
    """
    使用 MAE 作为误差函数。
    :param T: 在计算 g(e{it}) 时的求和上标T
    :param ori_list: 原始时间序列
    :param alg_list: 要比较的的算法
    :return: 返回 g(e{it})
    """
    # ret = 0
    # for t in range(T):
    ret = abs((alg_list[T-1] - ori_list[T-1]))
    return ret


def cul_d_t(method, ori_list, alg1_list, alg2_list):
    """
    计算d_t.
    :param method: 待使用的误差函数公式
    :param ori_list: 原始时间序列。
    :param alg1_list: 预测算法一的预测结果。
    :param alg2_list: 预测算法二的预测结果。
    :return:  d_t 列表
    """
    d_t_list = []
    if len(ori_list) != len(alg1_list) or len(ori_list) != len(alg2_list):
        raise Exception('The lengths of the three inputs do not match')
    if len(ori_list) == 0:
        raise Exception('The length of the input list should be more than 0')
    list_len = len(ori_list)
    for t in range(1, list_len + 1):
        temp = method(t, ori_list, alg1_list) - method(t, ori_list, alg2_list)
        d_t_list.append(temp)
    return d_t_list


def cul_overline_d(d_t_list):
    """
    计算 d_t 的加和平均，即 overline_d.
    :param d_t_list: d_t 列表
    :return: overline_d
    """
    return sum(d_t_list) / len(d_t_list)


def autocovariance(Xi, N, Xs):
    autoCov = 0
    T = float(N)
    for i in range(0, T):
        autoCov += ((Xi[i]) - Xs) * (Xi[i] - Xs)
    return (1 / (T)) * autoCov


def cul_widehat_gamma_d_tau_list(d_t_list):
    """
    计算 widehat_gamma_d_tau 列表。
    # :param tau: 大于0，小于时间序列长度的数
    :param d_t_list: d_t 列表
    :return: widehat_gamma_d_tau 列表
    """
    widehat_gamma_d_tau_list = []
    overline_d = cul_overline_d(d_t_list)
    for tau in range(len(d_t_list)):
        temp = 0.0
        for t in range(tau, len(d_t_list)):
            temp += (d_t_list[t] - overline_d) * (d_t_list[t - tau] - overline_d)
        widehat_gamma_d_tau_list.append(temp / len(d_t_list))
    # temp = 0
    # for lag in range(0):
    #     widehat_gamma_d_tau_list.append(autocovariance(d_t_list, len(d_t_list), lag, overline_d))
    # widehat_gamma_d_tau_list.append(temp / len(d_t_list))
    return widehat_gamma_d_tau_list


def cul_DM(d_t_list):
    """
    计算 DM 检验的结果。
    :param tau: 大于0，小于时间序列长度的数
    :param d_t_list: d_t 列表
    :return: DM 检验的结果
    """
    T = len(d_t_list)
    widehat_gamma_d_tau_list = cul_widehat_gamma_d_tau_list(d_t_list)
    temp = widehat_gamma_d_tau_list[0]
    # temp = (widehat_gamma_d_tau_list[0] + 2 * sum(widehat_gamma_d_tau_list[1:])) / T
    # k = len(widehat_gamma_d_tau_list) - 2  # S(T) = k-1 =T-2
    # temp = widehat_gamma_d_tau_list[0]  # 2 * pi * widehat_f_d_0
    # for tau in range(1, k + 1):
    #     if abs(tau + 1 / k):
    #         temp += 2 * widehat_gamma_d_tau_list[tau]
    overline_d = cul_overline_d(d_t_list)
    DM = overline_d /math.sqrt((temp)/T)
    # DM = 1 / math.sqrt(temp) * overline_d
    # harvey_adj = ((T + 1 - 2 * tau + tau * (tau - 1) / T) / T) ** (0.5)
    # DM = DM * harvey_adj
    # DM = overline_d / math.sqrt(temp / len(widehat_gamma_d_tau_list))
    return DM


def cul_P(d_t_list):
    """
    计算 DM 检验结果的相伴 P 值。
    :param d_t_list: d_t 列表
    :return: 相伴 P 值
    """
    DM = cul_DM(d_t_list)
    return 2 * t.cdf(-abs(DM), df=len(d_t_list) - 1)


if __name__ == '__main__':
    ori_list = [3, 5, 4, 1]
    a1_list = [2, 3, 4, 2]
    a2_list = [3, 2, 2, 4]
    d_t_list = cul_d_t(MAE, ori_list, a1_list, a2_list)
    # # print(d_t_list)
    # print(cul_widehat_gamma_d_tau_list(d_t_list))
    print("Original Data:")
    print(ori_list)
    print("Prediction Algorithm 1:")
    print(a1_list)
    print("Prediction Algorithm 2:")
    print(a2_list)
    print("#######################")
    print("DM: "+str(cul_DM(d_t_list)))
    print("P: "+str(cul_P(d_t_list)))
