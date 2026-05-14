from emailbody import Emailbody
import yagmail



class Sendmail:

    

 def send_emails(self,recommendations):

    yag = yagmail.SMTP(
        EMAIL,
        APP_PASSWORD
    )

    for data in recommendations.values():

        employee = data["employee"]

        matches = data["matches"]
        emailbody=Emailbody()
        body =emailbody. build_email_body(employee,matches)

        yag.send(
            to=employee["email"],
            subject="Monthly Employee Connection Recommendations",
            contents=body
        )

        print(
            f"Email sent to "
            f"{employee['first_name']} "
            f"{employee['last_name']}"
        )