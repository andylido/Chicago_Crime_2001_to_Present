import requests
import json

def get_resp(year):
    parameters = {
    "year": year
    }
    response = requests.get("https://data.cityofchicago.org/resource/crimes.json", params=parameters)
    if response.status_code == 200:
        return response.json()
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
    for dict_item in data:
        L.append(dict_item["primary_type"])
    D = {}
    for i in range(len(L)):
        word = L[i]
        if word !='':
            if word not in D:
                D.update({word:1})
            else:
                D[word] = D[word] + 1
    ordered_L = []
    for i in range(len(D)):
        Dkey = ""
        Dvalue = 0
        for k, v in D.items():
            if v > Dvalue:
                Dvalue = v
                Dkey = k
        ordered_L.append([Dkey, Dvalue])
        del D[Dkey]
    print(" Reported Crime Type for", year)
    for i in range(3):
        word = ordered_L[i][0]
        count = ordered_L[i][1]
        nice_print = '-'*(4-len(str(count)))+">"
        print("  ",count,nice_print,word)
    #print(" Total Count:", len(ordered_L),"\n")
    
def main():
    start = 2001
    years= []
    for i in range(19):
        years.append(start)
        start+=1
    for year in years:
        count_crimes(get_resp(year),year)
    #data2017 = get_resp(2017)
    #data2018 = get_resp(2018)
    #data2019 = get_resp(2019)
    #count_crimes(data2017,2017)
    #count_crimes(data2018, 2018)
    #count_crimes(data2019, 2019)
    
main()