employeeInfo={"Name":"Eddy",
             "Age":24,
             "City":"London"
             }

def searchDict(dict,value):
    found=False
    for key in dict:
        if dict[key]==value:
            print("Value Exists in key:",key)
            found=True
    if found==False:
        print("Value does not exist")
searchDict(employeeInfo,"London")