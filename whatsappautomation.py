import tkinter as tk
import datetime
from twilio.rest import Client
from tkinter import messagebox

account_sid = '[Acc_sid]'
auth_token = '[Auth token]'
client = Client(account_sid, auth_token)

def SendMsg(msg):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=msg,
        to='whatsapp:+919836117995'
        )
    exit()

def CheckTime(tm,msg):
    while True:
        if datetime.datetime.now().strftime('%H:%M')==tm:
            SendMsg(msg)
            break;

def AddReminder(hr,mn,md,msg):
    main.destroy()
    print('Reminder created.')
    if md=='PM':
        hr=str(int(hr)+12);
    elif md=='AM' and hr=='12':
        hr='00'
    time_str=f'{hr}:{mn}'
    CheckTime(time_str,msg)

def UpButton(limit,field,addvalue):
    value=int(field.get())
    if value+addvalue>=limit:
        field.delete(0, tk.END)
        field.insert(tk.END, str(value-limit+1).zfill(2))
        return
    else:
        field.delete(0,tk.END)
        field.insert(tk.END,str(value+1).zfill(2))

def DownButton(limit,field,check_value):
    value=int(field.get())
    if value-1<check_value:
        field.delete(0, tk.END)
        field.insert(tk.END,limit-1)
        return
    else:
        field.delete(0,tk.END)
        field.insert(tk.END,str(value-1).zfill(2))

def MeridianShift(button,field):
    if field.get()=='AM':
        button.config(text='AM')
        field.delete(0, tk.END)
        field.insert(tk.END,'PM')
    else:
        button.config(text='PM')
        field.delete(0, tk.END)
        field.insert(tk.END, 'AM')

main=tk.Tk()
main.geometry('200x200')
main.title("Work planar")
tk.Label(text='Add Work',fg='Blue',font=('Ariel',12)).pack()
timepanel=tk.Frame(main)
timepanel.pack(pady=5)

up_img=tk.PhotoImage(file="up.png")
down_img=tk.PhotoImage(file="down.png")

hour=tk.Entry(timepanel,width=2,font=(16))
hour.insert(tk.END,'12')
hour.grid(row=1,column=0,padx=5)

tk.Label(timepanel,text=':').grid(row=1,column=1)

min=tk.Entry(timepanel,width=2,font=(16))
min.insert(tk.END,'00')
min.grid(row=1,column=2,padx=5)

meridian_segment=tk.Entry(timepanel,width=3,font=(16))
meridian_segment.insert(tk.END,'AM')
meridian_segment.grid(row=1,column=3,padx=5)

hour_up=tk.Button(timepanel,image=up_img,height=10,width=13,command=lambda : UpButton(12,hour,0))
hour_up.grid(row=0,column=0)
hour_down=tk.Button(timepanel,image=down_img,height=10,width=13, command=lambda : DownButton(13,hour,1))
hour_down.grid(row=2,column=0)

min_up=tk.Button(timepanel,image=up_img,height=10,width=13,command=lambda : UpButton(60,min,1))
min_up.grid(row=0,column=2)
min_down=tk.Button(timepanel,image=down_img,height=10,width=13, command=lambda : DownButton(60,min,0))
min_down.grid(row=2,column=2)

meridian_switch=tk.Button(timepanel,text='PM',command=lambda : MeridianShift(meridian_switch,meridian_segment))
meridian_switch.grid(row=1,column=4)

tk.Label(text='Note:').pack()
note=tk.Text(main,height=3,width=20)
note.pack(pady=3)

add_reminder=tk.Button(main,text='Add Reminder',font=('Ariel','12'),bg='Blue',fg='White',command=lambda : AddReminder(hour.get(),min.get(),meridian_segment.get(),note.get(1.0,'end-1c')))
add_reminder.pack()
main.mainloop()