import customtkinter as ctk
from tkinter import messagebox, ttk
# Import logic module robustly in both package and standalone contexts.
try:
    # Preferred: relative import when running as a package
    from .database import logic
except Exception:
    # Fallbacks: try absolute import names and adjust sys.path so tooling/standalone runs work
    import importlib, os, sys
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(pkg_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    logic = None
    # Try a few possible module names
    for mod_name in ("logic", "CareerCompass.logic"):
        try:
            logic = importlib.import_module(mod_name)
            break
        except Exception:
            continue
    if logic is None:
        raise

class CareerCompassApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CareerCompass - Student Edition")
        self.geometry("700x550")
        
        # App State variables
        self.current_user_id = None
        
        # Main container frame to stack all screens
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # Show initial login screen
        self.show_login_screen()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_container()
        frame = ctk.CTkFrame(self.container)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(frame, text="Welcome to CareerCompass", font=("Arial", 18, "bold")).pack(pady=10)
        
        # Mocking student simple login registration
        ctk.CTkLabel(frame, text="Enter Name to Login/Register:").pack(pady=5)
        name_entry = ctk.CTkEntry(frame, width=30)
        name_entry.pack(pady=5)
        
        def handle_login():
            name = name_entry.get().strip()
            if not name:
                messagebox.showerror("Error", "Please enter your name!")
                return
            
            # Simple automatic user check/creation for student app flow
            user_id = logic.create_user(name, 20, "Undergraduate", "Python, Excel", "Software, Data", "None")
            self.current_user_id = user_id
            self.show_dashboard()

        ctk.CTkButton(frame, text="Get Started", command=handle_login).pack(pady=15)

    def show_dashboard(self):
        self.clear_container()
        user_data = logic.get_user(self.current_user_id)
        
        # Top Menu Bar Frame
        nav_bar = ctk.CTkFrame(self.container, fg_color="#333")
        nav_bar.pack(fill="x", side="top")
        
        ctk.CTkLabel(nav_bar, text=f"Welcome, {user_data['name']}", font=("Arial", 10, "bold")).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(nav_bar, text="Logout", command=self.show_login_screen).pack(side="right", padx=10, pady=5)
        
        # Main Dashboard Content Frame
        main_frame = ctk.CTkFrame(self.container)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(main_frame, text="Dashboard", font=("Arial", 16, "bold")).pack(anchor="w", pady=10)
        
        # Buttons to navigate everywhere
        ctk.CTkButton(main_frame, text="1. Update Profile & Skills", command=self.show_profile_screen).pack(pady=10, fill="x")
        ctk.CTkButton(main_frame, text="2. Take Career Quiz", command=self.show_quiz_screen).pack(pady=10, fill="x")
        ctk.CTkButton(main_frame, text="3. Search Matched Jobs", command=self.show_jobs_screen).pack(pady=10, fill="x")
        ctk.CTkButton(main_frame, text="4. View Application History", command=self.show_applications_screen).pack(pady=10, fill="x")

    def show_profile_screen(self):
        self.clear_container()
        user_data = logic.get_user(self.current_user_id)
        
        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Edit Profile Info", font=("Arial", 16, "bold")).pack(pady=10)
        
        ctk.CTkLabel(frame, text="Skills (Comma Separated):").pack(anchor="w")
        skills_entry = ctk.CTkEntry(frame, width=50)
        skills_entry.insert(0, user_data["skills"])
        skills_entry.pack(pady=5)
        
        ctk.CTkLabel(frame, text="Interests (Comma Separated):").pack(anchor="w")
        interests_entry = ctk.CTkEntry(frame, width=50)
        interests_entry.insert(0, user_data["interests"])
        interests_entry.pack(pady=5)
        
        def save_profile():
            # Update user info in DB
            from database import get_connection
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users SET skills = ?, interests = ? WHERE user_id = ?
            """, (skills_entry.get(), interests_entry.get(), self.current_user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Profile updated successfully!")
            self.show_dashboard()
            
        ctk.CTkButton(frame, text="Save & Return", command=save_profile).pack(pady=15)
        ctk.CTkButton(frame, text="Back", command=self.show_dashboard).pack()

    def show_quiz_screen(self):
        self.clear_container()
        user_data = logic.get_user(self.current_user_id)
        
        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Career Recommendation Quiz", font=("Arial", 16, "bold")).pack(pady=10)
        ctk.CTkLabel(frame, text="Processing recommendations based on your saved profile...", font=("Arial", 11)).pack(pady=10)
        
        # Get results
        recs = logic.recommend_careers(user_data["skills"], user_data["interests"])
        
        if not recs:
            ctk.CTkLabel(frame, text="No strong matches found yet. Try expanding your profile skills!", text_color="#EF4444").pack(pady=10)
        else:
            for r in recs:
                card = ctk.CTkFrame(frame)
                card.pack(fill="x", pady=5)
                ctk.CTkLabel(card, text=f"{r['career_name']} ({r['score']}% Match)", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(8, 0))
                ctk.CTkLabel(card, text=f"Description: {r['description']}", wraplength=600, justify="left").pack(anchor="w", padx=10)
                ctk.CTkLabel(card, text=f"Required Skills: {r['required_skills']}", text_color="gray", font=("Arial", 9, "italic")).pack(anchor="w", padx=10, pady=(0, 8))
                
        ctk.CTkButton(frame, text="Back to Dashboard", command=self.show_dashboard).pack(pady=20)

    def show_jobs_screen(self):
        self.clear_container()
        user_data = logic.get_user(self.current_user_id)
        
        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Job Recommendations & Skill Gap Analysis", font=("Arial", 16, "bold")).pack(pady=10)
        
        jobs = logic.match_jobs(user_data["skills"])
        
        # Basic list display via scrollable frame
        canvas = ctk.CTkCanvas(frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda _: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for job in jobs:
            job_card = ctk.CTkFrame(scrollable_frame)
            job_card.pack(fill="x", expand=True, pady=5)
            
            ctk.CTkLabel(job_card, text=f"{job['title']} at {job['company']}", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(8, 0))
            ctk.CTkLabel(job_card, text=f"Match Rating: {job['score']}% | Field: {job['career_field']} | Level: {job['level']}").pack(anchor="w", padx=10)
            
            if job["missing_skills"]:
                gap_text = f"Skill Gap (Missing): {', '.join(job['missing_skills'])}"
                ctk.CTkLabel(job_card, text=gap_text, text_color="#FF6B6B", font=("Arial", 9, "bold")).pack(anchor="w", padx=10)
            else:
                ctk.CTkLabel(job_card, text="You have all required skills for this job!", text_color="#10B981", font=("Arial", 9, "bold")).pack(anchor="w", padx=10, pady=(0, 8))
                
            # Direct binding to keep tracking clean
            def make_apply_cmd(j_id=job['job_id']):
                return lambda: [logic.apply_to_job(self.current_user_id, j_id), messagebox.showinfo("Applied", "Application submitted successfully!")]
                
            ctk.CTkButton(job_card, text="Apply Now", command=make_apply_cmd()).pack(side="right", anchor="e", padx=10, pady=8)
            
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        ctk.CTkButton(frame, text="Back", command=self.show_dashboard).pack(side="bottom", pady=10)

    def show_applications_screen(self):
        self.clear_container()
        frame = ctk.CTkFrame(self.container)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Your Job Applications", font=("Arial", 16, "bold")).pack(pady=10)
        
        apps = logic.get_user_applications(self.current_user_id)
        
        if not apps:
            ctk.CTkLabel(frame, text="You haven't applied to any jobs yet!").pack(pady=20)
        else:
            for a in apps:
                row = ctk.CTkFrame(frame)
                row.pack(fill="x", pady=5)
                ctk.CTkLabel(row, text=f"• {a['title']} — {a['company']}", font=("Arial", 11)).pack(side="left")
                ctk.CTkLabel(row, text=f" [{a['status']}] ", text_color="#3B82F6", font=("Arial", 10, "bold")).pack(side="right")
                
        ctk.CTkButton(frame, text="Back to Dashboard", command=self.show_dashboard).pack(pady=20)
