import webbrowser
import os
import time



youtube="www.youtube.com"
google="www.google.com"
a=input("Do you want to open youtube or google or textfile?")
if(a=='y'):
   webbrowser.open_new(youtube)
elif (a=='g'):
      webbrowser.open_new(google)
else:
  os.startfile("C:\\Users\\HP\\Desktop\\New folder")

