import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.build_page()

    def build_page(self):
        user = self.app.get_current_user()
        
        # Header section
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(header_frame, text=f"Welcome, {user.get('name', 'Student')}! 👋", font=("Segoe UI", 24, "bold"), text_color="#00D4FF").pack(anchor="w")
        ctk.CTkLabel(header_frame, text="Select a tool to get started", font=("Segoe UI", 12), text_color="#888888").pack(anchor="w", pady=(5, 0))

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Button frame with better styling
        button_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        button_container.pack(fill="both", expand=True, padx=20, pady=20)
        button_container.grid_columnconfigure((0, 1), weight=1)
        button_container.grid_rowconfigure((0, 1), weight=1)

        # Career Quiz button
        quiz_btn = ctk.CTkButton(button_container, text="📊 Career Quiz\nFind your path", height=80, font=("Segoe UI", 13, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", text_color="#FFFFFF", command=self.app.show_career_quiz)
        quiz_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Job Matches button
        jobs_btn = ctk.CTkButton(button_container, text="💼 Job Matches\nFind opportunities", height=80, font=("Segoe UI", 13, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", text_color="#FFFFFF", command=self.app.show_jobs)
        jobs_btn.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Applications button
        apps_btn = ctk.CTkButton(button_container, text="📋 Applications\nTrack your progress", height=80, font=("Segoe UI", 13, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", text_color="#FFFFFF", command=self.app.show_applications)
        apps_btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Update Profile button
        profile_btn = ctk.CTkButton(button_container, text="👤 Update Profile\nManage your info", height=80, font=("Segoe UI", 13, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", text_color="#FFFFFF", command=self.app.show_update_profile)
        profile_btn.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Logout button in footer
        footer_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        footer_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        logout_btn = ctk.CTkButton(footer_frame, text="Logout", width=100, height=35, font=("Segoe UI", 11, "bold"), fg_color="#ff4444", hover_color="#cc3333", text_color="#FFFFFF", command=self.app.logout)
        logout_btn.pack(side="right")
