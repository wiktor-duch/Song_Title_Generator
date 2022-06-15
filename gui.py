"This module allows to run the application with Tkinter."
import tkinter as tk
from tkinter.messagebox import showerror
from exceptions import MusicBrainzAPIException, RandomWordAPIException
from api_handler import get_random_words, get_songs

class GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # Configure window
        self.title('Song Title Generator')
        self.resizable(0, 0)
        pos_x = self.winfo_screenwidth() // 2 - 400
        pos_y = self.winfo_screenheight() // 2 - 400
        size_x = 600
        size_y = 600
        self.geometry(f"{size_x}x{size_y}+{pos_x}+{pos_y}")

        # configure the grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    # Creates all widgets
    def create_widgets(self) -> None:
        # Function that is called when the button is clicked
        def generate_words_and_records() -> None:
            # Validate input
            try:
                num_words = int(spinbox.get())
                if num_words < 5 or num_words > 20:
                    showerror(
                        "Value Error",
                        "Entered number must be between 5 and 20!"
                    )
            except ValueError:
                showerror(
                    "Input Error",
                    "You must enter a number between 5 and 20!"
                )
            
            # Display random words
            rand_word_list.delete(0,tk.END)
            try:
                random_words = get_random_words(num_words)
                for i in range(0, len(random_words)):
                    rand_word_list.insert(tk.END, f"\t{i+1}: {random_words[i]}")
            except RandomWordAPIException:
                showerror(
                    "Random Word API Error",
                    "An error occured when communicating with Random Word API."
                )

            # Display recordings
            recordings_list.delete(0,tk.END)
            try:
                songs = get_songs(random_words)
                i = 1
                for entry in songs:
                    recordings_list.insert(tk.END, f" {i}. {entry}:")
                    if isinstance(songs.get(entry), str):
                        recordings_list.insert(tk.END, f"\t{songs.get(entry)}")
                    else:
                        recordings_list.insert(tk.END, f"\tTITLE: {songs.get(entry).get('title')}")
                        artists = ", ".join(songs.get(entry).get('artists'))
                        recordings_list.insert(tk.END, f"\tARTISTS: {artists}")
                        recordings_list.insert(tk.END, f"\tALBUM: {songs.get(entry).get('album')}")
                    i += 1
            except MusicBrainzAPIException as e:
                showerror("MusicBrainz API Error", e)
        
        # Create user input field
        user_input_label = tk.Label(
            self,
            text="How many different words would you like to generate?",
            font="Helvetica 16"
        )
        user_input_label.grid(column=0, row=0, padx=5, pady=10)

        spinbox = tk.Spinbox(self, from_=5, to=20, width=15)
        spinbox.grid(column=1, row=0, sticky=tk.W, padx=5, pady=10)

        # Create main button
        search_button = tk.Button(
            self,
            text="Generate words and search",
            command=generate_words_and_records,
            font="Helvetica 13",
            padx=10,
            pady=5
        )
        search_button.grid(column=0, row=1, padx=5, pady=5, columnspan=4)

        # Random Word API label
        rand_word_label = tk.Label(self,
            text="Random words from API are:",
            font="Helvetica 18 bold"
        )
        rand_word_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        # Random words results
        rand_word_frame = tk.Frame(self, width=550)
        rand_word_frame.grid(column=0, row=3, columnspan=4, padx=5, pady=5)

        scrollbar = tk.Scrollbar(rand_word_frame)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        rand_word_list = tk.Listbox(
            rand_word_frame,
            yscrollcommand = scrollbar.set,
            width=90
        )
        rand_word_list.pack(side = tk.LEFT, fill = tk.BOTH)
        scrollbar.config(command = rand_word_list.yview)

        # MusicBrainz API label
        musicbrainz_label = tk.Label(self,
            text="Recordings found for each word:",
            font="Helvetica 18 bold"
        )
        musicbrainz_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        # Searching results
        musicbrainz_frame = tk.Frame(self, width=550)
        musicbrainz_frame.grid(column=0, row=5, columnspan=4, padx=5, pady=5)

        scrollbar = tk.Scrollbar(musicbrainz_frame)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        recordings_list = tk.Listbox(
            musicbrainz_frame,
            yscrollcommand = scrollbar.set,
            width=90
        )
        recordings_list.pack(side = tk.LEFT, fill = tk.BOTH)
        scrollbar.config(command = rand_word_list.yview)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()