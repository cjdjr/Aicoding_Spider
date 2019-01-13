# -*- coding:utf-8 -*-
import requests
import csv
import json
import random

ans=[]

def get_first_page(baseurl,header,page):#分析动态加载后得到的json格式页面
    print('正在打开第' + str(page) + '页网站')
    url=baseurl+r'page={0}&size=20&IsType=编程题&IsOrigin=课本&IsOriginExtend=课本%7C信息学一本通'.format(page)
    print(url)
    try:
        r = requests.get(url,headers = header[random.randint(0,1)])
        r.raise_for_status()
        r.encoding='utf-8'
        response=r.text
        # print(response)
        html=json.loads(response)
        return html
    except:
        print('打开网页失败！')

def save_to_db(data):

    # data是个list，将里面的内容保存到csv文件中
    with open('D:\ACM\一本通视频录制/题号.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            tmp=[]
            tmp.append(row)
            writer.writerow(tmp)


def spider():
    baseurl='http://www.aicoding.info/Homework/ProblemAdminquery?'  # json动态网址的格式是：网址+'?'+查询内容，网址和查询内容通过浏览器抓包
    header=[
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)',
         'Cookie':'.AspNet.ApplicationCookie=qtss28v46SjGiJkD89nIn95bHhk4swQE6v8ondafAysk69Bdj36SVp1vDtRL1Mt1PcYqpPekV51gC6Kf42Zcxll1c834rGgcmt-W1c0yxh4NGilZugHD3nesaLpv1yH5z6P238GdoAkGsjAhK564tus-Ha6kd3rYCrmtb6jzbsl1_wsK5KFzWs7i4Mw3XfW0VH-A0UKEQB0Jt3QpwS_11vBjkPMBtVoT2krt1aL0VqsAX4IYb7eEx7pLSBnbxWNThR8yaMVRWUdFf-qZP007p_mYRVW6-Upn5kkt4ZzTA66eDKJ6JdJ-4GbhO81PGZ_XZb21DqZ0C-05hopN4KbLXvRf4i_OqezxP9vvtqPaDXDYIhvJGOE5nQKwUvUZtZHt9hSkRzeFfCAcsDqAm2YeBluV7ZoARY2yYPVv-Qo5xCTmnSJrkqJd5bP3zrx1GH9bD0LX1tO3iEZzfMubCf1qT5yqdkrWC272Kug-2WGU8eoCZNyN21NLNPmDQMQAPjkfHUBsIGNZM_O6BVp2yzjO1g; __RequestVerificationToken=wTB28Dmvrc-DywoZyKq8AmnrCzZPyvyMFO_SV79MdJjUMvcKcRoKjBlC5-Sulg92URJK-S7K9MJSECkFs1r46Ev8U7lyyn3t_OPHy1IiMDU1'},
        {'User-Agent':'Mozilla/4.04[en](Win95;I;Nav)',
         'Cookie':'.AspNet.ApplicationCookie=qtss28v46SjGiJkD89nIn95bHhk4swQE6v8ondafAysk69Bdj36SVp1vDtRL1Mt1PcYqpPekV51gC6Kf42Zcxll1c834rGgcmt-W1c0yxh4NGilZugHD3nesaLpv1yH5z6P238GdoAkGsjAhK564tus-Ha6kd3rYCrmtb6jzbsl1_wsK5KFzWs7i4Mw3XfW0VH-A0UKEQB0Jt3QpwS_11vBjkPMBtVoT2krt1aL0VqsAX4IYb7eEx7pLSBnbxWNThR8yaMVRWUdFf-qZP007p_mYRVW6-Upn5kkt4ZzTA66eDKJ6JdJ-4GbhO81PGZ_XZb21DqZ0C-05hopN4KbLXvRf4i_OqezxP9vvtqPaDXDYIhvJGOE5nQKwUvUZtZHt9hSkRzeFfCAcsDqAm2YeBluV7ZoARY2yYPVv-Qo5xCTmnSJrkqJd5bP3zrx1GH9bD0LX1tO3iEZzfMubCf1qT5yqdkrWC272Kug-2WGU8eoCZNyN21NLNPmDQMQAPjkfHUBsIGNZM_O6BVp2yzjO1g; __RequestVerificationToken=wTB28Dmvrc-DywoZyKq8AmnrCzZPyvyMFO_SV79MdJjUMvcKcRoKjBlC5-Sulg92URJK-S7K9MJSECkFs1r46Ev8U7lyyn3t_OPHy1IiMDU1'}
    ]   # 用 Cookie 模拟登陆
    page=1
    total=26
    while page<=total:
        html=get_first_page(baseurl, header, page)  # html是返回的字典类型的数据
        # print(html)
        for each in html['data']:
            ans.append(each['id'])
        page+=1

if __name__=='__main__':

    spider()
    ans.sort()
    print(ans)
    save_to_db(ans)