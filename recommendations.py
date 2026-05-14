from loadEmployees import LoadEmployees
import random

class Recommendations:

   # CREATE RECOMMENDATIONS


 def create_recommendations(df, num_recommendations=3):

    employees = df.to_dict("records")

    recommendations = {}

    for employee in employees:

        # Remove current employee
        possible_matches = [
            emp for emp in employees
            if emp["email"] != employee["email"]
        ]

        # Random recommendations
        matches = random.sample(
            possible_matches,
            min(num_recommendations, len(possible_matches))
        )

        recommendations[employee["email"]] = {
            "employee": employee,
            "matches": matches
        }

    return recommendations 