import requests
import json


def get_resp(api):
    response = requests.get(api)
    if response.status_code == 200:
        resp = response.json()
        #print(len(resp))
        return response.json()
    else:
        print("Error. Status Code:",response.status_code,"\n")
        return 1
    
    
def get_resp_param(year):
    parameters = {
    "year": year
    }
    response = requests.get("https://data.cityofchicago.org/resource/crimes.json", params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error. Status Code:",response.status_code,"\n")
        return 1

    
def get_headers(api):
    response = requests.get(api)
    response.encoding = 'utf-8'
    headers = response.headers
    if response.status_code == 200:
        for dict_key in headers:
            print(dict_key, headers[dict_key])
    else:
        print("Error. Status Code:",response.status_code,"\n")
        return 1
      
        
def print_resp(data):
    for dict_item in data:
        for item in dict_item:
            print(item, dict_item[item])
        print("\n")
    print("\nData size:", len(data))
    
    
def count_crimes(data, year):
    L = []
    D = {}
    ordered_L = []
    
    for dict_item in data:
        L.append(dict_item["primary_type"])
        
    for i in range(len(L)):
        word = L[i]
        if word !='':
            if word not in D:
                D.update({word:1})
            else:
                D[word] = D[word] + 1
    
    
    for i in range(len(D)):
        Dkey = ""
        Dvalue = 0
        for k, v in D.items():
            if v > Dvalue:
                Dvalue = v
                Dkey = k
        ordered_L.append([Dkey, Dvalue])
        del D[Dkey]
        
    print("\n Reported Crime Type for", year)
    
    for i in range(3):
        word = ordered_L[i][0]
        count = ordered_L[i][1]
        nice_print = '-'*(4-len(str(count)))+">"
        print("  ",count,nice_print,word)
    #print(" Total Count:", len(ordered_L),"\n")
    
    
def main():
    api = "https://data.cityofchicago.org/resource/crimes.json"
    
    start = 2001
    years= []
    
    get_resp(api)
    #get_headers(api)
    
    print("\n Top 3 reported crimes from 2001 to 2019\n")
    for i in range(19):
        years.append(start)
        start+=1
    for year in years:
        count_crimes(get_resp_param(year),year)
    
    
main()