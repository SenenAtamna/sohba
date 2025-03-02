from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name: str 
    family: str
    email_adress: str
    created_date: str = None
    updated_date: str = None
  

    def id(self) -> int:
        return self._id

   
    def id(self, id: int):
        self._id = id

    
    def name(self) -> str:
        return self._name

    
    def name(self, name: str):
        self._name = name


    def family(self) -> str:
        return self._family

    
    def family(self, family: str):
        self._family = family        



    def email(self) -> str:
        return self._email


    def email(self, email_adress: str):
        self._email_adress = email_adress

    def created_date(self):
        return self._created_date

    def created_date(self, created_date:str):
        self._created_date = created_date    

    
