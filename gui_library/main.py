# gui -> memakai inveroment pakai ui sama ux atuh

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

app = tk.Tk()
app.configure(bg="white")
app.geometry("300x200")
app.resizable(False,False)
app.title("sapa dia")

# frae input
input_frame = ttk.Frame(app)
# penempatana grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# var
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# funsgi
def tombol_klik():
    pask = f"hai {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, ganteng "
    showinfo(title="hay", message=pask)


# komponen-komponnen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="nama depan")
nama_depan_label.pack(fill="x",expand=True,padx=10)


# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN )
nama_depan_entry.pack(fill="x",expand=True,padx=10)

# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="nama belakang")
nama_belakang_label.pack(fill="x",expand=True,padx=10)


# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(fill="x",expand=True,padx=10)


# 5. tombol

tombol = ttk.Button(input_frame,text="sapa!", command=tombol_klik)
tombol.pack(fill="x", expand=True,padx=10,pady=10 )

# 6 looping  
app.mainloop()