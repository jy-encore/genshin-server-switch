import re
import tkinter as tk
import tkinter.messagebox
import configparser
import os
from re import S
import webbrowser

#获取当前路径
curpath = os.path.dirname(os.path.realpath(__file__))
#设定config目录
inipath = os.path.join(curpath, "config.ini")

#读取ini
conf = configparser.ConfigParser()
conf.read(inipath, encoding="utf-8")
sections = conf.sections()

cps=conf.get('General','cps')
mes="成功切换服务器，当前服务器为"
ncps=mes+cps

# 主窗口window
window = tk.Tk()
window.title('原神世界线切换器')
window.geometry('500x150')
 
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
    window.destroy()

def switchmihoyo():
    conf.set('General', "channel", "1")
    conf.set('General', "cps", "mihoyo")
    conf.write(open(inipath, "r+", encoding="utf-8"))
    ncps=getcps()
    tkinter.messagebox.showinfo(title='切换成功', message=ncps) 
    window.destroy()

def download():
    webbrowser.open("https://wwa.lanzoui.com/iYtg7v8dt0b")

#提示信息
a = tk.Label(window, text='请将软件置于GenshinImpactGame文件夹', font=('simhei', 12), width=400, height=1)
a.pack()
b = tk.Label(window, text='并确保PCGameSDK.dll在\YuanShen_Data\Plugins目录下', font=('simhei', 12), width=400, height=1)
b.pack()

# 在图形界面上创建一个标签用以显示内容并放置
bi = tk.Button(window, text='切换b服', bg='white', font=('simhei', 13), command=switchbilibili)
bi.pack()
mi = tk.Button(window, text='切换官服', bg='white', font=('simhei', 11), command=switchmihoyo)
mi.pack()
dn = tk.Button(window, text='下载PCGameSDK.dll', bg='white', font=('simhei', 11), command=download)
dn.pack()
 
# 主窗口循环显示
window.mainloop()