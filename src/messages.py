import tkinter as tk
from tkinter import simpledialog


def ask(message):
  # Create the main window
  window = tk.Tk()
  window.title("")
  window.geometry("400x300")
  window.withdraw()

  # Read input string from user
  input_value = simpledialog.askstring("Menú", message)

  return input_value or ""