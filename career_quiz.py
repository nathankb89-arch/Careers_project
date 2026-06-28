import customtkinter as ctk
from tkinter import messagebox
from .recommendations import RecommendationsFrame
from database.database import get_all_careers


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

        # Back to Dashboard button (header)
        back_header_btn = ctk.CTkButton(header_frame, text="← Back to Dashboard", width=180, height=36, font=("Segoe UI", 11, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=self.app.show_dashboard)
        back_header_btn.pack(side="right")

        # Divider
        divider = ctk.CTkFrame(self, fg_color="#333333", height=2)
        divider.pack(fill="x", padx=20, pady=15)

        # Career selector for focused questions
        careers = [c for c in get_all_careers() if c and c.get('career_name')]
        career_names = [c['career_name'] for c in careers]

        selector_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        selector_frame.pack(fill="x", padx=20, pady=(0, 10))
        ctk.CTkLabel(selector_frame, text="Choose a career to answer focused questions:", font=("Segoe UI", 11), text_color="#9CA3AF").pack(anchor="w")
        self.career_menu = ctk.CTkOptionMenu(selector_frame, values=career_names, command=self.on_career_selected)
        if career_names:
            self.career_menu.set(career_names[0])
        else:
            self.career_menu.set("No careers available")
        self.career_menu.pack(anchor="w", pady=(6, 8))

        # Questions area (will be populated when a career is selected)
        self.questions_container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.questions_container.pack(fill="both", expand=False, padx=20, pady=(0, 10))

        # Recommendations list below the questions
        recommendations = self.app.get_recommendations()
        RecommendationsFrame(self, recommendations).pack(fill="both", expand=True, padx=20, pady=10)

        # Render initial questions for default selection
        if career_names:
            self.render_questions_for(careers[0])

        # Back button
        button_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        button_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkButton(button_frame, text="← Back to Dashboard", height=40, font=("Segoe UI", 12, "bold"), fg_color="#2d5a8c", hover_color="#3a6baa", command=self.app.show_dashboard).pack(anchor="w")

    def on_career_selected(self, value):
        careers = get_all_careers()
        for c in careers:
            if c and c.get('career_name') == value:
                self.render_questions_for(c)
                return
        self.render_questions_for(None)

    def render_questions_for(self, career):
        for w in self.questions_container.winfo_children():
            w.destroy()

        if not career or not isinstance(career, dict):
            ctk.CTkLabel(self.questions_container, text="No career questions are available right now.", font=("Segoe UI", 12), text_color="#CCCCCC").pack(anchor="w", pady=(10, 10))
            return

        field = (career.get('career_field') or '').lower()
        name = career.get('career_name', 'Career')

        ctk.CTkLabel(self.questions_container, text=f"Quick Questions — {name}", font=("Segoe UI", 13, "bold"), text_color="#00D4FF").pack(anchor="w", pady=(6, 4))

        question_bank = {
            'data': [
                "How comfortable are you with SQL and databases?",
                "Do you enjoy creating charts and interpreting trends?",
                "Rate your experience with Python or R (None/Basic/Intermediate/Advanced)"
            ],
            'software': [
                "How many programming projects have you completed?",
                "Do you enjoy debugging and problem solving? (Yes/No)",
                "Which languages do you prefer?"
            ],
            'marketing': [
                "Have you worked on social media campaigns before? (Yes/No)",
                "Do you enjoy writing and storytelling? (Yes/No)",
                "Rate your familiarity with SEO (None/Basic/Intermediate/Advanced)"
            ],
            'design': [
                "Which creative tools do you use (e.g., Photoshop, Figma)?",
                "Do you prefer visual design or product design?",
                "Do you enjoy client-driven briefs and iteration? (Yes/No)"
            ],
            'cosmetics': [
                "Are you comfortable advising customers one-on-one? (Yes/No)",
                "How much practical makeup experience do you have? (None/Some/Extensive)",
                "Do you enjoy learning new product formulas and trends? (Yes/No)"
            ]
        }

        questions = question_bank.get(field, [
            "Why does this career interest you?",
            "What strengths would you bring to this role?",
            "What would you like to learn to prepare for this career?"
        ])

        self._answer_vars = []
        for q in questions:
            frame = ctk.CTkFrame(self.questions_container, fg_color="#1f2224")
            frame.pack(fill="x", pady=(6, 6))
            ctk.CTkLabel(frame, text=q, font=("Segoe UI", 10), text_color="#CCCCCC").pack(anchor="w", padx=10, pady=(6, 2))
            entry = ctk.CTkEntry(frame, width=1, height=34, font=("Segoe UI", 10), fg_color="#2d2f31")
            entry.pack(fill="x", padx=10, pady=(0, 8))
            self._answer_vars.append((q, entry))

        submit_frame = ctk.CTkFrame(self.questions_container, fg_color="#1a1a1a")
        submit_frame.pack(fill="x", pady=(8, 0))
        submit_btn = ctk.CTkButton(submit_frame, text="Submit Answers", width=160, height=36, fg_color="#06b6d4", hover_color="#09a6bd", command=lambda: self.submit_answers(name))
        submit_btn.pack(anchor="e")

    def submit_answers(self, career_name):
        answers = {q: e.get().strip() for q, e in getattr(self, '_answer_vars', [])}
        self.app.last_quiz_answers = getattr(self.app, 'last_quiz_answers', {})
        self.app.last_quiz_answers[career_name] = answers
        messagebox.showinfo("Thanks", "Your answers have been recorded. This helps tailor recommendations.")
