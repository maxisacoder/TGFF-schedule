#test_status    0:not tested
#               1:tested

#type           0:breakable
#               1:not breakable


class Core(object):
    def __init__(self, core_id, type=0):
        self.core_id = core_id
        self.task_list = []
        # self.task_len = 0
        self.status = None
        self.test_status = 0
        self.type = type
        self.test = None
