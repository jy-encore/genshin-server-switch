import re
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import configparser
import os
import time
from re import S
import webbrowser

#定义触发函数功能
def getcps():
    cps=conf.get('General','cps')
    mes="成功切换服务器，当前服务器为"
    return(mes+cps)

def switchbilibili():
    conf.set('General', "channel", "14")
    conf.set('General', "cps", "bilibili")
    conf.write(open(inipath, "r+", encoding="utf-8"))
    ncps=getcps()
    tkinter.messagebox.showinfo(title='切换成功', message=ncps) 
    window.quit()
    window.destroy()

def switchmihoyo():
    conf.set('General', "channel", "1")
    conf.set('General', "cps", "mihoyo")
    conf.write(open(inipath, "r+", encoding="utf-8"))
    ncps=getcps()
    tkinter.messagebox.showinfo(title='切换成功', message=ncps) 
    window.quit()
    window.destroy()

def download():
    webbrowser.open("https://wwa.lanzoui.com/iYtg7v8dt0b")


#检查SDK文件是否存在
def sdk(path):
    file = path + 'YuanShen_Data\Plugins\PCGameSDK.dll'
    return(os.path.exists(file))

#设定工作路径
msg=tkinter.messagebox.askokcancel(title = '原神世界线切换器 提示',message='本程序借助原神本体识别工作目录\n不会对原神本体进行任何修改\n请在接下来的窗口中选择YuanShen.exe')

def openfile():
    pathtk=tk.Tk()
    pathtk.withdraw()
    file = filedialog.askopenfilename()
    return(os.path.abspath(file))

if msg== True:
    i=1
    while i < 100 :
        FolderPath = openfile()
        print(FolderPath)
        if 'YuanShen.exe' in FolderPath:
            curpath = FolderPath.replace('YuanShen.exe','')
            break
        else :
            tkinter.messagebox.showerror(title = '原神世界线切换器 提示',message='你选择的不是原神文件\n请选择YuanShen.exe')
            msg=tkinter.messagebox.askokcancel(title = '原神世界线切换器 提示',message='请在接下来的窗口中选择YuanShen.exe')
            if msg == True :
                i = i+1 
            elif msg == False:
                os._exit(0)
elif msg == False:
    os._exit(0)

print(curpath)

#设定config目录
inipath = os.path.join(curpath, "config.ini")

#读取ini
conf = configparser.ConfigParser()
conf.read(inipath, encoding="utf-8")
sections = conf.sections()

#检测文件
sdktf = sdk(curpath)
if sdktf == False:

    sdkmsg = tkinter.messagebox.showerror(title = '原神世界线切换器 提示',message='请检查PCGameSDK.dll是否在\YuanShen_Data\Plugins目录下\n点击确定进入下载链接 下载后请复制进以上目录并重启本程序')
    if sdkmsg == 'ok':
        download()
    time.sleep(1)
    os._exit(0)


# 主窗口window
window = tk.Tk()
window.title('原神世界线切换器')
window.geometry('200x50')


# 在图形界面上创建一个标签用以显示内容并放置
bi = tk.Button(window, text='切换b服', bg='white', font=('msyh', 13), command=switchbilibili)
bi.pack(side='left',padx=0,pady=0)
mi = tk.Button(window, text='切换官服', bg='white', font=('msyh', 11), command=switchmihoyo)
mi.pack(side='right',padx=0,pady=0)
 
# 主窗口循环显示
def _quit():
    window.quit()
    window.destroy() 
window.protocol("WM_DELETE_WINDOW", _quit)
window.mainloop()
