import tkinter as tk

class ApplicationPane:
    def __init__(self) -> None:
        self.root, self._pane = self.setup()
        self.left, self.right = self.setup_panels()

    def left(self) -> tk.Frame:
        return self.left
    
    def right(self) -> tk.Frame:
        return self.right
     
    def setup(self) -> tuple[tk.Tk, tk.PanedWindow]:
        # for the outside window
        root = tk.Tk()
        root.title("Market Analysis Tool")
        root.attributes("-fullscreen", True)
        root.resizable(False, False)
        pane = self.setup_panes()
        return root, pane

    def setup_panes(self) -> tk.PanedWindow:
        config = {
            "bg": "white",
            "borderwidth": 2,
        }
        pane = tk.PanedWindow(orient=tk.HORIZONTAL)
        pane.pack(fill=tk.BOTH, expand=True)
        pane.configure(**config)

        return pane
    
    def setup_panels(self) -> tk.Frame:
        screen_width = self._pane.winfo_screenwidth()
        shared_config = {
            "bg": "black",
        }

        # Left panel
        left_width = int(screen_width * 0.67)
        left_panel = tk.Frame(self._pane, width=left_width, **shared_config)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=1, pady=1)

        # Right panel
        right_width = screen_width - left_width
        right_panel = tk.Frame(self._pane, width=right_width, **shared_config)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=1, pady=1)
        return left_panel, right_panel

if __name__ == "__main__":
    app = ApplicationPane()
    app.root.mainloop()