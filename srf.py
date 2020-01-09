import json 
import csv

csv_list = []
user_agents = []

with open("C:\\Users\\Jay\\Desktop\\http.log") as json_file:
    data = json.load(json_file)
    SQLi        = ['UNION', "1' ","'1=1"]           #29
    xss         = ['<script>', 'alert(']     #16
    shellshock  = ['() { :; };']             #6
    LFI         = ['../', '/etc/passwd/']    #11
    for entry in data:
        for vuln in ('<script>', 'alert(','/../../', "1' ", "UNION", "() { :; };","/etc/passwd"): #xss,lfi,shellshock,sqli
            if vuln in entry["uri"] or vuln in entry["user_agent"] or vuln in entry["referrer"] or vuln in entry["host"] or vuln in entry["username"]:
                if entry['id.orig_h'] not in csv_list:
                    csv_list.append(entry['id.orig_h'])
                if entry['user_agent'] not in user_agents:
                    user_agents.append(entry['user_agent'])
    for agent in data:
        if agent['user_agent'] in user_agents:
            #import pdb; pdb.set_trace()
            if agent['id.orig_h'] not in csv_list:
                csv_list.append(agent['id.orig_h'])


with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_list)

print(len(csv_list))
print(csv_list)
