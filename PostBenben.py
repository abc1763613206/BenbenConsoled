import requests
import time

def BackMain():
    import MainBenben
    MainBenben.get()
def post():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'referer': 'https://www.luogu.org/',
        'x-csrf-token':'',
        'x-requested-with':'XMLHttpRequest'

    }

    version = 'Luogu BenbenPoster v1.2'
    cookies={'__client_id': 'c6275f5aff586120f673b1e991d3d13f42bf1b09'}
    url='https://www.luogu.org/api/feed/postBenben'
    print('\n' + version + '\n如果想退出程序，多按几次Ctrl+C！输入exit返回看犇犇界面\n输入内容（Markdown格式）（回复请手动复制内容，并在前面加 || ）： \n')
    Content=input()
    if(Content == 'exit'):
        BackMain()
    data={'content' : str(Content)}
    req=requests.Session()
    res=req.post(url=url,data=data,headers=headers,cookies=cookies)
    print(res.text)
    print('\n已提交请求！请去犇犇查看详情！\n\n')
    time.sleep(2)
    BackMain()



