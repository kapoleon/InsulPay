from scripts.insulpay_imports import *


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scratch")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create the menu bar
        self.menu_manager = MenuManager(self)
        self.menu_manager.create_main_menu()

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = MainApplication()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
