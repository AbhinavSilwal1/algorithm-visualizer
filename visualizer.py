class Visualizer:
    def __init__(self, canvas, array):
        self.canvas = canvas
        self.array = array

    # Draws the default array display.
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
                outline="black",
                width=1
            )

    # Draws the array for Bubble Sort.
    def draw_array_bubble(self, highlight_indices=None, sorted_start_index=None):
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
    def draw_array_selection(self, current_index=None, comparing_index=None, min_index=None, sorted_boundary=None):
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

    # Draws the array for Merge Sort.
    def draw_array_merge(self, current_index=None, left_boundary=None, right_boundary=None):
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
                color = "red"
            elif left_boundary is not None and right_boundary is not None and left_boundary <= i <= right_boundary:
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

    # Draws the array for Quick Sort.
    def draw_array_quick(self, current_index=None, pivot_index=None, partition_index=None):
        self.canvas.delete("all")

        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            if i == pivot_index:
                color = "orange"
            elif i == current_index:
                color = "red"
            elif partition_index is not None and i <= partition_index:
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