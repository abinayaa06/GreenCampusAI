# =====================================
# GreenCampus AI - Agent System
# =====================================

from recommendations import (
    energy_recommendations,
    water_recommendations,
    waste_recommendations
)

# =====================================
# Energy Agent
# =====================================

def energy_agent(electricity, students):

    usage_per_student = electricity / students

    if usage_per_student > 10:
        return "🔴 High", energy_recommendations

    elif usage_per_student > 5:
        return "🟡 Medium", energy_recommendations

    return "🟢 Low", energy_recommendations


# =====================================
# Water Agent
# =====================================

def water_agent(water, students):

    usage_per_student = water / students

    if usage_per_student > 500:
        return "🔴 High", water_recommendations

    elif usage_per_student > 250:
        return "🟡 Medium", water_recommendations

    return "🟢 Low", water_recommendations


# =====================================
# Waste Agent
# =====================================

def waste_agent(waste, students):

    waste_per_student = waste / students

    if waste_per_student > 2:
        return "🔴 High", waste_recommendations

    elif waste_per_student > 1:
        return "🟡 Medium", waste_recommendations

    return "🟢 Low", waste_recommendations


# =====================================
# Carbon Impact Agent
# =====================================

def carbon_agent(electricity):

    carbon_emission = round(
        electricity * 0.82,
        2
    )

    return carbon_emission


# =====================================
# Planning Agent
# =====================================

def planning_agent(
    energy_risk,
    water_risk,
    waste_risk
):

    issues = []

    if "High" in energy_risk:
        issues.append("Reduce electricity consumption")

    if "High" in water_risk:
        issues.append("Improve water conservation")

    if "High" in waste_risk:
        issues.append("Improve waste management")

    if not issues:
        issues.append(
            "Campus sustainability performance is good."
        )

    return issues