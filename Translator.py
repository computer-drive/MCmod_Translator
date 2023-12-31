import json
import os
print('''
___  ___ _____                        _   _____                           _         _                
|  \/  |/  __ \                      | | |_   _|                         | |       | |               
| .  . || /  \/ _ __ ___    ___    __| |   | |   _ __   __ _  _ __   ___ | |  __ _ | |_   ___   _ __ 
| |\/| || |    | '_ ` _ \  / _ \  / _` |   | |  | '__| / _` || '_ \ / __|| | / _` || __| / _ \ | '__|
| |  | || \__/\| | | | | || (_) || (_| |   | |  | |   | (_| || | | |\__ \| || (_| || |_ | (_) || |   
\_|  |_/ \____/|_| |_| |_| \___/  \__,_|   \_/  |_|    \__,_||_| |_||___/|_| \__,_| \__| \___/ |_|                                                                                                                                                                                   
''')
file_path=input("请输入需要翻译的语言文件路径：")
if os.path.exists(file_path):
    print("读取中...")
    with open(file_path,"r",encoding="utf-8") as f:
        file=json.loads(f.read())
    print("读取完成。")
    os.system("cls")
    for i in file:
        print(file[i]+" ")
    print("======================")
    print("请将上面输出的信息丢到翻译软件中，然后将翻译信息存储到一个文件中，并输入这个文件的路径")
    translate_file=input()
    if os.path.exists(translate_file):
        with open(translate_file,"r",encoding="utf-8") as f:
            translate=f.read().split("\n")
        count=0
        for i in file:
            
            # print(count)
            # print(i)
            file[i]=translate[count]
            count+=1

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(file,ensure_ascii=False))
        input("写入完成！")
        exit(0)
    else:
        print(f"{translate_file} 不存在！")
    input()
else:
    print(f"{file_path} 不存在！")
    input()