percentage=float(input("Enter percentage: "))
income =int(input("Enter family income: "))

percentage_ok =income >=75
income_ok = income <= 30000


print("percentage_ok:", percentage_ok)
print("inconme_ok:", income_ok)
print("schloarship eligible:",percentage_ok and income_ok)
print("at least one condition:",percentage or income_ok)
print("not percentage_ok:",not percentage_ok)
