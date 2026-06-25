from database.database import get_all_jobs


def match_jobs(user_skills):
    """Match jobs to user skills and show missing skills if needed."""
    jobs = get_all_jobs()
    skills = [skill.strip().lower() for skill in user_skills.split(',') if skill.strip()]
    matched = []

    for job in jobs:
        required = [item.strip().lower() for item in job["required_skills"].split(',') if item.strip()]
        matched_count = 0
        missing = []

        for requirement in required:
            if requirement in skills:
                matched_count += 1
            else:
                missing.append(requirement.title())

        score = int((matched_count / len(required)) * 100) if required else 0
        matched.append({
            "job_id": job["job_id"],
            "title": job["title"],
            "company": job["company"],
            "career_field": job["career_field"],
            "required_skills": job["required_skills"],
            "level": job["level"],
            "score": score,
            "missing_skills": missing
        })

    matched.sort(key=lambda item: item["score"], reverse=True)
    return matched
