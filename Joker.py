import Tkinter as tk

words="""this is a really large file, it has a lot of words"""*25

args=['end']
for i,w in enumerate(words.split()):
   args.extend((w+' ','TAG%d'%i))


root=tk.Tk()
text=tk.Text(root)
text.grid(row=0,column=0)
text.insert(*args)
root.mainloop()