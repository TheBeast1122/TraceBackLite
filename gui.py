import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import os

BG = "#1e1e1e"
BTN = "#0078D7"


def run_analysis():

    def worker():

        try:
            progress.pack(pady=10)
            progress.start()

            status_label.config(text="Running analysis...")

            output.delete(1.0, tk.END)

            process = subprocess.Popen(
                ["py", "core_app.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            for line in process.stdout:
                output.insert(tk.END, line)
                output.see(tk.END)

            process.wait()

            progress.stop()
            progress.pack_forget()

            status_label.config(text="Analysis Complete")

            messagebox.showinfo(
                "TraceBack Lite",
                "Analysis completed successfully."
            )

        except Exception as e:

            progress.stop()
            progress.pack_forget()

            status_label.config(text="Error")

            messagebox.showerror(
                "Error",
                str(e)
            )

    threading.Thread(
        target=worker,
        daemon=True
    ).start()


def open_report():

    report_path = os.path.join(
        "output",
        "traceback_report.txt"
    )

    if os.path.exists(report_path):
        os.startfile(report_path)
    else:
        messagebox.showwarning(
            "Report Missing",
            "No report found. Run analysis first."
        )


root = tk.Tk()

root.title("TraceBack Lite v1")
root.geometry("1200x800")
root.configure(bg=BG)

title = tk.Label(
    root,
    text="TRACEBACK LITE",
    font=("Segoe UI", 28, "bold"),
    bg=BG,
    fg="white"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Unified Digital Forensics Timeline Analyzer",
    font=("Segoe UI", 12),
    bg=BG,
    fg="#cccccc"
)

subtitle.pack()

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(pady=15)

run_btn = tk.Button(
    button_frame,
    text="▶ Run Analysis",
    width=20,
    height=2,
    bg=BTN,
    fg="white",
    command=run_analysis
)

run_btn.pack(
    side=tk.LEFT,
    padx=10
)

report_btn = tk.Button(
    button_frame,
    text="📄 Open Report",
    width=20,
    height=2,
    bg="#444444",
    fg="white",
    command=open_report
)

report_btn.pack(
    side=tk.LEFT,
    padx=10
)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    mode="indeterminate",
    length=600
)

# Hidden initially
progress.pack_forget()

output = tk.Text(
    root,
    bg="black",
    fg="#00ff00",
    insertbackground="white",
    font=("Consolas", 10)
)

output.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

status_label = tk.Label(
    root,
    text="Ready",
    bg="#333333",
    fg="white",
    anchor="w"
)

status_label.pack(
    side="bottom",
    fill="x"
)

root.mainloop()