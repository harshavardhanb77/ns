age=int(input("Enter the age in days"))
years=age//365
weeks=(age%365)//7
days=age-((years*365)+(weeks*7))
print(years,",",weeks,",",days)