import yaml
import json

yaml_path = r'test.yaml'
json_path = r'test.json'


def yaml2json(yaml_path: str, json_path: str):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    dict_content = yaml.load(content, Loader=yaml.FullLoader)
    # print(dict_content)
    with open(json_path, 'w+', encoding='utf-8') as f:
        json.dump(dict_content, f)


with open('dockerTest.py', 'r') as f:
    lines = f.readlines()
