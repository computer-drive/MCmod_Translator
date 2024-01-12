import os
import json
import zipfile
import sys
from colorama import Fore,Style
import shutil
import requests
import random
import base
import base.cmdLine as cmdLine
##检查更新
version=1.2

if "-NoCheckUpdate" not in cmdLine.finally_cmdl:
    print(f"检查更新....(当前版本：{version})")
    try:
        response = requests.get("https://computer-drive.github.io/software_update/mcmod_translator.json", timeout=1)
        
        if response.status_code  == 200:
            print("连接成功。")
            # print(response.text)
            json_data = json.loads(response.text)
            if json_data["latest_verison"]>version and version <= json_data["update"]["allow_version_max"] and version >= json_data["update"]["allow_version_min"]:
                #获取安装文件
                print("检测到新版本，正在下载Installer...")
                print(f"版本：{json_data['latest_verison']}")
                try:
                    response = requests.get(json_data["update"]["installer"], timeout=10)
        
                    if response.status_code  == 200:
                        filename=str(random.randint(0,65535))
                        os.system("md temp")
                        with open(f"{os.getcwd()}\\temp\\{filename}.exe","wb") as f:
                            f.write(response.content)
                        os.system(f"start {os.getcwd()}\\temp\\{filename}.exe -MainFile={__file__}")
                        sys.exit(0)
                    else:
                        print(f"获取失败，http状态码： {response.status_code}")

                except requests.Timeout:
                    print("连接超时。")

                except requests.RequestException as e:
                    print(f"连接失败")
            else:
                print("当前已是最新版本")
                
        else:
            print(f"获取失败，http状态码： {response.status_code}")

    except requests.Timeout:
        print("连接超时。")

    except requests.RequestException as e:
        print(f"连接失败")


    ##定义函数
    def get_subdirectories(folder_path):
        subdirectories = [f.path for f in os.scandir(folder_path) if f.is_dir()]
        return subdirectories

    def remove_last_segment(path):
        
        last_backslash_index = path.rfind('\\')

        if last_backslash_index != -1:
            return path[:last_backslash_index]

    

## 输出logo
print('''
___  ___ _____                        _   _____                           _         _                
|  \/  |/  __ \                      | | |_   _|                         | |       | |               
| .  . || /  \/ _ __ ___    ___    __| |   | |   _ __   __ _  _ __   ___ | |  __ _ | |_   ___   _ __ 
| |\/| || |    | '_ ` _ \  / _ \  / _` |   | |  | '__| / _` || '_ \ / __|| | / _` || __| / _ \ | '__|
| |  | || \__/\| | | | | || (_) || (_| |   | |  | |   | (_| || | | |\__ \| || (_| || |_ | (_) || |   
\_|  |_/ \____/|_| |_| |_| \___/  \__,_|   \_/  |_|    \__,_||_| |_||___/|_| \__,_| \__| \___/ |_|           ''')
##初始化
if "-UpdateLog" in cmdLine.finally_cmdl:
    print('''更新日志：
1.0
          ''')
print("正在初始化...")
try:
    if os.path.exists(".\\temp\\"):
        shutil.rmtree(".\\temp\\")
    try:
        if os.path.exists(".\\res\\"):
            shutil.rmtree(".\\res\\")
    except OSError as e:
        print("初始化失败！")
        print(f"原因：{e.strerror}")
        input()
        sys.exit()
except OSError as e:
    print("初始化失败！")
    print(f"原因：{e.strerror}")
    input()
    sys.exit()
print("初始化完毕！")
#输入并判断mod文件
mod_file=input("输入mod文件路径:")
if not os.path.exists(mod_file):
    print(f"{Fore.RED} {mod_file} 文件不存在！ {Style.RESET_ALL}")
    input()
    sys.exit()
##解压文件
print(f"解压 {mod_file}...")
zip=zipfile.ZipFile(mod_file)
zip_list=zip.namelist()
for f in zip_list:
    zip.extract(f,".\\temp\\")

print("解压完成！")
print(f"{Fore.BLUE}在运行目录中会产生一个temp目录，等待程序结束后自动删除。{Style.RESET_ALL}")
print("\n")
##读取语言文件
print("读取语言文件...")
if not os.path.exists(".\\temp\\assets\\"):
    print(f"{Fore.RED}assets文件夹不存在！你可能上传了一个错误的文件！ {Style.RESET_ALL}")
    input()
    sys.exit()
language_list=get_subdirectories(".\\temp\\assets\\")
##生成资源包

os.makedirs(os.getcwd()+"\\res\\")
with open(fr"{os.getcwd()}\res\pack.mcmeta","w",encoding="utf-8") as f:
    f.write('''
{
    "pack": { 
        "pack_format": 22,
        "description": "MCmod Translator资源包"
    }
}
            ''')
os.makedirs(fr"{os.getcwd()}\res\assets\\")
##遍历
for i in language_list:
    os.system("cls")
    with open(i+"\\lang\\en_us.json","r",encoding="utf-8") as f:
        en_us_json=json.loads(f.read())
    for j in en_us_json:
        print(en_us_json[j])
    print("======================")
    print("请将上面输出的信息丢到翻译软件中，然后将翻译信息存储到一个文件中，并输入这个文件的路径")
    translate_file=input()
    if not os.path.exists(translate_file):
        print(f"{Fore.RED} {translate_file} 文件不存在！ {Style.RESET_ALL}")
        input()
        sys.exit()
    with open(translate_file,"r",encoding="utf-8") as f:
        translate=f.read().split("\n")
    count=0
    for k in en_us_json:
        # print(count)
        # print(i)
        en_us_json[k]=translate[count]
        count+=1
    ## 写入
    new_path = i[1:]
    # 将'temp'替换为'res'
    new_path = new_path.replace("temp", "res")
    os.makedirs(fr"{os.getcwd()}{new_path}")
    os.makedirs(fr"{os.getcwd()}{new_path}\lang\\")
    with open(fr"{os.getcwd()}{new_path}\lang\zh_cn.json","w",encoding="utf-8") as f:
        f.write(json.dumps(en_us_json,ensure_ascii=False))
    print(f"{i} 写入完毕！")
print("全部写入完毕！")
#### 清理
print("正在清理Temp文件夹，请稍等...")
try:
    shutil.rmtree(".\\temp\\")
    print("删除成功！")
except OSError as e:
    print("删除失败，请手动删除。")
    print(f"原因：{e.strerror}")

input()