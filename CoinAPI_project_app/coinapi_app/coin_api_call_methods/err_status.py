# Hidden function
def print_error_status(response, method_name):
    print("Status Code:", response.status_code)
    print("Status Message:", response.reason)
    
    reasons = ["There is something wrong with your request", "Your API key is wrong", "Your API key doesnt't have enough privileges to access this resource",
               "You have exceeded your API key rate limits", "You requested specific single item that is not available"]
    codes = [400, 401, 403, 429, 550]
    codes
    if response.status_code in codes:
        print("Possible Reason:", reasons[codes.index(response.status_code)],"for the", method_name,"method.")
    