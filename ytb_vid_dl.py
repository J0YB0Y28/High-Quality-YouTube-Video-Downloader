from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('700x300')
root.resizable(0, 0)
root.title("Téléchargeur de vidéo YouTube")

Label(root, text='Copiez le lien de la vidéo YouTube que vous voulez télécharger',
      font='arial 15 bold').pack()

# enter link
link = StringVar()

Label(root, text='Copiez le lien ici :', font='arial 15 bold').place(x=270, y=60)
Entry(root, width=80, textvariable=link).place(x=32, y=90)

# function to download video


def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Téléchargement terminé', font='arial 15').place(x=270, y=210)


Button(root, text='TÉLÉCHARGER', font='arial 15 bold', bg='white',
       padx=2, command=Downloader).place(x=280, y=150)

root.mainloop()