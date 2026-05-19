import tkinter as tk
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from visualizer import Visualizer

ARRAY_SIZE = 50
ARRAY_MIN = 10
ARRAY_MAX = 500

class AlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        self.root.geometry("1080x600")
        self.root.resizable(False, False)

        # Title
        title_label = tk.Label(
            root,
            text="Algorithm Visualizer",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

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

        # Algorithm Dropdown
        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set("<Select Algorithm>")

        algorithm_dropdown = tk.OptionMenu(
            controls_frame,
            self.selected_algorithm,
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort"
        )

        algorithm_dropdown.config(
            width=18,
            bg="white",
            fg="black",
            activebackground="white",
            activeforeground="black",
            highlightthickness=0
        )

        algorithm_dropdown["menu"].config(
            bg="white",
            fg="black"
        )
        algorithm_dropdown.pack(side="left", padx=10)
        self.selected_algorithm.trace_add("write", self.update_legend)

        # Start Sorting Button
        start_button = tk.Button(
            controls_frame,
            text="Start Sorting",
            command=self.start_selected_sort
        )
        start_button.pack(side="left", padx=10)

        # Display Frame
        display_frame = tk.Frame(root)
        display_frame.pack(pady=20)

        # Canvas
        self.canvas = tk.Canvas(
            display_frame,
            width=800,
            height=400,
            bg="white"
        )
        self.canvas.pack(side="left", padx=(0, 30))

        # Dynamic Legend
        self.legend_content = tk.Label(
            display_frame,
            text="",
            font=("Arial", 11),
            justify="left",
            anchor="n"
        )
        self.legend_content.pack(side="left", anchor="n", pady=150)
        
        # Stats
        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 11)
        )

        self.status_label.place(
            relx=0.42,
            rely=0.95,
            anchor="center"
        )       

        self.array = []
        self.visualizer = Visualizer(self.canvas, self.array)
        self.comparisons = 0
        self.swaps = 0

        self.generate_array()

    # Generates a new random array and resets the display.
    def generate_array(self):
        self.array = [
            random.randint(ARRAY_MIN, ARRAY_MAX)
            for _ in range(ARRAY_SIZE)
        ]
        self.visualizer.array = self.array
        self.status_label.config(text="")
        self.visualizer.draw_array()

    # Updates the visible legend based on the selected algorithm.
    def update_legend(self, *args):
        selected = self.selected_algorithm.get()

        legends = {
            "Bubble Sort": "🔵 Unsorted\n\n🔴 Comparing\n\n🟢 Sorted",
            "Selection Sort": "🔵 Unsorted\n\n🔴 Comparing\n\n🟢 Sorted\n\n🟣 Current Position\n\n🟠 Current Minimum",
            "Insertion Sort": "🔵 Unsorted\n\n🔴 Comparing\n\n🟢 Sorted\n\n🟣 Current Key",
            "Merge Sort": "🔵 Unsorted\n\n🔴 Current Merge Index\n\n🟢 Current Merging Range",
            "Quick Sort": "🔵 Unsorted\n\n🔴 Current Index\n\n🟢 Partitioned Region\n\n🟠 Pivot"
        }
        self.legend_content.config(text=legends.get(selected, ""))

    # Starts the selected sorting algorithm.
    def start_selected_sort(self):
        selected = self.selected_algorithm.get()

        if selected == "Bubble Sort":
            self.start_bubble_sort()

        elif selected == "Selection Sort":
            self.start_selection_sort()

        elif selected == "Insertion Sort":
            self.start_insertion_sort()

        elif selected == "Merge Sort":
            self.start_merge_sort()

        elif selected == "Quick Sort":
            self.start_quick_sort()

    # Starts the Bubble Sort animation.
    def start_bubble_sort(self):
        self.comparisons = 0
        self.swaps = 0

        self.sorting_generator = bubble_sort(self.array)
        self.animate_bubble_sorting()

    # Animates Bubble Sort one generator step at a time.
    def animate_bubble_sorting(self):
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

            self.visualizer.draw_array_bubble(
                highlight_indices=[index1, index2],
                sorted_start_index=sorted_start_index
            )

            self.root.after(150, self.animate_bubble_sorting)

        except StopIteration:
            self.visualizer.draw_array()
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

            self.visualizer.draw_array_selection(
                current_index=current_index,
                comparing_index=comparing_index,
                min_index=min_index,
                sorted_boundary=sorted_boundary
            )

            self.root.after(150, self.animate_selection_sorting)

        except StopIteration:
            self.visualizer.draw_array()
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

            self.visualizer.draw_array_insertion(
                current_index=current_index,
                comparing_index=comparing_index
            )

            self.root.after(150, self.animate_insertion_sorting)

        except StopIteration:
            self.visualizer.draw_array()
            self.status_label.config(
                text=(
                    f"Insertion Sort Complete! "
                    f"Comparisons: {self.comparisons} | "
                    f"Operations: {self.swaps}"
                )
            )

    # Starts the Merge Sort animation.
    def start_merge_sort(self):
        self.comparisons = 0
        self.swaps = 0

        self.sorting_generator = merge_sort(self.array)
        self.animate_merge_sorting()

    # Animates Merge Sort one generator step at a time.
    def animate_merge_sorting(self):
        try:
            array_state, current_index, left_boundary, right_boundary, merged = next(
                self.sorting_generator
            )

            if current_index is not None:
                self.comparisons += 1

                self.status_label.config(
                    text=(
                        f"Merging range {left_boundary} to {right_boundary} | "
                        f"Current index: {current_index} | "
                        f"Operations: {self.comparisons}"
                    )
                )

            self.visualizer.draw_array_merge(
                current_index=current_index,
                left_boundary=left_boundary,
                right_boundary=right_boundary
            )

            self.root.after(150, self.animate_merge_sorting)

        except StopIteration:
            self.visualizer.draw_array()
            self.status_label.config(
                text=f"Merge Sort Complete! Operations: {self.comparisons}"
            )

    # Starts the Quick Sort animation.
    def start_quick_sort(self):
        self.comparisons = 0
        self.swaps = 0

        self.sorting_generator = quick_sort(self.array)
        self.animate_quick_sorting()

    # Animates Quick Sort one generator step at a time.
    def animate_quick_sorting(self):
        try:
            array_state, current_index, pivot_index, partition_index, swapped = next(
                self.sorting_generator
            )

            if current_index is not None:
                self.comparisons += 1

                if swapped:
                    self.swaps += 1
                    action_text = "Placed pivot in correct position"
                else:
                    action_text = "Partitioning array"

                self.status_label.config(
                    text=(
                        f"Current index: {current_index} | "
                        f"Pivot index: {pivot_index} | "
                        f"Partition index: {partition_index} | "
                        f"{action_text} | "
                        f"Comparisons: {self.comparisons} | "
                        f"Swaps: {self.swaps}"
                    )
                )

            self.visualizer.draw_array_quick(
                current_index=current_index,
                pivot_index=pivot_index,
                partition_index=partition_index
            )

            self.root.after(150, self.animate_quick_sorting)

        except StopIteration:
            self.visualizer.draw_array()
            self.status_label.config(
                text=(
                    f"Quick Sort Complete! "
                    f"Comparisons: {self.comparisons} | "
                    f"Swaps: {self.swaps}"
                )
            )

def main():
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()