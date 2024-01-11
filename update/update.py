import wget
import base.cmdLine as cmdLine
from base.customPrint import ForeColor,BackColor,Style
import base
import sys
import requests
import json
import os
import base

cmdLine.GetCommandLine()
# print(cmdLine.finally_cmdl)
if len(cmdLine.finally_cmdl)<2:
    base.error("需要-MainFile参数","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
    input()
    sys.exit(1)
else:
    main_file=cmdLine.finally_cmdl[1]["-MainFile"]
    base.info(f"主程序文件:{main_file}","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_BLUE_EX}INFO{Style.REST} ",text_color="")



base.info(f"正在获取更新信息","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_GREEN}WROK{Style.REST} ",text_color="")

try:
    response = requests.get("https://computer-drive.github.io/software_update/mcmod_translator.json", timeout=10)
    
    if response.status_code == 200:
        base.info(f"连接成功,解析文件中","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_GREEN}WROK{Style.REST} ",text_color="")
        update_info = json.loads(response.text)
        base.info(f"更新信息：{update_info}","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_BLUE_EX}INFO{Style.REST} ",text_color="")
    else:
        base.error(f"{ForeColor.RED}获取失败，http状态码： {response.status_code}{Style.REST}","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
        input()
        sys.exit(1)
        
except requests.Timeout:
    base.error("连接超时。","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
    input()
    sys.exit(1)
except requests.RequestException as e:
    base.error("连接失败。","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
    input()
    sys.exit(1)

base.info(f"正在下载文件","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_GREEN}WROK{Style.REST} ",text_color="")
try:
    response = requests.get(update_info["update"]["update_pack_file"], timeout=10)
    
    if response.status_code == 200:
        base.info(f"正在保存文件","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_GREEN}WROK{Style.REST} ",text_color="")
        with open(main_file,"wb") as f:
            f.write(response.content)
        base.info(f"文件保存完成！","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_BLUE_EX}INFO{Style.REST} ",text_color="")
        base.info(f"更新完成！","",show_location=False,show_time=False,type=f"{ForeColor.LIGHT_BLUE_EX}INFO{Style.REST} ",text_color="")
        os.system(f"start {main_file}")
    else:
        base.error(f"{ForeColor.RED}获取失败，http状态码： {response.status_code}{Style.REST}","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
        input()
        sys.exit(1)
        
except requests.Timeout:
    base.error("连接超时。","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
    input()
    sys.exit(1)
except requests.RequestException as e:
    base.error("连接失败。","",show_location=False,show_time=False,type=f"{ForeColor.RED}ERROR{Style.REST} ",text_color="")
    input()
    sys.exit(1)

