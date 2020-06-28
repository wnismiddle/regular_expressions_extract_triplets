import sys
from extract_utils import extract_attribute, extract_relation

assert len(sys.argv) >= 3
'''
sys.argv[0] 表示脚本名
sys.argv[1] 表示读取路径
sys.argv[2] 表示抽取结果的写入路径
sys.argv[3] 表示抽取任务类型。attribute：属性抽取，relation：关系抽取。无传参默认属性抽取。

'''
print(len(sys.argv))
print(str(sys.argv))

read_path = sys.argv[1]
write_path = sys.argv[2]

# read_path = 'data/raw_text.txt'
# write_path = 'data/attribute_extract_result.txt'
# write_path = 'data/relation_extract_result.txt'

if len(sys.argv) >= 4:
    task_type = sys.argv[3]
    assert task_type in ['attribute', 'relation']
else:
    task_type = 'attribute'


if task_type == 'attribute':
    extract_attribute(read_path, write_path)
else:
    extract_relation(read_path, write_path)



