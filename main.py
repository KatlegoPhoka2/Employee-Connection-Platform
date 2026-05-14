from loadEmployees import LoadEmployees
from recommendations import Recommendations
from sendmail import Sendmail

import pandas as pd





def main():
     load_EmployeeData=LoadEmployees()
     df= load_EmployeeData.load_employees(sheetID)
     employee_recommendations =Recommendations()
     recommendations =employee_recommendations.create_recommendations(df)
     mailsend=Sendmail()
     mailsend.send_emails(recommendations)






    

   

if __name__ == "__main__":
    main()