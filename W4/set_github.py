fruits = {'apple','manggo'}
citrus_fruits = {'manggo','pelam','papaya'}



# Perform set operations
union_fruits_citrus = fruits.union(citrus_fruits)
intersection_fruits_citrus = fruits.intersection(citrus_fruits)
#difference_fruits_citrus = fruits.difference(citrus_fruits)

difference_fruits_citrus = citrus_fruits.difference(fruits)


print(union_fruits_citrus)
print(intersection_fruits_citrus)
print(difference_fruits_citrus)