import customtkinter as ctk
from tkinter import messagebox


class ProfilePage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#0b1120")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.app = app
        self.user = self.app.get_current_user() or {}
        self.build_page()

    def build_page(self):
        # Create a scrollable area for the profile editor
        scroll_area = ctk.CTkScrollableFrame(self, fg_color="#0b1120", border_width=0)
        scroll_area.grid(row=0, column=0, sticky="nsew", padx=16, pady=16)
        scroll_area.grid_columnconfigure(0, weight=1)

        header_card = ctk.CTkFrame(scroll_area, fg_color="#111827", corner_radius=18, border_width=1, border_color="#1f2937")
        header_card.grid(row=0, column=0, sticky="ew", padx=12, pady=(0, 16))
        header_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header_card, text="👤 Profile Details", font=("Segoe UI", 24, "bold"), text_color="#38bdf8").grid(row=0, column=0, sticky="w", padx=20, pady=(20, 4))
        ctk.CTkLabel(header_card, text="Update your career profile with skills, talents, hobbies, education, and interests.", font=("Segoe UI", 11), text_color="#cbd5e1", wraplength=760, justify="left").grid(row=1, column=0, sticky="w", padx=20, pady=(0, 18))
        ctk.CTkButton(header_card, text="← Back", width=150, height=40, fg_color="#2563eb", hover_color="#1d4ed8", text_color="#ffffff", font=("Segoe UI", 11, "bold"), command=self.app.show_dashboard).grid(row=0, column=1, rowspan=2, sticky="e", padx=20, pady=20)

        card = ctk.CTkFrame(scroll_area, fg_color="#111827", corner_radius=18, border_width=1, border_color="#1f2937")
        card.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 16))
        card.grid_columnconfigure((0, 1), weight=1)

        left = ctk.CTkFrame(card, fg_color="#111827")
        left.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)
        right = ctk.CTkFrame(card, fg_color="#111827")
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)

        self._add_text_field(left, "Technical Skills", "List your main skills separated by commas.", "e.g., Python, Excel, SQL", "skills", self.user.get("skills", ""))
        self._add_text_field(left, "Talents", "What are you naturally good at?", "e.g., Creativity, Leadership", "talents", self.user.get("talents", ""))
        self._add_text_field(left, "Hobbies", "What do you enjoy doing in your free time?", "e.g., Reading, Music, Sports", "hobbies", self.user.get("hobbies", ""))

        profile_card = ctk.CTkFrame(right, fg_color="#0f172a", corner_radius=18, border_width=1, border_color="#1f2937")
        profile_card.pack(fill="x", pady=(0, 18))

        name_text = self.user.get("name", "Your Name")
        initials = "".join([part[0] for part in name_text.split() if part])[:2].upper()
        avatar = ctk.CTkFrame(profile_card, fg_color="#38bdf8", width=80, height=80, corner_radius=40)
        avatar.pack(anchor="center", pady=(18, 8))
        avatar_label = ctk.CTkLabel(avatar, text=initials, font=("Segoe UI", 22, "bold"), text_color="#ffffff", fg_color="#38bdf8")
        avatar_label.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(profile_card, text=name_text, font=("Segoe UI", 14, "bold"), text_color="#e2e8f0").pack(anchor="center", pady=(0, 4))
        self.education_preview_label = ctk.CTkLabel(profile_card, text=self.user.get("education", ""), font=("Segoe UI", 10), text_color="#a5b4fc")
        self.education_preview_label.pack(anchor="center", pady=(0, 8))
        ctk.CTkLabel(profile_card, text="Edit fields and save to keep your profile current.", font=("Segoe UI", 9), text_color="#94a3b8").pack(anchor="center", pady=(0, 18))

        info_card = ctk.CTkFrame(profile_card, fg_color="#111827", corner_radius=14)
        info_card.pack(fill="x", padx=14, pady=(0, 18))
        info_card.grid_columnconfigure((0, 1), weight=1)
        ctk.CTkLabel(info_card, text=f"Skills: {self.user.get('skills', 'None')}", font=("Segoe UI", 9), text_color="#cbd5e1").grid(row=0, column=0, sticky="w", padx=12, pady=(12, 4))
        ctk.CTkLabel(info_card, text=f"Talents: {self.user.get('talents', 'None')}", font=("Segoe UI", 9), text_color="#cbd5e1").grid(row=0, column=1, sticky="w", padx=12, pady=(12, 4))
        ctk.CTkLabel(info_card, text=f"Hobbies: {self.user.get('hobbies', 'None')}", font=("Segoe UI", 9), text_color="#cbd5e1").grid(row=1, column=0, sticky="w", padx=12, pady=(0, 12))
        ctk.CTkLabel(info_card, text=f"Education: {self.user.get('education', 'None')}", font=("Segoe UI", 9), text_color="#cbd5e1").grid(row=1, column=1, sticky="w", padx=12, pady=(0, 12))

        ctk.CTkLabel(right, text="Education Level", font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(anchor="w", pady=(6, 0))
        education_options = ["None", "High School", "Associate", "Bachelor's", "Master's", "Doctorate"]
        self.education_menu = ctk.CTkOptionMenu(right, values=education_options)
        self.education_menu.set(self.user.get("education", "High School"))
        self.education_menu.pack(fill="x", pady=(6, 14))

        ctk.CTkLabel(right, text="Career Interests", font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(anchor="w")
        ctk.CTkLabel(right, text="Industries or topics you enjoy (comma separated)", font=("Segoe UI", 9), text_color="#94a3b8").pack(anchor="w", pady=(0, 8))
        self.interests_entry = ctk.CTkEntry(right, width=1, height=40, font=("Segoe UI", 11), fg_color="#0b1120", border_color="#2563eb", border_width=1, placeholder_text="e.g., Technology, Design, Marketing")
        self.interests_entry.insert(0, self.user.get("interests", ""))
        self.interests_entry.pack(fill="x", pady=(0, 6))

        self.status_label = ctk.CTkLabel(scroll_area, text="", font=("Segoe UI", 11, "bold"), text_color="#34d399")
        self.status_label.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 10))

        button_frame = ctk.CTkFrame(scroll_area, fg_color="#0b1120")
        button_frame.grid(row=3, column=0, sticky="ew", padx=12, pady=(0, 20))
        button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(button_frame, text="Reset", width=130, height=44, font=("Segoe UI", 12, "bold"), fg_color="#334155", hover_color="#475569", command=self.reset_form).grid(row=0, column=0, padx=(0, 8), sticky="ew")
        ctk.CTkButton(button_frame, text="💾 Save Profile", width=180, height=48, font=("Segoe UI", 13, "bold"), fg_color="#22c55e", hover_color="#16a34a", text_color="#ffffff", command=self.save_profile).grid(row=0, column=1, padx=(8, 8), sticky="ew")
        ctk.CTkButton(button_frame, text="Cancel", width=120, height=44, font=("Segoe UI", 12, "bold"), fg_color="#1f2937", border_color="#334155", hover_color="#111827", command=self.app.show_dashboard).grid(row=0, column=2, padx=(8, 0), sticky="ew")

    def _add_text_field(self, parent, label, instruction, placeholder, attr_name, value):
        ctk.CTkLabel(parent, text=label, font=("Segoe UI", 12, "bold"), text_color="#38bdf8").pack(anchor="w")
        ctk.CTkLabel(parent, text=instruction, font=("Segoe UI", 9), text_color="#94a3b8").pack(anchor="w", pady=(0, 8))
        entry = ctk.CTkEntry(parent, width=1, height=40, font=("Segoe UI", 11), fg_color="#0b1120", border_color="#2563eb", border_width=1, placeholder_text=placeholder)
        entry.insert(0, str(value or ""))
        entry.pack(fill="x", pady=(0, 16))
        setattr(self, f"{attr_name}_entry", entry)

    def save_profile(self):
        skills = self.skills_entry.get().strip()
        education = self.education_menu.get().strip()
        talents = self.talents_entry.get().strip()
        hobbies = self.hobbies_entry.get().strip()
        interests = self.interests_entry.get().strip()

        try:
            self.app.update_user_profile(skills, interests, education, talents, hobbies)
            self.user = self.app.get_current_user()
            self.education_preview_label.configure(text=education)
            self.status_label.configure(text="Profile saved successfully!", text_color="#34d399")
        except Exception as e:
            self.status_label.configure(text=f"Save failed: {e}", text_color="#f87171")

    def reset_form(self):
        self.skills_entry.delete(0, "end")
        self.skills_entry.insert(0, self.user.get("skills", ""))
        self.talents_entry.delete(0, "end")
        self.talents_entry.insert(0, self.user.get("talents", ""))
        self.hobbies_entry.delete(0, "end")
        self.hobbies_entry.insert(0, self.user.get("hobbies", ""))
        self.interests_entry.delete(0, "end")
        self.interests_entry.insert(0, self.user.get("interests", ""))
        self.education_menu.set(self.user.get("education", "High School"))
        self.status_label.configure(text="Form reset to last saved values.", text_color="#60a5fa")