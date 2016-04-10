


def parse_type(tgff_file):
    type_dic = {}
    type_en = 0
    lines = (tgff_file.lower().split("\n"))
    for line_num in xrange(len(lines)):
        line_elements = lines[line_num].split()
        if type_en and len(line_elements) == 2:
            print line_elements
            type_dic[line_elements[0]] = line_elements[1]
        if lines[line_num] == "":
            continue
        elif lines[line_num].find("# type") == 0:
            type_en = 1
    return type_dic
