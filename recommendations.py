from loadEmployees import LoadEmployees
import random

import random


class Recommendations:

    def create_recommendations(
        self,
        df,
        num_recommendations=3
    ):

        employees = df.to_dict("records")

        recommendations = {}

        for employee in employees:

            possible_matches = [
                emp for emp in employees
                if emp["email"] != employee["email"]
            ]

            matches = random.sample(
                possible_matches,
                min(num_recommendations, len(possible_matches))
            )

            recommendations[employee["email"]] = {
                "employee": employee,
                "matches": matches
            }

        return recommendations