import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 示例：爬取笔趣阁首页的所有小说标题
def get_novel_titles(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.qidian.com/',
        'Cookie': '你的cookie粘贴在这里',  # 用浏览器F12复制Cookie内容
    }
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    proxies = {
        # 'http': 'http://127.0.0.1:7890',  # 如有可用代理，取消注释并填写
        # 'https': 'http://127.0.0.1:7890',
    }
    try:
        response = session.get(url, headers=headers, timeout=10, proxies=proxies)
        time.sleep(2)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        # 调试：如未获取到内容，保存页面源码
        if not soup.select('.book-mid-info h4 a'):
            with open('debug.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print('未获取到小说标题，已保存页面源码到 debug.html，请用浏览器打开分析。')
        # 针对起点畅销榜页面，小说标题在 .book-mid-info h4 a 标签中
        titles = []
        for a in soup.select('.book-mid-info h4 a'):
            title = a.get_text(strip=True)
            if title:
                titles.append(title)
        return titles
    except Exception as e:
        print(f'请求失败: {e}')
        return []

if __name__ == '__main__':
    url = 'https://www.qidian.com/rank/yuepiao/'  # 起点畅销榜页面
    titles = get_novel_titles(url)
    print('小说标题列表:')
    for t in titles:
        print(t)