# =====================================
# GreenCampus AI Sustainability Metrics
# =====================================

def calculate_sustainability_score(
    energy_risk,
    water_risk,
    waste_risk
):

    score = 100

    if "High" in energy_risk:
        score -= 30
    elif "Medium" in energy_risk:
        score -= 15

    if "High" in water_risk:
        score -= 30
    elif "Medium" in water_risk:
        score -= 15

    if "High" in waste_risk:
        score -= 30
    elif "Medium" in waste_risk:
        score -= 15

    return max(score, 0)