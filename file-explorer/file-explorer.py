import tkinter as tk
from tkinter import filedialog, ttk

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced File Explorer")
        self.root.geometry("500x300")
        self.root.resizable(True, True)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 12), padding=10)
        
        # Variables
        self.selected_file = tk.StringVar()
        self.selected_directory = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # File selection section
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding=10)
        file_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(file_frame, text="Browse File", command=self.browse_file).pack(side=tk.LEFT)
        ttk.Label(file_frame, textvariable=self.selected_file, wraplength=400).pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Directory selection section
        dir_frame = ttk.LabelFrame(main_frame, text="Directory Selection", padding=10)
        dir_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(dir_frame, text="Browse Directory", command=self.browse_directory).pack(side=tk.LEFT)
        ttk.Label(dir_frame, textvariable=self.selected_directory, wraplength=400).pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Status bar
        self.status_bar = ttk.Label(main_frame, text="Ready", relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file.set(file_path)
            self.status_bar.config(text=f"Selected file: {file_path}")
        
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory.set(directory_path)
            self.status_bar.config(text=f"Selected directory: {directory_path}")

def main():
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
