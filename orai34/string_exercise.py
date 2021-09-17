python = "python"
lenght_python = len("python")
print(lenght_python)

print(python[0])
print(python[-1])

str2 = "hallgató"
str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
str2_position_in_str3 = str3.find(str2)
print(str3[str2.find(str3):str2_position_in_str3 + len(str2)])

str4 = "Elemi"
str5 = "Programozás"

print(str4 +" "+ str5)
