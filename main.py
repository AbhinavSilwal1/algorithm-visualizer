import tkinter as tk
import random


ARRAY_SIZE = 50
ARRAY_MIN = 10
ARRAY_MAX = 500


class AlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        title_label = tk.Label(
            root,
            text="Algorithm Visualizer",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

        # Buttons Frame
        controls_frame = tk.Frame(root)
        controls_frame.pack(pady=10)

        generate_button = tk.Button(
            controls_frame,
            text="Generate Array",
            command=self.generate_array
        )
        generate_button.pack(side="left", padx=10)

        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=800,
            height=400,
            bg="white"
        )
        self.canvas.pack(pady=20)

        self.array = []

        self.generate_array()

    def generate_array(self):
        self.array = [
            random.randint(ARRAY_MIN, ARRAY_MAX)
            for _ in range(ARRAY_SIZE)
        ]

        self.draw_array()

    def draw_array(self):
        self.canvas.delete("all")

        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill="skyblue",
                outline=""
            )


def main():
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()