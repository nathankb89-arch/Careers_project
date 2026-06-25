import customtkinter as ctk
from .recommendations import RecommendationsFrame


class CareerQuizPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True)
        self.app = app
        self.build_page()

    def build_page(self):
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(header_frame, text="📊 Career Recommendations", font=("Segoe UI", 22, "bold"), text_color="#00D4FF").pack(anchor="w")
        ctk.CTkLabel(header_frame, text="Based on your skills and interests", font=("Segoe UI", 11), text_color="#888888").pack(anchor="w", pady=(5, 0))

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Scrollable content
        recommendations = self.app.get_recommendations()
        RecommendationsFrame(self, recommendations).pack(fill="both", expand=True, padx=20, pady=10)

        # Back button
        button_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        button_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkButton(button_frame, text="← Back to Dashboard", height=40, font=("Segoe UI", 12, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=self.app.show_dashboard).pack(anchor="w")
