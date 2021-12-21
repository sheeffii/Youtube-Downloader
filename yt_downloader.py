from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox



root =Tk()

#Setting sizes for the window
root.geometry("600x120")
root.resizable(False,False)

root.title("Yotube Downloader from SHS")
root.config(background="#001219")





#frontend 
def createlabels():

    # creating a label for link
    link_label = Label(root, text="Youtube URL:", bg="#E8d579")
    #grid allows us to place the link_label
    link_label.grid(row=1, column=0, padx=5, pady=5)

    #creating a entry for input
    root.link_text = Entry(root,width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, padx=5, pady=5)

    location_label = Label(root, text='Location: ', bg="#E8d579")
    location_label.grid(row=2, column=0, pady=5, padx=5)
    
    root.location_text = Entry(root, width=45, textvariable=download_path)
    root.location_text.grid(row=2, column=1, pady=3, padx=3)

    # creating a button  that will call the browse function
    browse_button = Button(root, text='Browse', command=browse, width=10, bg="#05E8E0")
    browse_button.grid(row=2, column=2, pady=1, padx=1 )

    download_button = Button(root,text='Download Video', command=download_video, width=25, bg="#05E8E0")
    download_button.grid(row=3, column=1, pady=3,padx=3)



#backend
def browse():
    #asking user for their directory
    download_dir = filedialog.askdirectory(initialdir="/", title='Please select a directory')
    #it will show your directory in entry point
    download_path.set(download_dir)

def download_video():
    #get url from video_link
    url = video_link.get()
    #folder where we want to download the video
    folder = download_path.get()

    #different streams of the video are fetched
    get_video = YouTube(url)
    #getting the highest resolution of the video
    get_stream = get_video.streams.get_highest_resolution()
    #download the video to the user folder
    get_stream.download(folder)

    
    messagebox.showinfo("Succes!!", "Download Successfully, You will find your video at\n" + folder)




video_link = StringVar()
download_path = StringVar()

#calling the function 
createlabels()

root.mainloop()