from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name: str 
    family: str
    email_adress: str
    created_date: str = None
    updated_date: str = None
  

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, id: int):
        self._id = id



    @property
    def name(self) -> str:
        return self._name 
    @name.setter
    def name(self, name: str):
        self._name = name



    @property
    def family(self) -> str:
        return self._family 
    @family.setter
    def family(self, family: str):
        self._family = family        


    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, email_adress: str):
        self._email_adress = email_adress


    @property
    def created_date(self):
        return self._created_date
    @created_date.setter
    def created_date(self, created_date:str):
        self._created_date = created_date    

    
