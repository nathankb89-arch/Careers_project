from database.database import get_all_careers


def recommend_careers(user_skills, user_interests):
    """Return simple career recommendations based on skills and interests."""
    careers = get_all_careers()
    skills = [skill.strip().lower() for skill in user_skills.split(',') if skill.strip()]
    interests = [interest.strip().lower() for interest in user_interests.split(',') if interest.strip()]

    recommendations = []
    for career in careers:
        required = [item.strip().lower() for item in career["required_skills"].split(',') if item.strip()]
        match_count = sum(1 for skill in skills if skill in required)
        score = int((match_count / len(required)) * 100) if required else 0

        bonus = 0
        for interest in interests:
            if interest and interest in career["career_name"].lower():
                bonus = 20
                break

        total = score + bonus
        if total >= 20:
            recommendations.append({
                "career_name": career["career_name"],
                "description": career["description"],
                "required_skills": career["required_skills"],
                "score": total
            })

    # sort from best match to weakest match
    recommendations.sort(key=lambda item: item["score"], reverse=True)
    return recommendations[:3]
