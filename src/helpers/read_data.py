import json

def read_json(path):
    with open (path, 'r') as file:
        data = json.load(file)
    return data

# def read_json_multiple():
#     with open ('', 'r') as file:
#         datas = json.loads(file)
#     for data in datas:
#         return data
