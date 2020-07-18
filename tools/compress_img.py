# encoding: utf-8

from tkinter import *
from tkinter.filedialog import *
# PIL中的Image与tkinter中的Image重名
from PIL import Image as Img

# ui
# ui update
# business

info = {
    'path': []
}


def make_app():
    app = Tk()
    Label(app, text='Image Compression').pack()
    Listbox(app, name='listbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=ui_get_data).pack()
    Button(app, text='compress', command=compress).pack()
    app.geometry('300x400')
    return app


def ui_get_data():
    f_names = askopenfilenames()
    listbox = app.children['listbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            listbox.insert(END, name.split('/')[-1])


def compress():
    for f_path in info['path']:
        output = '/Users/user/Desktop/output/'
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        image.save(output+'c_'+name, quality=60)


app = make_app()
app.mainloop()
