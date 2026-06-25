import customtkinter as ctk
from tkinter import messagebox

# Import the database and service functions from the new package structure.
from database.database import (
    init_db,
    create_user,
    get_user,
    get_user_by_name,
    get_user_applications,
    insert_application,
    update_user_profile,
)
from gui.login_page import LoginPage
from gui.dashboard import DashboardPage
from gui.career_quiz import CareerQuizPage
from gui.jobs_page import JobsPage
from gui.applications_page import ApplicationsPage
from gui.profile_page import ProfilePage
from services.career_engine import recommend_careers
from services.job_matcher import match_jobs


class CareerCompassApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("CareerCompass")
        self.geometry("800x600")
        self.resizable(False, False)

        self.current_user_id = None
        self.current_user = None

        self.container = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.container.pack(fill="both", expand=True)

        init_db()
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_screen()
        page = LoginPage(self.container, self)
        page.pack(fill="both", expand=True)

    def login(self, user_id):
        self.current_user_id = user_id
        self.current_user = get_user(user_id)
        self.show_dashboard()

    def logout(self):
        self.current_user_id = None
        self.current_user = None
        self.show_login_screen()

    def find_or_create_user(self, name):
        existing_user = get_user_by_name(name)
        if existing_user:
            return existing_user["user_id"]

        return create_user(
            name,
            18,
            "High School",
            "Python, Excel",
            "Technology, Writing",
            "None"
        )

    def get_current_user(self):
        return self.current_user or {}

    def show_dashboard(self):
        self.clear_screen()
        page = DashboardPage(self.container, self)
        page.pack(fill="both", expand=True)

    def show_career_quiz(self):
        self.clear_screen()
        page = CareerQuizPage(self.container, self)
        page.pack(fill="both", expand=True)

    def show_jobs(self):
        self.clear_screen()
        page = JobsPage(self.container, self)
        page.pack(fill="both", expand=True)

    def show_applications(self):
        self.clear_screen()
        page = ApplicationsPage(self.container, self)
        page.pack(fill="both", expand=True)

    def show_update_profile(self):
        self.clear_screen()
        page = ProfilePage(self.container, self)
        page.pack(fill="both", expand=True)

    def get_recommendations(self):
        user = self.get_current_user()
        return recommend_careers(user.get("skills", ""), user.get("interests", ""))

    def get_jobs(self):
        user = self.get_current_user()
        return match_jobs(user.get("skills", ""))

    def apply_to_job(self, job_id):
        # Save a new application for the logged-in user.
        if self.current_user_id is None:
            return
        insert_application(self.current_user_id, job_id)

    def get_applications(self):
        if self.current_user_id is None:
            return []
        return get_user_applications(self.current_user_id)

    def update_user_profile(self, skills, interests):
        # Update the user profile in the database and refresh cached user data.
        if self.current_user_id is None:
            return
        update_user_profile(self.current_user_id, skills, interests)
        self.current_user = get_user(self.current_user_id)


if __name__ == "__main__":
    app = CareerCompassApp()
    app.mainloop()
