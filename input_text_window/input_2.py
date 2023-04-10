import tkinter as tk

result = []


def create_input_window():
    def confirm_input():
        result.append(input_field.get())
        window.destroy()

    def cancel_input():
        window.destroy()

    # Create a new window
    window = tk.Tk()

    # Set the height of the window to 100 pixels
    window.geometry('580x240')

    # Disable the ability to resize the window
    window.resizable(False, False)

    # Set the title of the window
    window.title("Input Window")

    # Set the input label
    tk.Label(window, text="Enter your information:").grid(row=0, column=0)

    # Set the input text field
    input_field = tk.Text(window, height=8, wrap="word")
    input_field.grid(row=1, column=0, sticky="WE")

    # Set the button to submit the information
    submit_button = tk.Button(window, text="Submit", command=confirm_input)
    submit_button.grid(row=2, column=0, pady=5)

    # Set the button to cancel the input
    cancel_button = tk.Button(window, text="Cancel", command=cancel_input)
    cancel_button.grid(row=3, column=0)

    # Run the window
    window.mainloop()
    return result


# Call the function to create the input window
print(create_input_window())
