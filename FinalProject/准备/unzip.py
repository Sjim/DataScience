import json
from urllib import request, parse
import os
from urllib.parse import quote
import zipfile


def mkdir(path):
    # 引入模块

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 下载文件
f = open('../sample.json', encoding='utf-8')  # 都先用sample测试
res = f.read()
data = json.loads(res)
for k, v in data.items():
    print("这是k:"+k)
    for i in v['cases']:
        print(i['case_id'])
        for key, value in i.items():
            print(key, "=", value)
# for a in data.values():
#     outer="e:\\study\\数据科学基础\\大作业\\testfiles\\"+str(a["user_id"])
#     mkdir(outer)
#     print(a['user_id'])
#     for cases in a['cases']:
#         print(cases['case_id'],cases['case_type'])
#         filename = outer+"\\"+parse.unquote(os.path.basename(cases["case_zip"]))
#         a= 'http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/'+quote(cases["case_zip"][57:])
#         request.urlretrieve(a,filename)

#将下载的文件解压
outest = "e:\\study\\DataScience\\DataScience\\FinalProject\\代码\\"
ids = os.listdir(outest)
for id in ids:
    print(id)
    zips = os.listdir(outest+str(id))
    for zip in zips:
        print(outest+id+"\\"+zip)
        print(os.getcwd())
        z=zipfile.ZipFile(outest+"\\"+id+"\\"+zip, 'r')
        os.makedirs(outest+"\\"+id+"\\"+zip[:-5])
        z.extractall(path=outest+"\\"+id+"\\"+zip[:-5])
        z.close()
        os.remove(outest+"\\"+id+"\\"+zip)
