import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# File JSON
JSON_FILE = "questions.json"

# Load data
def load_questions():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Simpan data ke JSON
def save_questions(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Tambah pertanyaan baru
def add_question():
    question = simpledialog.askstring("Tambah Pertanyaan", "Masukkan pertanyaan:")
    if question:
        questions.append({"question": question, "answers": []})
        update_listbox()

# Hapus pertanyaan
def delete_question():
    selected = listbox.curselection()
    if selected:
        del questions[selected[0]]
        update_listbox()

# Tambah jawaban ke pertanyaan
def add_answer():
    selected = listbox.curselection()
    if selected:
        answer = simpledialog.askstring("Tambah Jawaban", "Masukkan jawaban:")
        points = simpledialog.askinteger("Nilai", "Masukkan nilai jawaban:")
        if answer and points is not None:
            questions[selected[0]]["answers"].append({"text": answer, "points": points})
            update_listbox()

# Update tampilan daftar pertanyaan
def update_listbox():
    listbox.delete(0, tk.END)
    for q in questions:
        listbox.insert(tk.END, q["question"])
    save_questions(questions)

# GUI Tkinter
root = tk.Tk()
root.title("Game Editor - Family Fortunes")

questions = load_questions()

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack()

tk.Button(root, text="Tambah Pertanyaan", command=add_question).pack()
tk.Button(root, text="Hapus Pertanyaan", command=delete_question).pack()
tk.Button(root, text="Tambah Jawaban", command=add_answer).pack()

update_listbox()
root.mainloop()
