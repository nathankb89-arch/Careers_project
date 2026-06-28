import customtkinter as ctk


class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = ctk.CTkCanvas(self, fg_color=kwargs.get('fg_color', '#1a1a1a'), highlightthickness=0, bd=0)
        self.scrollbar = ctk.CTkScrollbar(self, orientation='vertical', command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color=kwargs.get('fg_color', '#1a1a1a'))

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self._on_canvas_configure)

        self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scrollable_frame.bind('<Configure>', self._on_frame_configure)

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.window, width=event.width)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
