import csv
from pypinyin import lazy_pinyin
from collections import defaultdict


def create_pinyin_abbr(name):
    abbr = ''.join([p[0] for p in lazy_pinyin(name)])
    return abbr


# 从文件中读取数据
data = []
with open('/Users/wsw/Desktop/Oier.txt', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append({
            "award": row[0],
            "level": row[1],
            "name": row[2],
            "grade": row[3],
            "school": row[4],
            "score": int(row[5]),
            "province": row[6],
            "gender": row[7],
        })

# 创建一个字典，将拼音缩写作为键，对应的人名和排名的元组列表作为值
pinyin_to_name = defaultdict(list)
for record in data:
    name = record['name']
    pinyin_abbr = create_pinyin_abbr(name)
    pinyin_to_name[pinyin_abbr].append((record['score'], name))


def find_names_by_pinyin(pinyin):
    names = pinyin_to_name.get(pinyin, [])
    if not names:
        return "No matching names found"

    # 按排名对名称列表进行排序
    names.sort(key=lambda x[0]: x)

    # 仅返回名称，不包括排名
    return [name for score, name in names]


# 示例用法
print(find_names_by_pinyin("dht"))
