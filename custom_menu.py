from program_settings import *


class MenuManager:
    def __init__(self, master):
        self.master = master
        self.menu_font = ("Roboto", 15, "bold")

    def create_main_menu(self):
        main_menu = tk.Menu(self.master)
        self.master.config(menu=main_menu)
        self.create_file_menu(main_menu)
        self.create_system_menu(main_menu)

    def create_file_menu(self, main_menu):
        file_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.open_file, font=self.menu_font)
        file_menu.add_command(label="Close Window", command=self.on_closing, font=self.menu_font)

    def create_system_menu(self, main_menu):
        system_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="System", menu=system_menu)
        system_menu.add_command(label="Clear Directory", command=self.clean_files, font=self.menu_font)

    # Placeholder methods for the commands
    @staticmethod
    def open_file():
        file_path = tk.filedialog.askopenfilename(initialdir="/",
                                                  title="Select A File",
                                                  filetypes=(("excel files", "*.xlsx"), ("All Files", "*.*")))
        subprocess.Popen([file_path], shell=True)

    @staticmethod
    def clean_files():
        # Define the path to the directory to be cleaned
        path = os.path.join(os.getcwd(), 'temp')
        path_1 = os.path.join(os.getcwd(), 'payroll records')

        # remove the directory
        shutil.rmtree(path)
        shutil.rmtree(path_1)

        # remove insulpay.db
        os.remove('insulpay.db')

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()
