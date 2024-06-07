import pandas as pd
import re
import os
import json
from pathlib import Path


def remove_file_extension(file_path):
    """
    Remove the file extension from a given file path.

    :param file_path: The file path from which to remove the extension.
    :return: The file path without the extension.
    """
    return str(Path(file_path).with_suffix(''))


# Define a function to extract photoData1 and photoData2 image names
def extract_image_names(text):
    photo_data1 = re.findall(r'photoData1:\s*([\w.]+)', text)[0]
    photo_data2 = re.findall(r'photoData2:\s*([\w.]+)', text)[0]
    photo_data1 = remove_file_extension(photo_data1)+'.txt'
    photo_data2 = remove_file_extension(photo_data2)+'.txt'
    return photo_data1, photo_data2


# Load the Excel file
file_path = '测试报告.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name='测试报告')

# 遍历每个测试行
for index, row in df.iterrows():
    photo_data1, photo_data2 = extract_image_names(row['测试步骤'])
    print(index, photo_data1, photo_data2)
    with open(os.path.join('base64', photo_data1), 'r') as f:
        base64_1 = f.read()
    with open(os.path.join('base64', photo_data2), 'r') as f:
        base64_2 = f.read()
    json_data = {'bizSerialNo': str(12345678901234567890123456789000+index),
                 'photoData1': base64_1,
                 'photoData2': base64_2}
    
    # 保存字典为JSON文件
    with open(os.path.join('json_files', '{}.json'.format(index)), 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)