from pydantic import BaseModel

class Customer(BaseModel):
    Tenure_in_Months:int
    Monthly_Charge:float
    Total_Charges:float