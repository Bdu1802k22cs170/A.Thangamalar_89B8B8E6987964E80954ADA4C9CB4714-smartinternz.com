"""
write a function called linear_search_products and a target product
name as input.the function should perform a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found or an empty list if the product is not
found
"""


def LinearSearchProduct(productlist, Target product):
indices=[]

forindex, product in enumerate(productlist):
  if product==Target product:
  indices.append(index)

  return indices


#example usage:
products=["shoes","boot","loafer","shoes","sandal","shoes "]
Target="shoes"
result=linearsearchproduct(products, Target)
print(result)