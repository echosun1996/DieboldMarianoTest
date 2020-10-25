import math

from scipy.stats import norm


def MSE(T, ori_list, alg_list):
    """
    使用 MSE 作为误差函数。
    :param T: 在计算 g(e{it}) 时的求和上标T
    :param ori_list: 原始时间序列
    :param alg_list: 要比较的的算法
    :return: 返回 g(e{it})
    """
    ret = 0
    for t in range(T):
        ret += pow((alg_list[t] - ori_list[t]), 2)
    return ret


def MAE(T, ori_list, alg_list):
    """
    使用 MAE 作为误差函数。
    :param T: 在计算 g(e{it}) 时的求和上标T
    :param ori_list: 原始时间序列
    :param alg_list: 要比较的的算法
    :return: 返回 g(e{it})
    """
    ret = 0
    for t in range(T):
        ret += abs((alg_list[t] - ori_list[t]))
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


def cul_widehat_gamma_d_tau_list(d_t_list):
    """
    计算 widehat_gamma_d_tau 列表。
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
    return widehat_gamma_d_tau_list


def cul_DM(d_t_list):
    """
    计算 DM 检验的结果。
    :param d_t_list: d_t 列表
    :return: DM 检验的结果
    """
    widehat_gamma_d_tau_list = cul_widehat_gamma_d_tau_list(d_t_list)
    k = len(widehat_gamma_d_tau_list) - 2  # S(T) = k-1 =T-2
    temp = widehat_gamma_d_tau_list[0]  # 2 * pi * widehat_f_d_0
    for tau in range(1, k + 1):
        if abs(tau + 1 / k):
            temp += 2 * widehat_gamma_d_tau_list[tau]

    overline_d = cul_overline_d(d_t_list)
    DM = overline_d / math.sqrt(temp / len(widehat_gamma_d_tau_list))
    return DM


def cul_P(d_t_list):
    """
    计算 DM 检验结果的相伴 P 值。
    :param d_t_list: d_t 列表
    :return: 相伴 P 值
    """
    DM = cul_DM(d_t_list)
    return 2 * (1 - norm.cdf(abs(DM)))
