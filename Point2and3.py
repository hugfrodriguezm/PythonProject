import random
import hashlib
class Point2and3:
    
#Contructor
    
    def __init__(self,APIRequest): 
        self.__APIRequest=APIRequest

#Getters and setters 
    
    def GetAPIRequest(self):
     return self.__APIRequest
    
    def SetAPIRequest(self,APIRequest):
     self.__APIRequest=APIRequest 
 

#Functions
    #Recursive function to set all data for this dataset: 
    # Inputs var: This is a variable that contains important informmation:
    # Output (string): This is a string with only the important content for the excercise 
    
    def SetText(self,var):
      if(isinstance(var, str)):
        return var
      elif(isinstance(var, dict)):
        return var.values()
      elif(isinstance(var, list)):
        List=[]
        for i in var:
          List.append(self.SetText(i))
        return List 

    #Function to extrac the important information for point 2 and 3 
    #Inputs KeyInput(String)= Input to compare with dataset number 2
    ####    Input(string)= Information of dataset number 1
    ###     KeysOutput(list)= Informatio that will be extract in dataset number 2
    ###     Subindex (String)= Variable to extract the important information only
    # Output(List): List with the information will be used of dataset in pandas

    def OutputToChoose(self,KeyInput,Input,KeysOutput,Subindex):
        Output= []
        while(Output == []):
          Index=random.randint(0,len(self.__APIRequest))
          for i in self.__APIRequest[Index:]:
              if (i[KeyInput] == Input):
                for j in KeysOutput:
                  if(j is 'languages'):
                    Aux_List=[]
                    for k in i[j]:
                      Aux_List.append(hashlib.sha1(k[Subindex].encode()).hexdigest())
                    Output.append(tuple(Aux_List))
                  else:  
                    Output.append(self.SetText(var=i[j]))
                break
        return Output
