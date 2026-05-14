from loadEmployees import LoadEmployees
from recommendations import Recommendations


sheetID='********************************'


def main():
     load_EmployeeData=LoadEmployees()
     df= load_EmployeeData.load_employees(sheetID)
     employee_recommendations =Recommendations()
     recommendations =employee_recommendations.create_recommendations(df)




    

   

if __name__ == "__main__":
    main()