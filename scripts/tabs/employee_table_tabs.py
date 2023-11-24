import tkinter as tk
from tkinter import ttk


class TabOne:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = ttk.Label(self.frame, text="This is Tab One")
        label.pack(padx=10, pady=10)


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = ttk.Label(self.frame, text="This is Tab Two")
        label.pack(padx=10, pady=10)
