import customtkinter
import fetch_book
from urllib.parse import urlparse
import threading

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RFetcher")
        self.geometry("600x380")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # FRAME 1 (LEFT PART)
        self.checkbox_frame = customtkinter.CTkScrollableFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # URL Input
        self.label_chapter = customtkinter.CTkLabel(self.checkbox_frame, text="Chapter URL", fg_color="transparent")
        self.label_chapter.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.entry = customtkinter.CTkEntry(self.checkbox_frame, placeholder_text="https://royalroad.com/...")
        self.entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


        # Number of chapter to scan INPUT
        self.label_chapter_number = customtkinter.CTkLabel(self.checkbox_frame, text="Number of chapter to scan", fg_color="transparent")
        self.label_chapter_number.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.entry_number = customtkinter.CTkEntry(self.checkbox_frame, placeholder_text="20")
        self.entry_number.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")


        # Name of your ebook INPUT
        self.label_chapter_name = customtkinter.CTkLabel(self.checkbox_frame, text="Name of your ebook (no space)", fg_color="transparent")
        self.label_chapter_name.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.entry_name = customtkinter.CTkEntry(self.checkbox_frame, placeholder_text="Mother_Of_Learning")
        self.entry_name.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")


        # # Convert CHECKBOX
        # self.checkbox_convert = customtkinter.CTkCheckBox(self.checkbox_frame, text="Convert to AZW3")
        # self.checkbox_convert.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")

        # # Push to device CHECKBOX
        # self.checkbox_convert = customtkinter.CTkCheckBox(self.checkbox_frame, text="Push to your kindle")
        # self.checkbox_convert.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="w")


        # FRAME 2 (RIGHT PART)

        self.textbox = customtkinter.CTkTextbox(master=self,  corner_radius=0)
        self.textbox.grid(row=0, column=1, sticky="nsew")
        self.textbox.configure(state="disabled") 

        # FETCH Button
        self.button = customtkinter.CTkButton(self, text="GO !", command=self.fetch_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)




    def fetch_callback(self):
        print(f"Fetch button pressed! {self.entry.get()} {self.entry_number.get()} {self.entry_name.get()}")

        chapter_url = self.entry.get()
        number_of_chapters = self.entry_number.get()
        file_name = self.entry_name.get().strip().replace(" ","")


        # CHECK URL 
        invalid_url = False
        if "https://www.royalroad.com" not in chapter_url:
            invalid_url = True
        try:
            result = urlparse(chapter_url)
            if all([result.scheme, result.netloc]) == False:
                invalid_url = True
        except AttributeError:
            invalid_url =  True
        if invalid_url:
            self.append_log("Please enter a valid Chapter URL : https://www.royalroad.com/fiction/....")
            return False

        # CHECK FIELD LENGTH
        if len(chapter_url) == 0 or len(number_of_chapters) == 0 or len(file_name) == 0:
            self.append_log("Please verify input, some fields are empty")
            return False

        # CHECK FIELD FORMAT
        try:
            int(number_of_chapters)
        except:
            self.append_log("Number of chapter should be an integer and not a string")
            return False


        # fetch_book.main(chapter_url,int(number_of_chapters),"{0}.html".format(file_name),logger=self.append_log)
        
        self.button.configure(state="disabled")
        threading.Thread(target=self.fetch_book, args=(chapter_url, int(number_of_chapters), f"{file_name}.html")).start()

    def fetch_book(self, chapter_url, number_of_chapters, file_name):
        fetch_book.main(chapter_url, number_of_chapters, file_name, logger=self.append_log)
        self.button.configure(state="normal")
        self.textbox.see("end")
        self.append_log("Find your ebook inside the RFetcher folder !")

    def append_log(self, *args):
        
        # I use *args instead of a simple variable to be able to cactch several args, in a print-like fashion
        log_input = " ".join(map(str, args))
        
        self.textbox.configure(state="normal") 
        self.textbox.insert("end", log_input + "\n")
        self.textbox.configure(state="disabled") 



app = App()

app.mainloop()