import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    root.geometry("900x600")
    root.resizable(False, False)

    title_label = tk.Label(
        root,
        text="Algorithm Visualizer",
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()