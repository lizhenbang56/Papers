import glob
import csv

def generate_csv():
    files = sorted(glob.glob('C:\\zhbli\\notes\\2024年一所工作任务\\20240605CTID测试\\接口\\人脸特征提取接口\\json_files\\*.json'))
    print(files)
    with open("人脸特征提取接口.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for file in files:
            writer.writerow([file])
    print('文件名导出完成')


if __name__ == '__main__':
    generate_csv()