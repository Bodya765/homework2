import tkinter as tk

def create_click_counter_app():
    root = tk.Tk()
    root.title("Click Counter App")

    click_count = {"value": 0}

    label = tk.Label(root, text="Натисніть кнопку", font=("Helvetica", 14))
    label.pack(pady=20)

    def change_text():
        click_count["value"] += 1
        text = "Hello" if click_count["value"] % 2 == 1 else "Натисніть кнопку"
        label.config(text=text)
        root.title(f"Click Counter App - Кількість кліків: {click_count['value']}")

    button = tk.Button(root, text="Змінити напис", command=change_text)
    button.pack()

    return root

if __name__ == "__main__":
    app = create_click_counter_app()
    app.mainloop()
