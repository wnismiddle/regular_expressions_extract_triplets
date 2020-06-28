import json
import re
import time


with open('config/attribute_template.json', 'r', encoding='utf-8') as f:
    attribute_template = json.load(f)


with open('config/relation_template.json', 'r', encoding='utf-8') as f:
    relation_template = json.load(f)


def extract_attribute(read_path, write_path):
    pattern_type_list = []
    pattern_list = []
    type_mapping_dict = {}
    for t in attribute_template:
        type_mapping_dict[t['e_pattern_type']] = t['e_type']
        type_mapping_dict[t['attribute_pattern_type']] = t['attribute_type']
        pattern_type_list.append((t['e_pattern_type'], t['attribute_pattern_type']))
        pattern_list.append(t['pattern'])

    start_time = time.time()
    extract_list = []
    with open(read_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            for (pattern_type, pattern) in zip(pattern_type_list, pattern_list):
                for p in pattern:
                    regex = re.compile(p)
                    group_index = regex.groupindex

                    e_idx = group_index[pattern_type[0]]
                    attribute_idx = group_index[pattern_type[1]]
                    for i in regex.finditer(line):
                        e = i.group(e_idx)
                        e_type = type_mapping_dict[pattern_type[0]]
                        attribute = i.group(attribute_idx)
                        attribute_type = type_mapping_dict[pattern_type[1]]
                        extract_list.append((e, e_type, attribute_type, attribute, line))
    with open(write_path, 'w', encoding='utf-8') as f:
        for l in extract_list:
            f.write('{}（{}） {}：{} {}\n'.format(l[0], l[1], l[2], l[3], l[4]))
    end_time = time.time()
    cost_time = end_time-start_time
    print('一共抽取了{}条属性， 经历了{}s, 平均每秒抽取{}条属性'.format(len(extract_list), cost_time, int(len(extract_list)/cost_time)))


def extract_relation(read_path, write_path):
    pattern_type_list = []
    pattern_list = []
    type_mapping_dict = {}
    for t in relation_template:
        type_mapping_dict[t['e1_pattern_type']] = t['e1_type']
        type_mapping_dict[t['e2_pattern_type']] = t['e2_type']
        type_mapping_dict[t['relation_pattern_type']] = t['relation_type']
        pattern_type_list.append((t['e1_pattern_type'], t['e2_pattern_type'], t['relation_pattern_type']))
        pattern_list.append(t['pattern'])

    start_time = time.time()
    extract_list = []
    with open(read_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            for (pattern_type, pattern) in zip(pattern_type_list, pattern_list):
                for p in pattern:
                    regex = re.compile(p)
                    group_index = regex.groupindex

                    e1_idx = group_index[pattern_type[0]]
                    e2_idx = group_index[pattern_type[1]]
                    relation_idx = group_index[pattern_type[2]]
                    for i in regex.finditer(line):
                        e1 = i.group(e1_idx)
                        e1_type = type_mapping_dict[pattern_type[0]]
                        e2 = i.group(e2_idx)
                        e2_type = type_mapping_dict[pattern_type[1]]
                        r = i.group(relation_idx)
                        r_type = type_mapping_dict[pattern_type[2]]
                        extract_list.append((e1, e1_type, e2, e2_type, r, r_type, line))
    with open(write_path, 'w', encoding='utf-8') as f:
        for l in extract_list:
            f.write('{}（{}） {}（{}） {}（{}） {}\n'.format(l[0], l[1], l[2], l[3], l[4], l[5], l[6]))
    end_time = time.time()
    cost_time = end_time - start_time
    print('一共抽取了{}条关系， 经历了{}s, 平均每秒抽取{}条关系'.format(len(extract_list), cost_time, int(len(extract_list) / cost_time)))
