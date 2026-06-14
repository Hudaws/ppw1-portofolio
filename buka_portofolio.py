"""Launcher kecil untuk membuka repository atau demo live PPW1."""

from __future__ import annotations

import sys
import webbrowser


REPO_URL = "https://github.com/Hudaws/ppw1-portofolio"
DEMO_URL = "https://hudaws.github.io/ppw1-portofolio/"


def open_url(url: str) -> None:
    webbrowser.open_new_tab(url)


def run_gui() -> None:
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("PPW1 Portofolio")
    root.geometry("430x260")
    root.resizable(False, False)
    root.configure(bg="#f6f7f1")

    title = tk.Label(
        root,
        text="PPW1 Portofolio",
        bg="#f6f7f1",
        fg="#1e2a32",
        font=("Segoe UI", 18, "bold"),
    )
    title.pack(pady=(22, 4))

    subtitle = tk.Label(
        root,
        text="Misbahul Huda - 25/568209/SV/27391",
        bg="#f6f7f1",
        fg="#66737d",
        font=("Segoe UI", 10),
    )
    subtitle.pack()

    hint = tk.Label(
        root,
        text="Pilih halaman yang ingin dibuka:",
        bg="#f6f7f1",
        fg="#1e2a32",
        font=("Segoe UI", 10),
    )
    hint.pack(pady=(18, 10))

    button_frame = tk.Frame(root, bg="#f6f7f1")
    button_frame.pack()

    def launch(label: str, url: str) -> None:
        open_url(url)
        messagebox.showinfo("Berhasil", f"{label} dibuka di browser.")

    button_style = {
        "width": 24,
        "height": 2,
        "bg": "#0f766e",
        "fg": "white",
        "activebackground": "#0b5f59",
        "activeforeground": "white",
        "font": ("Segoe UI", 10, "bold"),
        "relief": "flat",
        "cursor": "hand2",
    }

    tk.Button(
        button_frame,
        text="Buka Repository GitHub",
        command=lambda: launch("Repository GitHub", REPO_URL),
        **button_style,
    ).pack(pady=5)

    tk.Button(
        button_frame,
        text="Buka Demo Live",
        command=lambda: launch("Demo Live", DEMO_URL),
        **button_style,
    ).pack(pady=5)

    close_button = tk.Button(
        root,
        text="Tutup",
        command=root.destroy,
        width=12,
        bg="#ffffff",
        fg="#1e2a32",
        activebackground="#eef0ea",
        activeforeground="#1e2a32",
        font=("Segoe UI", 9),
        relief="solid",
        bd=1,
        cursor="hand2",
    )
    close_button.pack(pady=(12, 0))

    root.mainloop()


def run_console() -> None:
    while True:
        print("\nPPW1 Portofolio")
        print("1. Buka Repository GitHub")
        print("2. Buka Demo Live")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ").strip()

        if choice == "1":
            open_url(REPO_URL)
            print("Repository GitHub dibuka di browser.")
        elif choice == "2":
            open_url(DEMO_URL)
            print("Demo Live dibuka di browser.")
        elif choice == "3":
            print("Selesai.")
            return
        else:
            print("Pilihan tidak valid.")


def main() -> None:
    try:
        run_gui()
    except Exception as exc:
        if getattr(sys, "frozen", False):
            raise
        print(f"Mode GUI tidak tersedia: {exc}")
        run_console()


if __name__ == "__main__":
    main()
