import csv
import requests
import random

response = requests.get("https://openlibrary.org/works/OL45883W.json")

respJson = response.json()

print(respJson["subject_people"]) #Teste
print(respJson["subject_places"])
print(respJson["subject_times"])
print(respJson["subjects"])

#Abre e da append no arquivo tsv
file = open("Fantastic_Mr. Fox.tsv","a")
file.write("{}\t{}\n".format(random.choice(respJson["subject_people"]), random.choice(respJson["subject_places"])))
file.write("{}\t{}\n".format(random.choice(respJson["subject_times"]), random.choice(respJson["subjects"])))
file.close()


