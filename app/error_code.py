from enum import Enum
class ErrorCode(Enum):
    #Business Error related Exceptions
    B0001 = "Authentication failed"
    B0002 = "Reached login limit"
    B0003 = "Already registered account"
    
    B2001 = "No active card"
    B2002 = "National ID is not available"
    
    #System Error related Exceptions
    S0001 = "DB Error: DB access error"
    S0002 = "DB Error: Cannot find specified data in DB"
    
    S1001 = "Host Error: System Error"
    S1002 = "Host Error: Connection Timeout"
    S1003 = "Host Error: Network Error"
    S1004 = "Host Error: Gateway Internal Error"
    S9991 = "Unexpected System Exception - HTTP Web Errors"
    S9992 = "Unexpected System Exception - Web Validation Errors"
    S9999 = "Unexpected System Exception"
    
# print(Color.RED.name)
# print(Color.RED.value)

# #get name from value
# print(Color(1).name)
