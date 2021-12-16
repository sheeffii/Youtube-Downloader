import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox



root = tk.Tk()

root.geometry("600x120")
root.resizable(False,False)

root.title("Yotube Downloader from SHS")
root.config(background="#001219")








def createlabels():
    link_label = Label(root, text="Youtube URL:", bg="#E8d579")
    link_label.grid(row=1, column=0, padx=5, pady=5)

    root.link_text = Entry(root,width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, padx=5, pady=5)

    location_label = Label(root, text='Location: ', bg="#E8d579")
    location_label.grid(row=2, column=0, pady=5, padx=5)

    root.location_text = Entry(root, width=45, textvariable=download_path)
    root.location_text.grid(row=2, column=1, pady=3, padx=3)


    browse_button = Button(root, text='Browse', command=browse, width=10, bg="#05E8E0")
    browse_button.grid(row=2, column=2, pady=1, padx=1 )

    download_buton = Button(root,text='Download Video', command=download_video, width=25, bg="#05E8E0")
    download_buton.grid(row=3, column=1, pady=3,padx=3)


def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Director Path")
    download_path.set(download_dir)

def download_video():

    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)

    
    messagebox.showinfo("Succes!!", "Download Successfully, You will find your video at\n" + folder)




video_link = StringVar()
download_path = StringVar()

createlabels()

root.mainloop()