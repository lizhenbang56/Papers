markdown_table = """
| 日期         |       |     | 4216 余额 | 微信零钱 |
| ---------- | ----- | --- | --- | ---- |
| 2024-03-21 | +37.82 | 利息  |
| 2024-03-27 | 20    |     |
| 2024-04-11 | -16.00 | qq音乐会员 | 36221.35 | 17542.72 |
| 2024-04-12 | -12.50 | 买桑葚 | 36029.29 |
| 2024-04-13 | +17525.19 | 微信提现 | 53554.48 |
"""

with open('账单.md') as f:
    markdown_table = f.read().splitlines()

# 将Markdown表格分割为行
table_rows = markdown_table#.strip().split('\n')

row_num = len(table_rows)

current_money = None
history = 0


# 初始化一个空列表来存储解析后的数据
parsed_data = []

# 遍历每一行
for row_id in range(row_num):
    print(row_id)
    row = table_rows[row_id]
    # 移除行首尾的'|'字符和空格
    #clean_row = row.strip('| ')
    # 根据竖线'|'分割每一行的数据
    data_items = row.split('|')

    if row_id > 2:
        history += float(data_items[2])
        print(history)
        current_money = float(data_items[-2]) + float(data_items[-3])
        print(current_money)
    print(data_items)
    # 移除空字符串
    data_items = [item for item in data_items if item]
    # 将解析后的数据添加到列表中
    parsed_data.append(data_items)

# 打印解析后的数据
#for entry in parsed_data:
    #print(entry)