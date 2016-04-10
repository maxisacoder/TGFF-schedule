from random import *


# class Graph(object):
#     def __init__(self, graph_id):
#         self.graph_id = graph_id
#         self.task_dic = {}
    # def append_task(self,task):
    #     self.task_list.append(task)


class Arc(object):
    def __init__(self, arc_id, type, task_end):
        self.task_id = arc_id
        self.type = type
        self.task_end = task_end

# task::status        0:not waken
#                     1:running
#                     2:stalled


class Task(object):
    def __init__(self, task_id, type_value):
        self.task_id = task_id
        self.type_value = type_value
        self.child = []
        self.parent = []
        self.runtime = 0
        self.status = 0
        self.finished = 0

    def is_executable(self):
        if not len(self.parent):
            exe_en = 1
        else:
            exe_en = 1
            for i in xrange(len(self.parent)):
                if not self.parent[i].finished:
                    exe_en = 0
                    break
        return exe_en

    def is_finished(self):
        if self.runtime >= self.type_value:
            self.finished = 1
        return self.finished


def core_allocation(task, cores):
    core_num = randint(0, 9)
    # while (cores[core_num].task_len >= 10):
    #     core_num = randint(0, 9)
    cores[core_num].task_list.append(task)
    # cores[core_num].task_len += 1;


def parse_task(tgff_file, cores, type_dic):
    lines = (tgff_file.lower().split("\n"))
    for line_num in xrange(len(lines)):
        if lines[line_num] == "":
            continue
        # elif lines[line_num].find('@') == 0:
        #     if lines[line_num].find('task_graph') == 1:
        #         line_elements = lines[line_num].split()
        #         graphs.append(Graph(line_elements[1]))
        #         graph_num += 1
        elif lines[line_num].find('#') == 0:
            continue
        else:
            line_elements = lines[line_num].split()
            if line_elements[0] == 'task':
                type_value = float(type_dic[line_elements[3]])
                task_new = Task(line_elements[1], type_value)
                core_allocation(task_new, cores)

                # elif line_elements[0] == 'arc':
                #     graphs[graph_num-1].task_dic[line_elements[3]].child.append(graphs[graph_num-1].task_dic[line_elements[5]])
                #     graphs[graph_num-1].task_dic[line_elements[5]].parent.append(graphs[graph_num-1].task_dic[line_elements[3]])
    #
    # print graphs[0].task_dic['t0_1'].parent




