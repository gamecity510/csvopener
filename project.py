import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import font
from tkinter import messagebox
#ساخت alert 
def alert_big():
    messagebox.showinfo(title='فایل بزرگ است', message='فایل شما بیش از 20 ستون و سطر است')
def alert_none():
    messagebox.showinfo(title='هشدار', message='لطفا  ادرس را درست وارد کنید')
def alert_file():
    messagebox.showinfo(title='هشدار', message='فایل را لطفا وارد کنید ')

#ساخت پنجره
root = tk.Tk()
root.title("Database Sorting")
root.configure(bg="#1e3f66")  
root.geometry("500x300")       
#تغییر فونت
custom_font = font.Font(family="Helvetica", size=12, weight="bold")
# فریم برای مرتب کردن ویجت‌ها
frame = tk.Frame(root, bg="#1e3f66")
frame.pack(padx=20, pady=20, fill="both", expand=True)
#ساخت  یک تابع برای خواندن فایل و نمایش ان
def open_file():
    #ساخت پنجره انتخاب فایل و تایپ فایل
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    #شرط برای  وارد نشدن فایل
    if not filepath:
        return alert_file()
    #مشحص کردن مسیر فایل و خواندن ان
    df = pd.read_csv(filepath)
    #تنظیم پنجره چارت
    plt.figure(figsize=(10, 6))
    #تنظیم شرط فایل های بزرگ 
    if df.shape[0] < 20 and df.shape[1] < 20:
        #تنظیم چارت بر اساس دیتا 
        for col in df.columns:
            plt.plot(df.index, df[col], label=f'Column {col}')
            """  df.columns لیستی از نام ستون‌های DataFrame است.
            
            """

        plt.title('Columns')
        plt.xlabel('Row')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
    else:
        
        return alert_big()
# ساخت تابع برای url
def open_url():
    url = entry.get()#دریافت  مفدار نوار تکست
    if url == "":#بررسی مقدار نوار
        return alert_none()
    url = str(url)#رشته کردن نوار
    try:#ساخت باگ هندلر
        df = pd.read_csv(url)#خواندن فایل csv
    except Exception as e:
        
        return alert_none()

    plt.figure(figsize=(10, 6))
    if df.shape[0] < 20 and df.shape[1] < 20:
        for col in df.columns:
            plt.plot(df.index, df[col], label=f'Column {col}')

        plt.title('Columns')#تنظیم title
        plt.xlabel('Row')#نام خط افقی
        plt.ylabel('Value')#نام خط عمودی
        plt.legend()#تنظیم راهنمای نمودار
        plt.show()#نمایش دادن پلات
    else:
       
        return alert_big()
#ساخت دکمه 1
btn_open = tk.Button(frame, text="CSV Opener", command=open_file,
                     width=15, height=2, bg='#16efc8', font=custom_font)
btn_open.pack(pady=10)
#ساخت نوار تکس
entry = tk.Entry(frame, width=50, font=custom_font)
entry.pack(pady=10)
#ساخت دکمه 2
btn_url = tk.Button(frame, text="CSV URL Opener", command=open_url,
                    width=15, height=2, bg='#16efc8', font=custom_font)
btn_url.pack(pady=10)
#اجرای برنامه
root.mainloop()
