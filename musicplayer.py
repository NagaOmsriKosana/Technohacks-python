import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("500x300")

        self.playlist = []
        self.current_track = 0
        self.paused = False

        pygame.mixer.init()

        self.create_ui()
    
    def create_ui(self):
        # Create listbox to display playlist
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white", selectbackground="gray")
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        # Add buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        self.play_button = tk.Button(control_frame, text="Play", command=self.play_music)
        self.pause_button = tk.Button(control_frame, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(control_frame, text="Next", command=self.next_track)
        self.prev_button = tk.Button(control_frame, text="Previous", command=self.prev_track)
        self.add_button = tk.Button(control_frame, text="Add Songs", command=self.add_songs)
        self.remove_button = tk.Button(control_frame, text="Remove Song", command=self.remove_song)

        self.play_button.grid(row=0, column=0, padx=10)
        self.pause_button.grid(row=0, column=1, padx=10)
        self.stop_button.grid(row=0, column=2, padx=10)
        self.prev_button.grid(row=0, column=3, padx=10)
        self.next_button.grid(row=0, column=4, padx=10)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for file in files:
            self.playlist.append(file)
            self.playlist_box.insert(tk.END, os.path.basename(file))
    
    def remove_song(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            index = selected_song[0]
            self.playlist.pop(index)
            self.playlist_box.delete(index)
    
    def play_music(self):
        if not pygame.mixer.music.get_busy():
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                if not self.playlist:
                    messagebox.showerror("Error", "Playlist is empty. Add songs to the playlist.")
                else:
                    track = self.playlist[self.current_track]
                    pygame.mixer.music.load(track)
                    pygame.mixer.music.play()
                    self.root.title("Playing: " + os.path.basename(track))
        else:
            messagebox.showerror("Error", "Music is already playing.")
    
    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.root.title("Paused: " + os.path.basename(self.playlist[self.current_track]))
        else:
            messagebox.showerror("Error", "No music to pause.")
    
    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.root.title("Python Music Player")
        else:
            messagebox.showerror("Error", "No music to stop.")
    
    def next_track(self):
        if self.current_track < len(self.playlist) - 1:
            self.current_track += 1
            self.play_music()
        else:
            messagebox.showinfo("End of Playlist", "No more tracks in the playlist.")

    def prev_track(self):
        if self.current_track > 0:
            self.current_track -= 1
            self.play_music()
        else:
            messagebox.showinfo("Start of Playlist", "This is the first track in the playlist.")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
