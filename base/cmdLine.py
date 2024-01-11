import sys
original_cmdl=sys.argv
finally_cmdl=[]
def GetCommandLine(not_moudle=False):
    for i in original_cmdl: #遍历整个命令行列表
        i_list=i.split("=")
        if "=" in i and len(i_list)==2: #是否为一对键值对
            finally_cmdl.append({i_list[0]:i_list[1]})
            
        else:
            #否
            finally_cmdl.append(i)


if __name__=="__main__":
    GetCommandLine(not_moudle=True)
    print(finally_cmdl)
else:
    GetCommandLine()