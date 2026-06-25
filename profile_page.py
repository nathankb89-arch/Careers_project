import customtkinter as ctk
from tkinter import messagebox


class ProfilePage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.user = self.app.get_current_user()
        self.build_page()

    def build_page(self):
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(header_frame, text="👤 Update Profile", font=("Segoe UI", 22, "bold"), text_color="#00D4FF").pack(anchor="w")
        ctk.CTkLabel(header_frame, text="Manage your skills and interests", font=("Segoe UI", 11), text_color="#888888").pack(anchor="w", pady=(5, 0))

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Form container
        form_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        form_container.pack(fill="both", expand=True, padx=20, pady=10)
        form_container.grid_columnconfigure(0, weight=1)

        # Card container
        card = ctk.CTkFrame(form_container, fg_color="#2d2d2d", corner_radius=12, border_width=1, border_color="#333333")
        card.pack(fill="both", expand=True, padx=0, pady=0)
        card.grid_columnconfigure(0, weight=1)

        # Skills section
        ctk.CTkLabel(card, text="Technical Skills", font=("Segoe UI", 12, "bold"), text_color="#00D4FF").grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
        ctk.CTkLabel(card, text="Enter skills separated by commas (e.g., Python, Excel, SQL)", font=("Segoe UI", 9), text_color="#888888").grid(row=1, column=0, sticky="w", padx=20, pady=(0, 10))
        
        self.skills_entry = ctk.CTkEntry(card, width=400, height=45, font=("Segoe UI", 11), fg_color="#3d3d3d", border_color="#00D4FF", border_width=2, placeholder_text="e.g., Python, Excel, Data Analysis")
        self.skills_entry.insert(0, self.user.get("skills", ""))
        self.skills_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

        # Interests section
        ctk.CTkLabel(card, text="Career Interests", font=("Segoe UI", 12, "bold"), text_color="#00D4FF").grid(row=3, column=0, sticky="w", padx=20, pady=(10, 5))
        ctk.CTkLabel(card, text="Enter interests separated by commas (e.g., Technology, Finance)", font=("Segoe UI", 9), text_color="#888888").grid(row=4, column=0, sticky="w", padx=20, pady=(0, 10))
        
        self.interests_entry = ctk.CTkEntry(card, width=400, height=45, font=("Segoe UI", 11), fg_color="#3d3d3d", border_color="#00D4FF", border_width=2, placeholder_text="e.g., Technology, Startups, AI")
        self.interests_entry.insert(0, self.user.get("interests", ""))
        self.interests_entry.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 20))

        # Button frame
        button_frame = ctk.CTkFrame(card, fg_color="#2d2d2d")
        button_frame.grid(row=6, column=0, sticky="ew", padx=20, pady=(0, 20))
        button_frame.grid_columnconfigure(1, weight=1)

        save_button = ctk.CTkButton(button_frame, text="💾 Save Changes", width=140, height=40, font=("Segoe UI", 12, "bold"), fg_color="#00D4FF", hover_color="#00B8D4", text_color="#000000", command=self.save_profile)
        save_button.grid(row=0, column=0, padx=(0, 10))

        back_button = ctk.CTkButton(button_frame, text="Cancel", width=140, height=40, font=("Segoe UI", 12, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=self.app.show_dashboard)
        back_button.grid(row=0, column=2, padx=(10, 0))

    def save_profile(self):
        skills = self.skills_entry.get().strip()
        interests = self.interests_entry.get().strip()
        self.app.update_user_profile(skills, interests)
        messagebox.showinfo("Success", "Your profile has been updated!")
        self.app.show_dashboard()
