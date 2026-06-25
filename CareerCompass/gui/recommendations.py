import customtkinter as ctk


class RecommendationsFrame(ctk.CTkFrame):
    def __init__(self, parent, recommendations):
        super().__init__(parent, fg_color="#1a1a1a")
        self.pack(fill="both", expand=True, padx=0, pady=0)
        self.recommendations = recommendations
        self.build_frame()

    def build_frame(self):
        if not self.recommendations:
            empty_frame = ctk.CTkFrame(self, fg_color="#2d2d2d", corner_radius=10)
            empty_frame.pack(fill="both", expand=True, padx=5, pady=5)
            ctk.CTkLabel(empty_frame, text="📭 No recommendations available yet", font=("Segoe UI", 12), text_color="#888888").pack(pady=20)
            return

        for idx, item in enumerate(self.recommendations):
            card = ctk.CTkFrame(self, fg_color="#2d2d2d", corner_radius=12)
            card.pack(fill="x", expand=False, padx=5, pady=8)
            
            # Header with score
            header_frame = ctk.CTkFrame(card, fg_color="#2d2d2d")
            header_frame.pack(fill="x", padx=15, pady=(15, 5))
            header_frame.grid_columnconfigure(0, weight=1)
            
            ctk.CTkLabel(header_frame, text=f"{item['career_name']}", font=("Segoe UI", 13, "bold"), text_color="#00D4FF").grid(row=0, column=0, sticky="w")
            
            # Score badge
            score_text = f"{item['score']}% Match"
            score_color = "#10B981" if item['score'] >= 70 else "#F59E0B" if item['score'] >= 50 else "#EF4444"
            ctk.CTkLabel(header_frame, text=score_text, font=("Segoe UI", 11, "bold"), text_color=score_color).grid(row=0, column=1, sticky="e")
            
            # Description
            ctk.CTkLabel(card, text=item['description'], font=("Segoe UI", 10), text_color="#CCCCCC", wraplength=700, justify="left").pack(anchor="w", padx=15, pady=(0, 8))
            
            # Skills
            ctk.CTkLabel(card, text=f"Required Skills: {item['required_skills']}", font=("Segoe UI", 9), text_color="#888888").pack(anchor="w", padx=15, pady=(0, 15))
