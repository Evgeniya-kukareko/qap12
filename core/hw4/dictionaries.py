school = {"1a": 20,
          "2б": 23,
          "3в": 25,
          "4г": 30,
          "5а": 21,
          "6б": 32,
          "7в": 24,
          "8г": 31,
          "9а": 23,
          "10б": 27}

# print(school["1a"])

school.update({"4г": 10, "6б": 10})
school["8г"] = 10

school.update({"4a": 7, "4б": 7})
school["4в"] = 7

del school["1a"]

# print(school)
