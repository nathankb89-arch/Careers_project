import customtkinter as ctk
from functools import partial
from tkinter import messagebox


class JobsPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.build_page()

    def build_page(self):
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(header_frame, text="💼 Job Matches", font=("Segoe UI", 22, "bold"), text_color="#00D4FF").pack(anchor="w")
        ctk.CTkLabel(header_frame, text="Perfect opportunities matched to your skills", font=("Segoe UI", 11), text_color="#888888").pack(anchor="w", pady=(5, 0))

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Jobs container
        jobs_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        jobs_container.pack(fill="both", expand=True, padx=20, pady=10)
        jobs_container.grid_columnconfigure(0, weight=1)

        jobs = self.app.get_jobs()

        if not jobs:
            empty_card = ctk.CTkFrame(jobs_container, fg_color="#2d2d2d", corner_radius=10)
            empty_card.pack(fill="both", expand=True)
            ctk.CTkLabel(empty_card, text="📭 No jobs available right now", font=("Segoe UI", 13), text_color="#888888").pack(pady=30)
        else:
            for idx, job in enumerate(jobs):
                card = ctk.CTkFrame(jobs_container, fg_color="#2d2d2d", corner_radius=12, border_width=1, border_color="#333333")
                card.pack(fill="x", expand=False, pady=8)
                card.grid_columnconfigure(0, weight=1)
                
                # Job header with title and match score
                header = ctk.CTkFrame(card, fg_color="#2d2d2d")
                header.pack(fill="x", padx=15, pady=(12, 8))
                header.grid_columnconfigure(0, weight=1)
                
                # Title and company
                title_text = f"{job['title']} at {job['company']}"
                ctk.CTkLabel(header, text=title_text, font=("Segoe UI", 12, "bold"), text_color="#00D4FF").grid(row=0, column=0, sticky="w")
                
                # Match score badge
                match_color = "#10B981" if job['score'] >= 80 else "#F59E0B" if job['score'] >= 60 else "#EF4444"
                ctk.CTkLabel(header, text=f"{job['score']}% Match", font=("Segoe UI", 10, "bold"), text_color=match_color).grid(row=0, column=1, sticky="e", padx=(10, 0))
                
                # Job details
                details_frame = ctk.CTkFrame(card, fg_color="#2d2d2d")
                details_frame.pack(fill="x", padx=15, pady=(0, 10))
                
                ctk.CTkLabel(details_frame, text=f"📍 {job['career_field']} • Level: {job['level']}", font=("Segoe UI", 10), text_color="#AAAAAA").pack(anchor="w", pady=(0, 5))

                # Skills status
                if job['missing_skills']:
                    missing_text = f"🔧 Missing: {', '.join(job['missing_skills'])}"
                    ctk.CTkLabel(details_frame, text=missing_text, font=("Segoe UI", 9), text_color="#F59E0B").pack(anchor="w", pady=(0, 8))
                else:
                    ctk.CTkLabel(details_frame, text="✓ You have all required skills!", font=("Segoe UI", 9), text_color="#10B981").pack(anchor="w", pady=(0, 8))

                # Buttons
                button_frame = ctk.CTkFrame(card, fg_color="#2d2d2d")
                button_frame.pack(fill="x", padx=15, pady=(0, 12))
                button_frame.grid_columnconfigure(1, weight=1)
                
                ctk.CTkButton(button_frame, text="Apply", width=80, height=32, font=("Segoe UI", 10, "bold"), fg_color="#00D4FF", hover_color="#00B8D4", text_color="#000000", command=partial(self.handle_apply, job['job_id'])).grid(row=0, column=0, padx=(0, 8))
                
                back_command = getattr(self.app, "show_dashboard", None)
                if not callable(back_command):
                    back_command = lambda: None
                ctk.CTkButton(button_frame, text="← Back", width=80, height=32, font=("Segoe UI", 10, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=back_command).grid(row=0, column=2, padx=(8, 0))

        # Footer with back button
        footer_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        footer_frame.pack(fill="x", padx=20, pady=20)
        
        back_command = getattr(self.app, "show_dashboard", None)
        if not callable(back_command):
            back_command = lambda: None
        ctk.CTkButton(footer_frame, text="← Back to Dashboard", height=40, font=("Segoe UI", 12, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=back_command).pack(anchor="w")

    def handle_apply(self, job_id):
        apply_func = getattr(self.app, "apply_to_job", None)
        if callable(apply_func):
            apply_func(job_id)
            messagebox.showinfo("Applied", "Your application was saved.")
        else:
            messagebox.showwarning("Error", "Unable to apply to this job.")
