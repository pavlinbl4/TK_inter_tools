import tkinter as tk


def create_checkbox_list(words):

    def submit():
        selected_words = [word for i, word in enumerate(words) if checkboxes[i].get() == 1]
        window.destroy()
        return selected_words

    window = tk.Tk()
    window.geometry("300x200")
    window.title("Checkbox List")

    checkboxes = []
    for i, word in enumerate(words):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=word, variable=var, onvalue=1, offvalue=0)
        checkbox.grid(row=i, column=0, padx=5, pady=5)
        checkboxes.append(var)

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=i + 1, column=0, columnspan=len(words), padx=5, pady=5)

    window.mainloop()
    return selected_words


# Example usage

words = ["apple", "banana", "cherry", "durian"]

selected_words = create_checkbox_list(words)
print(selected_words)
