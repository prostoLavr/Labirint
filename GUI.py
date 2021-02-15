import tkinter as tk


master = tk.Tk()
master.title('Labirint')


def do_print(event=None):
    msg = ent.get()
    lst_box.configure(state='normal')
    lst_box.insert(tk.END, f'\nYou: {msg}')
    lst_box.delete('1.0', 'end')
    lst_box.configure(state='disabled')
    ent_txt.set('')


label = tk.Label(master, text='header label')
label.pack()

lst_group = tk.Frame(master)
scroll = tk.Scrollbar(lst_group)
lst_box = tk.Text(lst_group, height=15, width=50, yscrollcommand=scroll.set)
lst_box.insert(tk.END, f'First')
lst_box.configure(state='disabled')
scroll.pack(side=tk.RIGHT, fill=tk.Y)
lst_box.pack(side=tk.LEFT, fill=tk.BOTH)
lst_group.pack()


input_group = tk.Frame(master)
in_label = tk.Label(input_group, text='Варианты ввода')
line_group = tk.Frame(master)
ent_txt = tk.StringVar()
ent = tk.Entry(line_group, textvariable=ent_txt)
ent.bind('<Return>', do_print)
send = tk.Button(line_group, text='send!', command=do_print)
ent.grid(row=0, column=0)
send.grid(row=0, column=1)

line_group.pack()
in_label.pack()
input_group.pack()

master.mainloop()
