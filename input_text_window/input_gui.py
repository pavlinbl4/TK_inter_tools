import tkinter as tk

result = []


def input_window():
    def confirm_input():
        result.append(entry.get())
        root.destroy()

    def cancel_input():
        root.destroy()

    root = tk.Tk()
    root.geometry('300x150+' + str(root.winfo_screenwidth() // 9) + '+' + str(root.winfo_screenheight() // 3))

    label = tk.Label(root, text="Enter information:")
    label.pack(pady=15)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    confirm_button = tk.Button(root, text="Confirm", command=confirm_input)
    confirm_button.pack()

    cancel_button = tk.Button(root, text="Cancel", command=cancel_input)
    cancel_button.pack()

    root.mainloop()
    return result


if __name__ == '__main__':
    print(input_window())
