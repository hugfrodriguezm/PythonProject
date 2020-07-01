class Point1:

    #Contructor
    
    def __init__(self,APIRequest): 
        self.__APIRequest=APIRequest 
 
    #Getters and setters 
    
    def GetAPIRequest(self):
     return self.__APIRequest
    
    def SetAPIRequest(self,APIRequest):
     self.__APIRequest=APIRequest 
 
    # This function find uniques values of any key of a list
    # Inputs varlist: List to test all information
    # Inputs key: key to find Uniques values
    
    # Output (string): This is a string with only the important content for the excercise
    def _FindDiferentKeys(self,key,varlist): 
      UniqueList=[]
      for i in varlist:
        if i[key] not in UniqueList:
         UniqueList.append(i[key])
      return UniqueList