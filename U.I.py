import time
from tkinter import filedialog
import customtkinter
import subprocess
import threading
import queue

#customtkinter.ScalingTracker.set_user_scaling(0.5)
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

customtkinter.set_default_color_theme("dark-blue")
frames = []
counter=0
binary=0
module_counter=0
label=[]

def on_closing():
    app.destroy()


def clip_downloader():
    global counter
    frame_top.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    widgets = []
    counter += 1
    gray13="gray13"
    gray16 = "gray16"
    gray30="gray30"
    frame = customtkinter.CTkFrame(frame_top,bg_color=gray13)
    frame.columnconfigure(0, weight=1)
    # frame.grid(row=counter+1, column=0, sticky="we")
    if counter==1:
        frame.pack(padx=20,pady=(20,20),anchor="nw")
    else:
        frame.pack( padx=20, pady=(0, 20),anchor="nw")
    frames.append(frame)
    nested_frame= customtkinter.CTkFrame(frame,bg_color=gray13)
    nested_frame.grid(row=0, column=0, sticky="we",padx=20, pady=20)
    nested_frame.grid_columnconfigure(0,weight=1)


    title = customtkinter.CTkFrame(nested_frame, bg_color=gray16)
    title.grid(row=0, column=0, sticky="we")
    label2= customtkinter.CTkLabel(title, text="Thumbnail Maker", font=customtkinter.CTkFont(size=20, weight="bold"))
    label2.grid(row=0, column=0,pady=(0, 25))


    def maximize():
        editor_maximize.grid_forget()
        nested_frame.grid(row=0, column=0, sticky="we", padx=20, pady=20)
        frame_top.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    def minimize():
        nested_frame.grid_forget()
        editor_maximize.grid(row=0, column=4, sticky="we")
        frame_top.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    title.grid_columnconfigure(0, minsize=10)  # empty row with minsize as spacing
    title.grid_columnconfigure(5, weight=1)  # empty row as spacing
    title.grid_columnconfigure(8, minsize=20)  # empty row with minsize as spacing
    title.grid_columnconfigure(11, minsize=10)  # empty row with minsize as spacing

    editor_minimize = customtkinter.CTkButton(title, text="-", command=minimize,width=30)
    editor_minimize.grid(row=0, column=20, sticky="e")
    editor_maximize= customtkinter.CTkButton(frame, text="+", command=maximize, width=30)
    # stock_toggle_subtract = customtkinter.CTkButton(stock_input, text="-", command=stock_input_less_options,width=30)

    youtube_input=customtkinter.CTkFrame(nested_frame,bg_color=gray16)
    #youtube_input.columnconfigure(0, weight=1)
    youtube_input.grid(row=1, column=0, sticky="we")
    label = customtkinter.CTkLabel(youtube_input, text="Search Terms")
    label.grid(row=0, column=0, sticky="we" ,padx=(0, 35))

    widget = customtkinter.CTkEntry(youtube_input)
    widgets.append(widget)

    widget.grid(row=0, column=0, sticky="we")



    stock_input=customtkinter.CTkFrame(nested_frame,bg_color=gray16)
    stock_input.grid(row=2, column=0, sticky="we")
    label = customtkinter.CTkLabel(stock_input, text="Thumbnail Text")
    label.grid(row=0, column=0, sticky="we",padx=(0, 10))

    widget.grid(row=0, column=0, sticky="we")


    directory=customtkinter.CTkFrame(nested_frame,bg_color=gray16)
    directory.grid(row=5, column=0, sticky="we")
    label = customtkinter.CTkLabel(directory, text="Directory value: {Null}",font=customtkinter.CTkFont(size=15, weight="bold"))
    label.grid(row=0, column=0, sticky="we",padx=(0, 80),pady=(0,10))


    widgets2=[]
    audio_address = []


    Youtube_searchwords=[]
    Stock_searchwords=[]

    def thread():
        # Create a new thread to increment the progress bar
        print('queue starting')
        global label
        global module_counter


        Youtube_searchwords.append(widgets[0].get())
        # Stock search words

        Stock_searchwords.append(widgets[0].get())
        # Image search words

        print(Youtube_searchwords)
        print(Stock_searchwords)

        progress = customtkinter.CTkFrame(nested_frame, bg_color=gray16)
        progress.grid(row=13, column=0, sticky="we")
        progress.grid_columnconfigure(0,weight=1)
        progress_title= customtkinter.CTkLabel(progress, text="Processing")
        progress_title.grid(row=0, column=0, sticky="n",pady=(0,12))
        progressbar_1 = customtkinter.CTkProgressBar(master=progress)
        progressbar_1.grid(row=1, column=0, sticky="we")
        b7.grid_forget()
        # progressbar_1.set(0.4)
        progressbar_1.set(2)
        #youtube_input.grid_forget()
        stock_input.grid_forget()


        queue.put(lambda: nested_function (Youtube_searchwords,Stock_searchwords,progress,progressbar_1,progress_title))
        module_counter += 1
        label_1 = customtkinter.CTkLabel(master=frame_module, text=f"Module {module_counter}",
                                         font=customtkinter.CTkFont(size=12))  # font name and size in px
        label.append(label_1)
        while len(label) >= 35:
            label.pop(0)
        for i in range(len(label)):
            # label_1.grid(row=module_counter+i, column=0, pady=10, padx=70)
            label[i].grid(row=i + 1, column=0, pady=0, padx=20, sticky="w")

    def nested_function(topic,text,progress,progressbar_1,progress_title):
        global label
        global binary
        #binary = 0
        # search words
        import main
        import Base
        Base.thumbnail(topic,text)
        #thumbnail code

        progress_title.configure(progress, text="Finished")
        progressbar_1.set(10)



        label_1 = customtkinter.CTkLabel(master=frame_module, text="Module Completed",
                                         font=customtkinter.CTkFont(size=12))  # font name and size in px

        label.append(label_1)
        while len(label) >= 35:
            label.pop(0)
        for i in range(len(label)):
            label[i].grid(row=i + 1, column=0, pady=0, padx=20, sticky="w")

        binary = 0
    # activate =customtkinter.CTkFrame(frame)
    # activate.grid(row=12, column=0, sticky="we")
    b7 = customtkinter.CTkButton(nested_frame, text="Start", command=thread)
    b7.grid(row=12, column=0, sticky="we")




app = customtkinter.CTk()
app.geometry("1910x1080")
# self.minsize(App.WIDTH, App.HEIGHT)
app.title("Video Editor")
app.protocol("WM_DELETE_WINDOW", on_closing)  # call .on_closing() when app gets closed

# ============ create three frames ============

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

frame_left = customtkinter.CTkFrame(master=app,width=180,corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")

frame_right = customtkinter.CTkFrame(master=app)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
frame_right.grid_rowconfigure(0, weight=1)
frame_right.columnconfigure(0, weight=1)

frame_module = customtkinter.CTkFrame(master=app)
frame_module.grid(row=0, column=2, sticky="nswe")


# ============ frame_left ============

#queue functions

def process_queue():
    # Check if there are any functions in the queue
    # print("working")
    global binary
    x=5
    y=[7,3]
    if not queue.empty() and binary == 0:
        print(queue.qsize())
        binary = 1
        # Get the next function in the queue and call it
        func = queue.get()
        thread = threading.Thread(target=func)
        thread.start()
        # func()
        # Schedule this function to run again after 100ms
    app.after(100, process_queue)


# configure grid layout (1x13)
frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
frame_left.grid_rowconfigure(10, minsize=20)    # empty row with minsize as spacing
frame_left.grid_rowconfigure(13, minsize=10)  # empty row with minsize as spacing

label_1 = customtkinter.CTkLabel(master=frame_left,text="Video Editor Modes")  # font name and size in px
label_1.grid(row=1, column=0, pady=10, padx=10)

# button_1 = customtkinter.CTkButton(master=frame_left,text="Full Editor", fg_color=("gray75", "gray30"),command=full_editor)
# button_1.grid(row=2, column=0, pady=10, padx=20)

button_2 = customtkinter.CTkButton(master=frame_left,text="Clip Downloader",fg_color=("gray75", "gray30"),command=clip_downloader)
button_2.grid(row=5, column=0, pady=10, padx=20)


button_5 = customtkinter.CTkButton(master=frame_left,text="Edit Mode with audio",fg_color=("gray75", "gray30"),command=edit_mode_with_audio)
button_5.grid(row=6, column=0, pady=10, padx=20)

label_1 = customtkinter.CTkLabel(master=frame_left,text="Clip Downloader must be  \nused with Edit with Audio", font=customtkinter.CTkFont(size=13))  # font name and size in px
label_1.grid(row=13, column=0, pady=10, padx=10)

# ============ frame_main ============

frame_main = customtkinter.CTkFrame(frame_right,corner_radius=20,bg_color="gray10")
frame_main.grid(row=0, column=0,sticky='news')
frame_main.grid_rowconfigure(0, weight=1)
frame_main.columnconfigure(0, weight=1)

frame_canvas = customtkinter.CTkFrame(frame_main,corner_radius=20,bg_color="gray10",width=100)
frame_canvas.grid(row=0, column=0,sticky='news')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)

import win32gui
import win32con
import win32api

canvas = customtkinter.CTkCanvas(frame_canvas, bg='#000000', bd=0, highlightthickness=0, relief='ridge')
hwnd = canvas.winfo_id()
colorkey = win32api.RGB(0,0,0) #full black in COLORREF structure
wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,new_exstyle)
win32gui.SetLayeredWindowAttributes(hwnd,colorkey,255,win32con.LWA_COLORKEY)

canvas.grid(row=0, column=0, sticky="news")
canvas.grid_columnconfigure(0, weight=1)
canvas.grid_rowconfigure(0, weight=1)

vsb = customtkinter.CTkScrollbar(frame_canvas, command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

def on_resize(event):
    # Get the canvas width and height
    canvas_width = event.width
    # Resize the frame to fit the canvas
    frame_top.configure(width=canvas_width)

# set default values
frame_top=customtkinter.CTkFrame(canvas,bg_color="grey13")
canvas.create_window((0, 0), window=frame_top, anchor='nw')
canvas.bind("<Configure>", on_resize)


# ============ frame_module ============

# frame_module.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
# frame_module.grid_rowconfigure(7, weight=1)  # empty row as spacing
# frame_module.grid_rowconfigure(10, minsize=20)    # empty row with minsize as spacing
# frame_module.grid_rowconfigure(13, minsize=10)  # empty row with minsize as spacing

label_1 = customtkinter.CTkLabel(master=frame_module,text="Module", font=customtkinter.CTkFont(size=15))  # font name and size in px
label_1.grid(row=0, column=0, pady=10, padx=70)



queue = queue.Queue()

process_queue()

app.mainloop()
