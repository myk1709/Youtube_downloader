from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import math,os
from pytube import YouTube
#---------------------constants-----------------------#
LIGHT_YT_BACK = '#f4f9f9'
LIGHT_LOGO = 'ytred.png'
DARK_YT_BACK = '#2c394b'
DARK_LOGO = 'ytdark.png'
mode_on = 'light'

#-----------------dark Mode---------------------------#

    
#-----------------------------------------------------#
#-------------------------youtube download------------#
def progressUpdate(fs,fn):
    progress.grid(row=7,column=1,columnspan=3)
    file_size = os.path.getsize(f'/Users/mayanksharma/Desktop/Python-new/self_project/youtube-downloader/{fn}')
    print(file_size,fs)
    
def download():
    link = e1.get()
    try:
        yt = YouTube(link)
    except:
        l2.config(text='Please Check the link')
        print('error')
    else:
        res = resolution.get()
        l2.config(text='')
        ys = yt.streams.get_by_resolution(str(res))
        fs = yt.streams.filter().get_by_resolution(str(res)).filesize
        fn = yt.streams.filter().get_by_resolution(str(res)).default_filename
        ys.download('/Users/mayanksharma/Desktop/Python-new/self_project/youtube-downloader')
        print(fs,fn)
        progressUpdate(fs,fn)
        



#--------------------------UI---------------------------#
window = Tk()
window.title('Youtube Video Downloader')
window.config(padx=100,pady=50)

imgOld = Image.open(LIGHT_LOGO)
imgNew = imgOld.resize((300,300))
logoOld = Image.open('light_mode.png')
logoNew = logoOld.resize((math.floor(logoOld.width/11),math.floor(logoOld.height/11)))

img = ImageTk.PhotoImage(imgNew)
logoImg = ImageTk.PhotoImage(logoNew)

'''
button_mode = Button(window,image=logoImg,borderwidth=0,highlightthickness=0)
#button_mode.grid(row=0,column=0)
button_mode.pack(side=TOP)
'''

canvas = Canvas(window,width=300,height=300)
canvas.create_image(150,150,image = img)

canvas.grid(row=1,column=1)
#canvas.pack()



l1 = Label(window,text='Please enter link',font=('Ubuntu',20,'bold'))
l1.grid(row=2,column=1)
#l1.pack()

l2 = Label(window,text = '',fg='#E63E6D')
l2.grid(row=3,column=1)

e1 = Entry(window,width=40)
e1.grid(row=4,column=1)
#e1.pack()


res_label = Label(text='Select Resolution')
res_label.grid(row=5,column=0)

resolution = ttk.Combobox(window)
resolution['values']= ('720p', '480p', '360p', '240p', '144p')
resolution.grid(row=5,column=1)

b1 = Button(text='Get Video',width=30,command = download)
b1.grid(row=6,column=0,columnspan=2)
#b1.pack(side= LEFT,pady=20)

progress = ttk.Progressbar(window,orient='horizontal',length=100,mode='determinate')
#progress.pack(fill=BOTH,expand=True)

window.mainloop()