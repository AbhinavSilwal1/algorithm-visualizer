import tkinter as tk
from tkinter import messagebox
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort

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

        # Legend Button
        legend_button = tk.Button(
            root,
            text="Legend",
            font=("Arial", 10),
            command=self.show_legend
        )
        legend_button.place(x=20, y=15)

        # Buttons Frame
        controls_frame = tk.Frame(root)
        controls_frame.pack(pady=10)

        # Generate Array Button
        generate_button = tk.Button(
            controls_frame,
            text="Generate Array",
            command=self.generate_array
        )
        generate_button.pack(side="left", padx=10)

        # Bubble Sort Button
        bubble_sort_button = tk.Button(
            controls_frame,
            text="Start Bubble Sort",
            command=self.start_sorting
        )
        bubble_sort_button.pack(side="left", padx=10)

        # Selection Sort Button
        selection_sort_button = tk.Button(
            controls_frame,
            text="Start Selection Sort",
            command=self.start_selection_sort
        )
        selection_sort_button.pack(side="left", padx=10)

        # Insertion Sort Button
        insertion_sort_button = tk.Button(
            controls_frame,
            text="Start Insertion Sort",
            command=self.start_insertion_sort
        )
        insertion_sort_button.pack(side="left", padx=10)

        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=800,
            height=400,
            bg="white"
        )
        self.canvas.pack(pady=20)
        
        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 11)
        )
        self.status_label.pack(pady=5)

        self.array = []
        self.comparisons = 0
        self.swaps = 0

        self.generate_array()

    # Generates a new random array and resets the display.
    def generate_array(self):
        self.array = [
            random.randint(ARRAY_MIN, ARRAY_MAX)
            for _ in range(ARRAY_SIZE)
        ]
        self.status_label.config(text="")
        self.draw_array()

    # Displays the color legends for different sorting algorithms.
    def show_legend(self):
        messagebox.showinfo(
            "Sorting Color Legends",
            "Bubble Sort:\n"
            "Blue = Unsorted\n"
            "Red = Comparing\n"
            "Green = Sorted\n\n"

            "Selection Sort:\n"
            "Blue = Unsorted\n"
            "Red = Comparing\n"
            "Green = Sorted\n"
            "Purple = Current Position\n"
            "Orange = Current Minimum\n\n"

            "Insertion Sort:\n"
            "Blue = Unsorted\n"
            "Red = Comparing\n"
            "Green = Sorted\n"
            "Purple = Current Key"
        )

    # Starts the Bubble Sort animation.
    def start_sorting(self):
        self.comparisons = 0
        self.swaps = 0
        self.sorting_generator = bubble_sort(self.array)
        self.animate_sorting()

    # Animates Bubble Sort one generator step at a time.
    def animate_sorting(self):
        try:
            array_state, index1, index2, sorted_start_index, swapped = next(
                self.sorting_generator
            )

            if index1 is not None and index2 is not None:
                self.comparisons += 1

                if swapped:
                    self.swaps += 1
                    action_text = "Swapped"
                else:
                    action_text = "No swap needed"

                self.status_label.config(
                    text=(
                        f"Comparing index {index1} and {index2} | "
                        f"{action_text} | "
                        f"Comparisons: {self.comparisons} | "
                        f"Swaps: {self.swaps}"
                    )
                )

            self.draw_array(
                highlight_indices=[index1, index2],
                sorted_start_index=sorted_start_index
            )

            self.root.after(150, self.animate_sorting)

        except StopIteration:
            self.draw_array()
            self.status_label.config(
                text=(
                    f"Bubble Sort Complete! "
                    f"Comparisons: {self.comparisons} | "
                    f"Swaps: {self.swaps}"
                )
            )

    # Starts the Selection Sort animation.
    def start_selection_sort(self):
        self.comparisons = 0
        self.swaps = 0

        self.sorting_generator = selection_sort(self.array)
        self.animate_selection_sorting()

    # Animates Selection Sort one generator step at a time.
    def animate_selection_sorting(self):
        try:
            array_state, current_index, comparing_index, min_index, sorted_boundary, swapped = next(
                self.sorting_generator
            )

            if current_index is not None and comparing_index is not None:
                self.comparisons += 1

                if swapped:
                    self.swaps += 1
                    action_text = "Swapped current value with minimum value"
                else:
                    action_text = "Searching for the minimum value"

                self.status_label.config(
                    text=(
                        f"Current index: {current_index} | "
                        f"Comparing index: {comparing_index} | "
                        f"Minimum index: {min_index} | "
                        f"{action_text} | "
                        f"Comparisons: {self.comparisons} | "
                        f"Swaps: {self.swaps}"
                    )
                )

            self.draw_array_selection(
                current_index=current_index,
                comparing_index=comparing_index,
                min_index=min_index,
                sorted_boundary=sorted_boundary
            )

            self.root.after(150, self.animate_selection_sorting)

        except StopIteration:
            self.draw_array()
            self.status_label.config(
                text=(
                    f"Selection Sort Complete! "
                    f"Comparisons: {self.comparisons} | "
                 f"Swaps: {self.swaps}"
                )
            )

    # Starts the Insertion Sort animation.
    def start_insertion_sort(self):
        self.comparisons = 0
        self.swaps = 0

        self.sorting_generator = insertion_sort(self.array)
        self.animate_insertion_sorting()

    # Animates Insertion Sort one generator step at a time.
    def animate_insertion_sorting(self):
        try:
            array_state, current_index, comparing_index, key, inserted = next(
                self.sorting_generator
            )

            if current_index is not None and comparing_index is not None:
                self.comparisons += 1

                if inserted:
                    self.swaps += 1
                    action_text = "Inserted key into correct position"
                else:
                    action_text = "Shifting elements to the right"

                self.status_label.config(
                    text=(
                        f"Current index: {current_index} | "
                        f"Comparing index: {comparing_index} | "
                        f"Key: {key} | "
                        f"{action_text} | "
                        f"Comparisons: {self.comparisons} | "
                        f"Operations: {self.swaps}"
                    )
                )

            self.draw_array_insertion(
                current_index=current_index,
                comparing_index=comparing_index
            )

            self.root.after(150, self.animate_insertion_sorting)

        except StopIteration:
            self.draw_array()
            self.status_label.config(
                text=(
                    f"Insertion Sort Complete! "
                    f"Comparisons: {self.comparisons} | "
                    f"Operations: {self.swaps}"
                )
            )

    # Draws the array for Bubble Sort.
    def draw_array(self, highlight_indices=None, sorted_start_index=None):
        self.canvas.delete("all")

        if highlight_indices is None:
            highlight_indices = []

        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            if i in highlight_indices:
                color = "red"
            elif sorted_start_index is not None and i >= sorted_start_index:
                color = "lightgreen"
            else:
                color = "skyblue"

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill=color,
                outline="black",
                width=1
            )

    # Draws the array for Selection Sort.
    def draw_array_selection(
        self,
        current_index=None,
        comparing_index=None,
        min_index=None,
        sorted_boundary=None
    ):
        self.canvas.delete("all")

        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            if i == current_index:
                color = "purple"
            elif i == comparing_index:
                color = "red"
            elif i == min_index:
                color = "orange"
            elif sorted_boundary is not None and i < sorted_boundary:
                color = "lightgreen"
            else:
                color = "skyblue"

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill=color,
                outline="black",
                width=1
            )

    # Draws the array for Insertion Sort.
    def draw_array_insertion(self, current_index=None, comparing_index=None):
        self.canvas.delete("all")

        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            if i == current_index:
                color = "purple"
            elif i == comparing_index:
                color = "red"
            elif current_index is not None and i < current_index:
                color = "lightgreen"
            else:
                color = "skyblue"

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill=color,
                outline="black",
                width=1
            )

def main():
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()