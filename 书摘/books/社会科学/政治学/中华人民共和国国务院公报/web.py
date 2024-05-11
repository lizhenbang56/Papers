"""
对应关系
https://www.gov.cn/gongbao/2023/issue_10686/  2023-25
https://www.gov.cn/gongbao/2023/issue_10246/  2023-3
https://www.gov.cn/gongbao/2023/issue_10226/  2023-2
https://www.gov.cn/gongbao/2023/issue_10206/  2023-1
https://www.gov.cn/gongbao/2022/issue_10186/  2022-35
https://www.gov.cn/gongbao/2022/issue_9526/   2022-2
https://www.gov.cn/gongbao/2022/issue_9506/   2022-1
https://www.gov.cn/gongbao/2011/issue_2096/   2011-1
"""
import requests
from bs4 import BeautifulSoup


def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件内容并传递给Beautiful Soup对象
        soup = BeautifulSoup(file, 'html.parser')
        # 打印整个Beautiful Soup对象的结构（可选）
        # print(soup.prettify())

        # 示例：获取所有链接的href属性值
        items = soup.find_all('li')
        for item in items:
            a_tag = item.find('a')
            if a_tag:
                attrs = a_tag.attrs
                if 'href' in attrs:
                    href = a_tag['href']
                    if href[:2] == './':
                        extracted_text = a_tag.get_text(strip=True)
                        print(extracted_text)


def web_download(year, issue):

    url = 'https://arxiv.org/list/cs/new'
    try:
        # 发送 HTTP GET 请求
        response = requests.get(url)
        total_size = int(response.headers.get('content-length', 0))
        print(total_size)

        # 检查是否成功获取页面
        if response.status_code == 200:
            print('成功连接')
            # 获取页面内容
            html_content = response.text

            # 可以将内容保存到文件，如下：
            save_path = "{}.html".format(file_name)
            if os.path.exists(save_path):
                print('文件{}已存在'.format(save_path))
            else:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(html_content)
                    print('保存完成')
                    html_to_docx(file_name)
        else:
            print("无法获取页面，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)

def parse(url):    
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    response.encoding = 'utf-8'  # 解决中文乱码    

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用Beautiful Soup解析网页内容
        soup = BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('li')
        for title in titles:
            print(title)
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)


def main():
    # url = 'https://www.gov.cn/gongbao/2023/issue_10686/'
    # parse(url)
    # path = '2023-25.html'
    # parse_html(path)


if __name__ == '__main__':
    main()

