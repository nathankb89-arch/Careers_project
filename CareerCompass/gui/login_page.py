import customtkinter as ctk
from tkinter import messagebox


class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.build_page()

    def build_page(self):
        # Main container with padding
        main_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        main_container.pack(fill="both", expand=True, padx=40, pady=60)
        main_container.grid_columnconfigure(0, weight=1)

        # Logo/Title section with enhanced styling
        title_frame = ctk.CTkFrame(main_container, fg_color="#1a1a1a")
        title_frame.grid(row=0, column=0, pady=(0, 40), sticky="ew")
        title_frame.grid_columnconfigure(0, weight=1)
        
        # Main title with gradient-like effect using multiple labels
        ctk.CTkLabel(title_frame, text="🎯 CareerCompass", font=("Segoe UI", 40, "bold"), text_color="#00D4FF").pack()
        ctk.CTkLabel(title_frame, text="Your Career Path Starts Here", font=("Segoe UI", 15), text_color="#6B7280").pack(pady=(8, 0))
        ctk.CTkLabel(title_frame, text="Discover opportunities matched to your skills", font=("Segoe UI", 11), text_color="#4B5563").pack(pady=(4, 0))

        # Card container with enhanced design
        card = ctk.CTkFrame(main_container, fg_color="#252525", corner_radius=20)
        card.grid(row=1, column=0, sticky="ew")
        card.grid_columnconfigure(0, weight=1)
        
        # Decorative top border/accent
        accent_bar = ctk.CTkFrame(card, fg_color="#00D4FF", height=4, corner_radius=20)
        accent_bar.pack(fill="x", padx=0, pady=0)
        
        # Card content with better spacing
        content_frame = ctk.CTkFrame(card, fg_color="#252525")
        content_frame.pack(fill="both", expand=True, padx=35, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Welcome section
        ctk.CTkLabel(content_frame, text="Welcome Back!", font=("Segoe UI", 26, "bold"), text_color="#FFFFFF").pack(anchor="w", pady=(0, 5))
        ctk.CTkLabel(content_frame, text="Sign in to your account or create a new one", font=("Segoe UI", 12), text_color="#9CA3AF").pack(anchor="w", pady=(0, 25))

        # Divider line
        divider = ctk.CTkFrame(content_frame, fg_color="#404040", height=1)
        divider.pack(fill="x", pady=(0, 25))

        # Name label with enhanced styling
        name_label_frame = ctk.CTkFrame(content_frame, fg_color="#252525")
        name_label_frame.pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(name_label_frame, text="Full Name", font=("Segoe UI", 12, "bold"), text_color="#E5E7EB").pack(anchor="w")
        
        # Name entry with enhanced styling
        self.name_entry = ctk.CTkEntry(
            content_frame, 
            width=300, 
            placeholder_text="Enter your full name", 
            font=("Segoe UI", 12), 
            height=45,
            fg_color="#1F2937",
            border_color="#00D4FF",
            border_width=2,
            text_color="#FFFFFF",
            placeholder_text_color="#6B7280"
        )
        self.name_entry.pack(fill="x", pady=(0, 25))

        # Login button with enhanced styling and spacing
        login_button = ctk.CTkButton(
            content_frame, 
            text="Continue →", 
            height=48, 
            font=("Segoe UI", 13, "bold"), 
            fg_color="#00D4FF", 
            hover_color="#00B8D4", 
            text_color="#000000",
            corner_radius=10,
            command=self.handle_login
        )
        login_button.pack(fill="x", pady=(0, 15))

        # Footer text
        ctk.CTkLabel(content_frame, text="Secure • No Account Required", font=("Segoe UI", 10), text_color="#6B7280").pack(anchor="center", pady=(10, 0))

    def handle_login(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Validation Error", "Please type your name before continuing.")
            return

        user_id = self.app.find_or_create_user(name)
        self.app.login(user_id)
