from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Kasir Sederhana')

# variabel
Chattime_Milk_Tea           = StringVar()
Chattime_Roasted_Milk_Tea   = StringVar()
Jasmine_Green_Milk_Tea      = StringVar()
Hazelnut_Chocolate_milk_Tea = StringVar()
Taro_Milk_Tea               = StringVar()
Vanilla_Milk_Tea            = StringVar()
Caramel_Milk_Tea            = StringVar()
Honeyn_Milk_Tea             = StringVar()
Matcha_Milk_Tea             = StringVar()
Authentic_Thai_Tea          = StringVar()
tekstotal                   = StringVar()
teksaung                    = StringVar()
total                       = 0

# buat function
def totalbeli():
    global Chattime_Milk_Tea, Chattime_Roasted_Milk_Tea, Jasmine_Green_Milk_Tea, Hazelnut_Chocolate_milk_Tea, Taro_Milk_Tea, Vanilla_Milk_Tea, Caramel_Milk_Tea, Honeyn_Milk_Tea, Matcha_Milk_Tea, Authentic_Thai_Tea, tekstotal, total
    Minuman_Pertama         = int(Chattime_Milk_Tea.get())              * 22000
    Minuman_kedua           = int(Chattime_Roasted_Milk_Tea.get())      * 22000
    Minuman_Ketiga          = int(Jasmine_Green_Milk_Tea.get())         * 25000
    Minuman_Keempat         = int(Hazelnut_Chocolate_milk_Tea.get())    * 25000
    Minuman_Kelima          = int(Taro_Milk_Tea.get())                  * 25000
    Minuman_Keenam          = int(Vanilla_Milk_Tea.get())               * 24000
    Minuman_Ketujuh         = int(Caramel_Milk_Tea.get())               * 23000
    Minuman_Kedelapan       = int(Honeyn_Milk_Tea.get())                * 23000
    Minuman_Kesembilan      = int(Matcha_Milk_Tea.get())                * 23000
    Minuman_Kesepuluh       = int(Authentic_Thai_Tea.get())             * 22000
    
    total = Minuman_Pertama + Minuman_kedua   + Minuman_Ketiga  + Minuman_Keempat + Minuman_Kelima + Minuman_Keenam + Minuman_Ketujuh + Minuman_Kedelapan + Minuman_Kesembilan + Minuman_Kesepuluh
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksaung.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian Kamu Sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='Maaf Uang Kamu Kurang')

def clear():
        Chattime_Milk_Tea.set('0')
        Chattime_Roasted_Milk_Tea.set('0')
        Jasmine_Green_Milk_Tea.set('0')
        Hazelnut_Chocolate_milk_Tea.set('0')
        Taro_Milk_Tea.set('0')
        Vanilla_Milk_Tea.set('0')
        Caramel_Milk_Tea.set('0')
        Honeyn_Milk_Tea.set('0')
        Matcha_Milk_Tea.set('0')
        Authentic_Thai_Tea.set('0')
        tekstotal.set('0')
        teksaung.set('0')


app.geometry('650x700') # membuat ukuran
app.configure(bg='#31c6d4') # membuat backgroung warna

# membuat properti tulisan title
Label(app, text='KASIR TOKO MINUMAN', bg='#31c6d4', foreground='#fef5ac', font='arial 18 bold').place(x=200,y=20)
Label(app, text='==========  Daftar Menu  ==========', bg='#31c6d4', foreground='#fef5ac', font='arial 14 bold').place(x=160,y=60)

# membuat label nama menu
Label(app, text='1.     Chattime Milk Tea',                 bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=100)
Label(app, text='2.     Chattime Roasted Milk Tea',         bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=140)
Label(app, text='3.     Jasmine Green Milk Tea',            bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=180)
Label(app, text='4.     Hazelnut Chocolate milk Tea',       bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=220)
Label(app, text='5.     Taro Milk Tea',                     bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=260)
Label(app, text='6.     Vanilla Milk Tea',                  bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=300)
Label(app, text='7.     Caramel Milk Tea',                  bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=340)
Label(app, text='8.     Honeyn Milk Tea',                   bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=380)
Label(app, text='9.     Matcha Milk Tea',                   bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=420)
Label(app, text='10.    Authentic Thai Tea',                bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=460)


# membuat label harga
Label(app, text='Rp. 22000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=100)
Label(app, text='Rp. 22000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=140)
Label(app, text='Rp. 25000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=180)
Label(app, text='Rp. 25000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=220)
Label(app, text='Rp. 25000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=260)
Label(app, text='Rp. 24000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=300)
Label(app, text='Rp. 23000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=340)
Label(app, text='Rp. 23000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=380)
Label(app, text='Rp. 23000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=420)
Label(app, text='Rp. 22000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=460)

# membuat spinbox
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Chattime_Milk_Tea,             command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Chattime_Roasted_Milk_Tea,     command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Jasmine_Green_Milk_Tea,        command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Hazelnut_Chocolate_milk_Tea,   command=totalbeli).place(x=550,y=220)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Taro_Milk_Tea,                 command=totalbeli).place(x=550,y=260)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Vanilla_Milk_Tea,              command=totalbeli).place(x=550,y=300)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Caramel_Milk_Tea ,             command=totalbeli).place(x=550,y=340)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Honeyn_Milk_Tea ,              command=totalbeli).place(x=550,y=380)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Matcha_Milk_Tea,               command=totalbeli).place(x=550,y=420)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Authentic_Thai_Tea,            command=totalbeli).place(x=550,y=460)
# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#31c6d4', foreground='#fef5ac', font='arial 12 ').place(x=100,y=540)

# membuat entry jumlah uang
Entry(app, textvariable=teksaung, width=20).place(x=100,y=570)

# membuat label total
Label(app, text='Total',            bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=300,y=500)
Label(app, text='Rp. ',             bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=400,y=500)
Label(app, textvariable=tekstotal,  bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=430,y=500)

# membuat tombol
Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=600)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=600)

# footer text
Label(app, text='Created by IDF', bg='#31c6d4', foreground='#fef5ac', font='arial 10 ').place(x=300,y=650)

app.mainloop() # menampilkan aplikasi