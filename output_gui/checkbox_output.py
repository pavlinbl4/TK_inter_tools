import tkinter as tk


def create_checkbox_list(words):
    def submit():
        for i, word in enumerate(words):
            if checkboxes[i].get() == 1:
                selected_words.append(word)
        window.destroy()

    h = 30 * (len(words) % 10 + 10)
    l = 200 + 140 * ((len(words) // 10))
    window = tk.Tk()
    window.geometry(f"{l}x{h}")
    window.title("Checkbox List")

    checkboxes = []
    for i, word in enumerate(words):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=word.strip(), variable=var, onvalue=1, offvalue=0)
        checkbox.grid(row=i % 10, column=1 + i // 10, padx=30, pady=5, sticky='W')
        checkboxes.append(var)

    submit_button = tk.Button(window, text="Submit", command=submit)
    # submit_button.grid(row=i + 1, column=0, columnspan=len(words), padx=50, pady=5)
    submit_button.grid(row=i + 1, column=0, columnspan=len(words), pady=35)

    window.mainloop()
    return selected_words


def create_checkbox_dict(category_dict):
    words = [k for k in category_dict.keys()]

    def submit():
        for i, word in enumerate(words):
            if checkboxes[i].get() == 1:
                selected_words.append(word)
        window.destroy()

    h = 30 * (len(words) + 5)
    l = 200 + 140 * ((len(words) // 10))
    window = tk.Tk()
    window.geometry(f"{l}x{h}")
    window.title("Checkbox List")

    checkboxes = []
    for i, word in enumerate(words):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=word.strip(), variable=var, onvalue=1, offvalue=0)
        checkbox.grid(row=i, column=1, padx=30, pady=5, sticky='W')
        checkboxes.append(var)

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=i + 1, column=1, columnspan=len(words), pady=45)

    window.mainloop()
    return category_dict[selected_words[0]]


if __name__ == '__main__':
    selected_words = []

    category_dict = {'Культура': '1000000', 'Правосудие': '2000000', 'Происшествия и конфликты': '3000000',
                     'Экономика и бизнес': '4000000', 'Образование': '5000000', 'Экология': '6000000',
                     'Медицина': '7000000', 'Светская жизнь': '8000000', 'Досуг, туризм и отдых': '10000000',
                     'Политика': '11000000', 'Религия': '12000000', 'Наука': '13000000', 'Общество': '14000000',
                     'Спорт': '15000000', 'Армия и ВПК': '16000000', 'Окружающая среда': '18000000'}

    # _words = create_checkbox_list(
    #     ["industrialisation", "apple", 'melon', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box',
    #      'knife',
    #      'bread', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box', 'knife', 'bread',
    #      "industrialisation",
    #      "industrialisation", "apple", 'melon', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box',
    #      'knife',
    #      'bread', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box'])
    # print(_words)
    print(create_checkbox_dict(category_dict))
