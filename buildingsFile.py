class Building:
    building_name = ""
    city = ""
    country = ""
    height = ""
    floors = ""


def readData():
    inputFile = open("buildings.txt", "r")

    BuildingsList = []

    for eachLine in inputFile:
        building = eachLine.strip().split(",")

        record = Building
        record.building_name = building[0]
        record.city = building[1]
        record.country = building[2]
        record.height = float(building[3])
        record.floors = int(building[4])

        BuildingsList.append(record)

    inputFile.close()
    return BuildingsList

def findTallestBuilding(buildings):
    maxvalue = buildings[0]
    for eachElement in range(len(buildings)):
        if buildings[eachElement].height > maxvalue.height:
            maxvalue = building[eachElement]
    print("Tallest Building is " + maxvalue.building_name + ", " + maxvalue.city + ", " + maxvalue.country)

def countChinaBuildings(buildings):
    counter = 0
    for eachBuilding in range(len(buildings)):
        if buildings[eachBuilding].country == "China":
            counter = counter + 1
            return counter

def printOutput(number):
        buildingInChina = number
        print("There are", buildingsInChina, "buildings in China.")

buildings = readData()
findTallestBuilding(buildings)
buildingsInChina = countChinaBuildings(buildings)
printOutput(buildingsInChina)
