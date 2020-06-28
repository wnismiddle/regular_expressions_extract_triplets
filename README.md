# Use regular expressions to extract triplets

## 描述
该项目支持使用正则表达式抽取文本中的实体-属性-属性值、实体-关系-实体三元组



## 文件说明

config/attribute_template.json 配置属性的正则表达式抽取模板

config/relation_template.json 配置关系的正则表达式抽取模板



## 脚本入参

* sys.argv[0] 表示脚本名  
* sys.argv[1] 表示读取路径  
* sys.argv[2] 表示抽取结果的写入路径  
* sys.argv[3] 表示抽取任务类型。attribute：属性抽取，relation：关系抽取。无传参默认属性抽取。  


## 示例启动命令

* 抽取属性
```
python main.py data/raw_text.txt data/attribute_extract_result.txt attribute
```
* 抽取关系
```
python main.py data/raw_text.txt data/relation_extract_result.txt relation
```