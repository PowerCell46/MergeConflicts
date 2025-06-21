import pandas as pd

peopleData = pd.read_csv("./data.csv")

malesPeopleData = peopleData[peopleData["gender"] == "male"]
# print(malesPeopleData)

femalesPeopleData = peopleData[peopleData["gender"] == "female"]
# print(femalesPeopleData)

print(peopleData.info())

peopleData["wage"].plot()