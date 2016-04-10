# status
#               1:pre_test
#               2:under test
#               3:after_test


class Test(object):
    def __init__(self, pre_test, under_test, after_test):
        self.pre_test = pre_test
        self.under_test = under_test
        self.after_test = after_test
        self.status = 1


def test_dic_init():
    test_dic = {}
    pre_after_test = [0, 0, 32, 1.57, 1.000, 1.000, 5.28, 179, 1.728, 1.000]
    under_test = [25, 5.88, 2.507, 5.829, 6.206, 9.869, 3.359, 4.605, 8.36, 3.863]
    for i in range(10):
        test_dic[i] = Test(pre_after_test[i], under_test[i], pre_after_test[i])
    return test_dic
