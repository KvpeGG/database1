import encryptor

dataFile = open("data.txt", "a")


def addValue(key, value):
    dataFile.writelines(f"{key}={value}\n")


def readValue(value):
    for i, line in enumerate(dataFile):
        if line.split("=")[0] == value:
            return line.removeprefix(value + "=")


print("Please pick operation")

print("r: Read value")
print("w: Write value")

option = input()

if option == "r":
    dataFile = open("data.txt", "r")
    value = input("Enter the value: ")
    print(readValue(value))
elif option == "w":
    open("data.txt", "a")
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    addValue(key, value)

dataFile.close()