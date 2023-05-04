import subprocess
import tkinter
from tkinter import *
from tkinter import scrolledtext

def pinger():

    ip = ip_entry.get()
    count = int(count_entry.get())
    interval = int(interval_entry.get())
    ttl = int(ttl_entry.get())
    cmd = f'ping -c {count} -i {interval} -t {ttl} {ip}'
    results = subprocess.run(cmd.split(),capture_output=True)
    output_label.insert(tkinter.END,results)



root = Tk()
root.geometry('600x600')
root.title('Pinger')

#ip
iplabel = Label(root,text='Ip')
iplabel.pack()
ip_entry = Entry(root)
ip_entry.pack()

#count
count_label = Label(root,text='Count')
count_label.pack()
count_entry = Entry(root)
count_entry.pack()

#interval
interval_label = Label(root,text='Interval')
interval_label.pack()
interval_entry = Entry(root)
interval_entry.pack()

#TTL
ttl_label = Label(root,text="TTL")
ttl_label.pack()
ttl_entry = Entry(root)
ttl_entry.pack()


#output
output_label = scrolledtext.ScrolledText(root,height=10,width=50)
output_label.pack()


submitBtn = Button(root,text="Submit",command=pinger)
submitBtn.pack()


root.mainloop()