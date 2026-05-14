

class Emailbody:
    

 def build_email_body(self,employee, matches):

    recommendation_text = ""

    for index, match in enumerate(matches, start=1):

        recommendation_text += (
            f"{index}. "
            f"{match['first_name']} "
            f"{match['last_name']} "
             f"{match['email']}\n "
        )

    body = f"""
Hi {employee['first_name']},

Here are your employee connection recommendations for this month:

{recommendation_text}

Choose one person and schedule a casual non-work conversation.

Once completed, send confirmation to HR.

Enjoy connecting.
"""

    return body