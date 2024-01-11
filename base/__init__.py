import datetime
from operator import ge
from base.customPrint import ForeColor,BackColor,Style
import os
import yaml
import json
import requests
import platform
from base import systemInfo
from translate import Translator
# Gihtub_Update 更新的信息
class NoUpdate():
    pass
class VersionLow():
    pass
class VersionHigh():
    pass
class NoUPdatePack():
    pass
class UpdatePack():
    url=""
    def __init__(self,url) -> None:
        self.url=url
###################
def get_time(): #获取时间
    '''
    返回现在的时间。格式：小时:分钟:秒
    '''
    return datetime.datetime.now().strftime("%H:%M:%S")

def info(text:str,location:str,
         text_color=None, #文本
         show_location:bool=False, #是否显示位置
         show_time:bool=True, #是否显示时间
         show_type:bool=True, #是否显示类型
         type:str=f"{ForeColor.LIGHT_BLUE_EX}[INFO]{Style.REST}", #类型
         time:str=f"{ForeColor.LIGHT_BLUE_EX}[{get_time()}]{Style.REST}", #时间
         more_information_first:str="", #额外信息，前面
         more_information_end:str="", #额外信息，最后
         location_color=ForeColor.LIGHT_BLUE_EX):  #位置颜色

    if not more_information_first==0:
        print(more_information_first,end="")
    if show_time:
        print(time,end="")
    # print(show_location)
    if show_location==True:
        print(show_location)
        print(f"{text_color}{location}{Style.REST}",end="")
    else:
        pass
    if show_type:
        print(type,end="")
    if not text_color==None:
        print(text_color,end="")
    else:
        print(ForeColor.LIGHT_BLUE_EX,end="")
    print(f"{text_color}{text}{Style.REST}",end="")
    if not more_information_end=="":
        print(more_information_end,end="")
    print("")

def warn(text:str,location:str,
         text_color=None,
         show_location:bool=False,
         show_time:bool=True,
         show_type:bool=True,
         type:str=f"{ForeColor.LIGHT_YELLOW}[WARN]{Style.REST}",
         time:str=f"{ForeColor.LIGHT_YELLOW}[{get_time()}]{Style.REST}",
         more_information_first:str="",
         more_information_end:str="",location_color=ForeColor.LIGHT_YELLOW):
    if not more_information_first==0:
        print(more_information_first,end="")
    if show_time:
        print(time,end="")
    # print(show_location)
    if show_location==True:
        print(show_location)
        print(f"{text_color}{location}{Style.REST}",end="")
    else:
        pass
    if show_type:
        print(type,end="")
    if not text_color==None:
        print(text_color,end="")
    else:
        print(ForeColor.LIGHT_YELLOW,end="")
    print(f"{text_color}{text}{Style.REST}",end="")
    if not more_information_end=="":
        print(more_information_end,end="")
    print("")

def error(text:str,location:str,
         text_color=None,
         show_location:bool=False,
         show_time:bool=True,
         show_type:bool=True,
         type:str=f"{ForeColor.RED}[ERROR]{Style.REST}",
         time:str=f"{ForeColor.RED}[{get_time()}]{Style.REST}",
         more_information_first:str="",
         more_information_end:str="",location_color=ForeColor.RED):
    if not more_information_first==0:
        print(more_information_first,end="")
    if show_time:
        print(time,end="")
    # print(show_location)
    if show_location==True:
        print(show_location)
        print(f"{text_color}{location}{Style.REST}",end="")
    else:
        pass
    if show_type:
        print(type,end="")
    if not text_color==None:
        print(text_color,end="")
    else:
        print(ForeColor.RED,end="")
    print(f"{text_color}{text}{Style.REST}",end="")
    if not more_information_end=="":
        print(more_information_end,end="")
    print("")

def log_info(text:str,location:str,
         text_color=None,
         show_location:bool=False,
         show_time:bool=True,
         show_type:bool=True,
         type:str=f"[INFO]",
         time:str=f"[{get_time()}]",
         more_information_first:str="",
         more_information_end:str="",location_color=""):
    if not more_information_first==0:
        print(more_information_first,end="")
    if show_time:
        print(time,end="")
    # print(show_location)
    if show_location==True:
        print(show_location)
        print(f"{text_color}{location}{Style.REST}",end="")
    else:
        pass
    if show_type:
        print(type,end="")
    print(f"{text}{Style.REST}",end="")
    if not more_information_end=="":
        print(more_information_end,end="")
    print("")

def fix_moudles(print=False): #修复运行库
    pass


def open_yaml(filename):#读取yaml
    '''
    打开文件，并读取转换成python的格式。
    返回值：当返回值为"FileNotFound"时，代表文件不存在
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    except FileNotFoundError:
        return "FileNotFound"


def write_yaml(filename,writevaule): #写入yaml
    '''
    打开文件，并将python的格式转换成yaml文件的格式写入文件
    返回值：当返回值为"FileNotFound"时，代表文件不存在。返回值为"WriteFinish"代表写入成功
    '''
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            yaml.dump(data=writevaule, stream=f, allow_unicode=True)
            return "WriteFinish"
    except FileNotFoundError:
        return "FileNotFound"

def read_json(filename): #读取json
    '''
    读取文件并转换成python格式
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        json_text=json.loads(f.read())
    return json_text

    
def write_json(filename,writevaule): #写入json
    '''
    读取文件，并将python的格式转换成json的格式写入文件
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(writevaule))

def read_file(filename):
    
    '''
    读取文件并返回文件的内容
    '''
    with open(filename,"r",encoding="utf-8") as f:
        return f.read()
    

def write_file(filename,write):
    '''
    读取文件，并将python的格式转换成json的格式写入文件
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(write)


def clean_screen():
    '''
    清除屏幕
    '''
    os.system("cls")

def set_color(arg:str):
    '''
    更改颜色
    '''
    os.system("color "+arg)

def pip_install(packagename):
    '''
    通过pip安装python模块
    '''
    os.system("pip install "+packagename) 



def web_download(url,timeout):
    '''
    从网页中下载文件\n
    参数：\n
    url -文件地址\n
    timeout -超时时间 \n
    返回值将以元组的形式返回\n
    {\n
        "http_code": http状态码,\n
        "return_data":返回的数据,\n
        "time_out":是否连接超时\n
    }\n
    '''
    try:
        response = requests.get(url,timeout=timeout)
        return {
            "http_code":response.status_code,
            "return_data":response.text,
            "time_out":True
        }
    except requests.Timeout:
        return {
            "http_code":None,
            "return_data":None,
            "time_out":True
        }

class Web_download():
    '''
    获取网页上的内容\n
    当定义类时，提供两个参数：\n
    url -地址\n
    timeout -超时时间\n
    然后会自动下载文件，返回值将在类的成员中\n
    Is_timeout 是否连接超时，当连接超时时，为True，否则为False\n
    http_code  返回的http状态码\n
    data       返回的内容\n
    '''
    url=""
    timeout=0
    Is_timeout=False
    http_code=0
    data=""
    def __init__(self,url,timeout) -> None:
        self.url=url
        self.timeout=timeout
        try:
            response=requests.get(self.url,timeout=self.time_out)
            self.http_code=response.status_code
            self.data=response.text
        except requests.Timeout:
            self.Is_timeout=True


def translate_en_to_zh(vaule):
    '''
    翻译：英->中
    '''
    translator = Translator(to_lang="chinese")
    translation = translator.translate(vaule)
    return translation

class Github_update():
    version=""
    update_file=""
    timeout=0
    def __init__(self,version,update_file,timeout) -> None:
        self.version=version
        self.update_file=update_file
        self.timeout=timeout
    
    def check_update(self):
        download_example=Web_download(self.update_file,self.timeout)
        download_data=download_example.data
        if download_data["latest_verison"] > self.version:
            if self.version <download_data["update"]["allow_version_min"]:
                return VersionLow
            elif self.version >download_data["update"]["allow_version_max"]:
                return VersionHigh
            elif download_data["update"]["update_pack"]==False:
                return NoUPdatePack
            else:
                return_vaule=UpdatePack(download_data["update"]["update_pack_file"])
                return return_vaule
                
        else:
            return NoUpdate
        
class SystemInfo():
    '''
    获取系统信息
    version=系统版本
    system=系统(Windows)
    format=系统规格(32bit,64bit)
    type=处理器类型(AMD64)
    name=计算机名称
    cpu_info=CPU信息
    '''
    version=platform.version() 
    system=platform.system()
    format=platform.architecture()[0]
    type=platform.machine()
    name=platform.node()
    cpu_info=systemInfo.GetCpuConstants()["cpu_name"]
    class Python():
        buildinfo=platform.python_build()
        version=platform.python_version()
    python=Python() 
        
def set_title(title):
    os.system(f"title {title}")


if __name__=="__main__":
    print('这个python程序是一个模块，你需要在其他的python文件中使用import 或 from xxx import 等来使用。')
    
    # print(SystemInfo.version,SystemInfo.system,SystemInfo.format,SystemInfo.type,SystemInfo.name,SystemInfo.cpu_info,SystemInfo.python.buildinfo,SystemInfo.python.version)