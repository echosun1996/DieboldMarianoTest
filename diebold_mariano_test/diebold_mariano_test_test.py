import unittest

from .diebold_mariano_test import *


class diebold_mariano_test_test(unittest.TestCase):
    ori_list = [3, 5, 4, 1]
    a1_list = [2, 3, 4, 2]
    a2_list = [3, 2, 2, 4]

    def test_cul_dt(self):
        d_t_list = cul_d_t(MSE, self.ori_list, self.a1_list, self.a2_list)
        right_list = [1, -4, -8, -16]
        self.assertEqual(d_t_list, right_list)

    def test_cul_overline_d(self):
        d_t_list = cul_d_t(MSE, self.ori_list, self.a1_list, self.a2_list)
        overline_d = cul_overline_d(d_t_list)
        right_result = -6.75
        self.assertEqual(overline_d, right_result)

    def test_cul_widehat_gamma_d_tau_list(self):
        d_t_list = cul_d_t(MSE, self.ori_list, self.a1_list, self.a2_list)
        widehat_gamma_d_tau_list = cul_widehat_gamma_d_tau_list(d_t_list)
        right_list = [38.6875, 7.359375, -8.78125, -17.921875]
        self.assertEqual(widehat_gamma_d_tau_list, right_list)

    def test_cul_DM(self):
        d_t_list = cul_d_t(MSE, self.ori_list, self.a1_list, self.a2_list)
        DM = cul_DM(d_t_list)
        right_result = -2.4688535993934706
        self.assertEqual(DM, right_result)

    def test_cul_P(self):
        d_t_list = cul_d_t(MSE, self.ori_list, self.a1_list, self.a2_list)
        P = cul_P(d_t_list)
        right_result = 0.09015604507899912
        self.assertEqual(P, right_result)

    def test_cul_P_MAE(self):
        d_t_list = cul_d_t(MAE, self.ori_list, self.a1_list, self.a2_list)
        P = cul_P(d_t_list)
        right_result = 0.2009762261989219
        self.assertEqual(P, right_result)
