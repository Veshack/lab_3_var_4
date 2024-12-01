import tkinter as tk
import random
import string
from pygame import mixer

mixer.init() 
mixer.music.load("banditi8bit.mp3") 
mixer.music.play(999)

def cancel():
    window.destroy()

def word_choose():
    letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first_block = ""
    second_block = ""
    third_block = ""
    ratio_1 = 0
    ratio_2 = 0
    ratio_3 = 0
    while ratio_1 < 30 or ratio_1 > 35:
        first_block = ""
        ratio_1 = 0
        for i in range(4):
            a = random.randint(0, len(letter_list)-1)
            first_block += letter_list[a]
            ratio_1 += a + 1
    while ratio_2 < 30 or ratio_2 > 35:
        second_block = ""
        ratio_2 = 0
        for i in range(4):
            a = random.randint(0, len(letter_list)-1)
            second_block += letter_list[a]
            ratio_2 += a + 1
    while ratio_3 < 30 or ratio_3 > 35:
        third_block = ""
        ratio_3 = 0
        for i in range(4):
            a = random.randint(0, len(letter_list)-1)
            third_block += letter_list[a]
            ratio_3 += a + 1
    return first_block + "-" + second_block + "-" + third_block

def animate_label(duration=2000):
    animate(duration)

def stop_animation(final_word):
    word_label.configure(text=final_word)  # Показать окончательное слово после анимации

def animate(duration):
    if duration > 0:
        new_text = generate_random_format()
        word_label.configure(text=new_text)
        window.after(50, lambda: animate(duration - 50))  # Уменьшаем оставшееся время на 50 мс
    else:
        final_word = word_choose()  # Генерируем окончательное слово
        stop_animation(final_word)

def generate_random_format():
    return ''.join(random.choice(string.ascii_uppercase) if char != '-' else '-' for char in "XXXX-XXXX-XXXX")

def generatio():
    word_label.configure(text='XXXX-XXXX-XXXX')  # Сброс текста перед анимацией
    animate_label()

window = tk.Tk()
window.title('My app')
window.geometry('300x300')
bg_img = tk.PhotoImage(file='pic.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

word_label = tk.Label(window, text='XXXX-XXXX-XXXX', font=('Consolas', 26), 
                      bg='black', fg='white', borderwidth=1, relief="ridge")
word_label.place(relx=0.05, rely=0.4, relwidth=0.9)

btn_guess = tk.Button(window, text='Generate', width=15, command=generatio)
btn_guess.place(relx=0.07, rely=0.7)
btn_cancel = tk.Button(window, text='Cancel', width=15, command=cancel)
btn_cancel.place(relx=0.55, rely=0.7)

window.mainloop()


