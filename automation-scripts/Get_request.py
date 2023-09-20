import requests
import json

'''host_url = "http://34.93.32.208/products/company-details?product_id=5208648&source=CATALOG"
response_code = requests.get(host_url)
print("The response from this GET request")
print(response_code)'''

host_url = "http://34.93.32.208/products/incorrect_contact_reporting"
body = {
    "fname":"dipanshu",
    "lname":"singhjadon",
    "title":"Mr.",
    "profile_id":"8528706",
    "email":"dipanshu.s@tradeindia.com",
    "complaint":"issue in laptop",
    "contact":"+919999332927"
    
}
response_code = requests.post(host_url,data=body)
print(response_code)

response_result = (json.dumps(response_code.json(), indent=4))
print(response_result)
