from decimal import Decimal
def makeChange(amount = None):
    """
    Create two lists:
    money: store the amount of the bill
            To perform exact calculations, multiply all the amount of bills by 1000, 
            which should be [20,10,5,1,0.25,0.1,0.05,0.1] at first, then all the calculations 
            and comparisons are done among integers.
    result: empty list used to store the output 
    """
    money, result = [20000, 10000, 5000, 1000, 250, 100, 50, 10], []
    
  
    #If there is no input or the input is string or the input is out of range[0,100), return empty list
    
    if amount == None or type(amount) == str or amount <0 or amount >= 100:
        return result
      
    # Multiply the amount by 1000, and keep the integer part(keep the digits till thousands places)
    amount = int(Decimal(str(amount)) * 1000)
    
    # Scan the money list, calculate the number of bills one by one and append the result to the output list
    for x in money:
        result.append(amount // x)
        amount = amount % x
    
    #If amount is no less than 5(thousands places is no less than 5), add one penny, else do nothing
    if amount >= 5:
        result[-1] += 1
    else:
        pass
    return result
   
    