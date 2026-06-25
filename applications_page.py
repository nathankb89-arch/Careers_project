import customtkinter as ctk


class ApplicationsPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.build_page()

    def build_page(self):
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(header_frame, text="📋 Application History", font=("Segoe UI", 22, "bold"), text_color="#00D4FF").pack(anchor="w")
        ctk.CTkLabel(header_frame, text="Track your job applications and their status", font=("Segoe UI", 11), text_color="#888888").pack(anchor="w", pady=(5, 0))

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Applications container
        apps_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        apps_container.pack(fill="both", expand=True, padx=20, pady=10)
        apps_container.grid_columnconfigure(0, weight=1)

        applications = self.app.get_applications()

        if not applications:
            empty_card = ctk.CTkFrame(apps_container, fg_color="#2d2d2d", corner_radius=10)
            empty_card.pack(fill="both", expand=True)
            ctk.CTkLabel(empty_card, text="📍 No applications yet", font=("Segoe UI", 13), text_color="#888888").pack(pady=15)
            ctk.CTkLabel(empty_card, text="Start applying to jobs to see them here", font=("Segoe UI", 11), text_color="#666666").pack(pady=(0, 15))
        else:
            for idx, application in enumerate(applications):
                card = ctk.CTkFrame(apps_container, fg_color="#2d2d2d", corner_radius=10, border_width=1, border_color="#333333")
                card.pack(fill="x", expand=False, pady=8)
                card.grid_columnconfigure(0, weight=1)
                
                # Job info
                info_frame = ctk.CTkFrame(card, fg_color="#2d2d2d")
                info_frame.pack(fill="x", padx=15, pady=(12, 8))
                info_frame.grid_columnconfigure(0, weight=1)
                
                ctk.CTkLabel(info_frame, text=f"{application['title']} at {application['company']}", font=("Segoe UI", 12, "bold"), text_color="#00D4FF").grid(row=0, column=0, sticky="w")
                
                # Status badge
                status = application['status']
                if status.lower() == 'applied':
                    status_color = "#3B82F6"
                    status_icon = "📋"
                elif status.lower() in ['reviewing', 'under review']:
                    status_color = "#F59E0B"
                    status_icon = "🔍"
                elif status.lower() in ['accepted', 'approved']:
                    status_color = "#10B981"
                    status_icon = "✅"
                elif status.lower() in ['rejected', 'denied']:
                    status_color = "#EF4444"
                    status_icon = "❌"
                else:
                    status_color = "#888888"
                    status_icon = "ⓘ"
                
                ctk.CTkLabel(info_frame, text=f"{status_icon} {status}", font=("Segoe UI", 10, "bold"), text_color=status_color).grid(row=0, column=1, sticky="e")

        # Footer with back button
        footer_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        footer_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkButton(footer_frame, text="← Back to Dashboard", height=40, font=("Segoe UI", 12, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=self.app.show_dashboard).pack(anchor="w")
