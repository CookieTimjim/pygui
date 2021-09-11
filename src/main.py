import tkinter as tk

# Button logic
def settings():
    pass

def answer():
    pass

def next_question():
    pass




question = 'This is a flash card question, I have made it quite a long string to test for text wrapping and space.'
answer = 'The answer is simple, there is more than enough space and text wrapping works perfectly :)'

# Question window generation
window = tk.Tk()
window.configure(bg='#2F3136')
window.geometry('400x240')

window.title('Flash cards')

# Outlines
textframe = tk.Frame(window, bg='#2F3136')
textframe.place(height=160, width=380, x=10, y=10)
buttonframe = tk.Frame(window, bg='#0313ff')
buttonframe.place(height=40, width=380, x=10, y=190)

questionlabel = tk.Label(
                        textframe,
                        text=question,
                        fg='white',
                        bg='#2F3136',
                        font=('Roboto', 13),
                        wraplength=380,
                        justify=tk.LEFT
                        ).pack(anchor=tk.NW)

answerlabel = tk.Label(
                        textframe,
                        text=answer,
                        fg='white',
                        bg='#2F3136',
                        font=('Roboto', 13),
                        wraplength=380,
                        justify=tk.LEFT
                        ).pack(anchor=tk.NW)

settingsbutton = tk.Button(buttonframe, text='Settings').grid(column=0, row=0)
answerbutton = tk.Button(buttonframe, text='Answer').grid(column=1, row=0)
nextbutton = tk.Button(buttonframe, text='Next').grid(column=2, row=0)

window.resizable(False, False)
window.mainloop()

