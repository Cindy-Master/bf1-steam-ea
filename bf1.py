import tkinter as tk
from tkinter import messagebox
import os
import shutil
import sys
import winreg

def get_bf1_install_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\EA Games\Battlefield 1")
        value, _ = winreg.QueryValueEx(key, "Install Dir")
        return value
    except Exception as e:
        messagebox.showerror("Error", "无法获取战地一的安装路径！")
        return None

def copy_files_to_install_dir():
    install_dir = get_bf1_install_path()
    if install_dir:
        try:
            for filename in ["installScript.vdf", "EAStore.ini"]:
                source_path = os.path.join(getattr(sys, '_MEIPASS', os.getcwd()), filename)
                destination_path = os.path.join(install_dir, filename)
                shutil.copy(source_path, destination_path)
            messagebox.showinfo("Info", "文件复制成功！")
        except Exception as e:
            messagebox.showerror("Error", "复制文件时发生错误！")




def steam_to_origin():
    copy_files_to_install_dir()
    install_dir = get_bf1_install_path()
    if install_dir:
        try:
            os.remove(os.path.join(install_dir, "installScript.vdf"))
        except FileNotFoundError:
            messagebox.showinfo("Info", "installScript.vdf 文件不存在。")
        except Exception as e:
            messagebox.showerror("Error", "删除 installScript.vdf 时发生错误！")

def steam_to_ea():
    copy_files_to_install_dir()
    install_dir = get_bf1_install_path()
    if install_dir:
        try:
            os.remove(os.path.join(install_dir, "EAStore.ini"))
        except FileNotFoundError:
            messagebox.showinfo("Info", "EAStore.ini 文件不存在。")
        except Exception as e:
            messagebox.showerror("Error", "删除 EAStore.ini 时发生错误！")

def ea_origin_to_steam():
    copy_files_to_install_dir()

app = tk.Tk()
app.title("战地一版本转换工具")
app.geometry("400x200")

label = tk.Label(app, text="仅支持steam下载的游戏进行三版本转换\n不支持EA或Origin下载后的游戏进行转换\n推荐使用msk大佬的免平台工具\n推荐使用msk大佬的免平台工具\n推荐使用msk大佬的免平台工具\n本工具制作by：Master", justify=tk.LEFT)
label.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

btn_steam_to_origin = tk.Button(button_frame, text="steam-->origin", command=steam_to_origin)
btn_steam_to_origin.pack(side=tk.LEFT, padx=5)

btn_steam_to_ea = tk.Button(button_frame, text="steam-->EA", command=steam_to_ea)
btn_steam_to_ea.pack(side=tk.LEFT, padx=5)

btn_ea_origin_to_steam = tk.Button(button_frame, text="EA/origin-->steam", command=ea_origin_to_steam)
btn_ea_origin_to_steam.pack(side=tk.LEFT, padx=5)

app.mainloop()
