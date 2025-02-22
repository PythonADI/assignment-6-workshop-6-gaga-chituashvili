student = [{
    "name":"george",
    "age":19,
    "courses":"business"
}]

for students in student:
    print(f'{students["name"]} {students["age"]}')




for students in student:
    students["GPA"]="3.5"
    print(students)


for sdutents in student:
    students["adress"]={
        "city":"tbilisi",
        "zip_code":1331
    }
    print(students)


for students in student:
    print(sdutents.keys())
    print(students.values())

for students in student:
    print(f""" 
///////////////////////
name:{students['name']}
//////////////////////
age:{students['age']}
//////////////////////
courses:{students["courses"]}
//////////////////////
city:{students["adress"]["city"]}
//////////////////////
zip_code:{students["adress"]["zip_code"]}
""")
    





student = [{
    "name":"george",
    "age":19,
    "courses":"business"
},{
     "name":"joe",
    "age":21,
    "courses":"Criminal law"
},
{
     "name":"nick",
    "age":27,
    "courses":"International relations"
},
{
     "name":"liza",
    "age":25,
    "courses":"management"
}
]



for sub in student:
      if sub["courses"] != "management":
          continue
      print(sub)


for i in student:
    if i["age"]>20:
       break
    print(len(i))



products = [
    {
        "name":"fork",
        "price":14.5,
        "quantity":10
    },
     {
        "name":"apple",
        "price":1.5,
        "quantity":25
    },
     {
        "name":"fork",
        "price":3,
        "quantity":15
    },
     {
        "name":"egg",
        "price":0.5,
        "quantity":50
    },
     {
        "name":"coca_cola",
        "price":3.5,
        "quantity":17
    },
     {
        "name":"borjomi",
        "price":1.8,
        "quantity":12
    }
]

total_price=0
total_product=0

for product in products:
   total_price += product["price"] * product["quantity"]
   total_product += product["quantity"]

avarage_price= total_price / total_product

print(avarage_price)



sales = [{
    "product_a": [5, 8, 12],
    "product_b": [3, 9, 7],
    "product_c": [10, 15, 8],
}]


total_sales = {
    product: sum(sales_data)
    for product, sales_data in sales[0].items()
}

for product, total in total_sales.items():
    print(f'Total sales for {product}: {total}')



total_sum = 0

for sale in sales:
    for product, quantities in sale.items():
        total_sum += sum(quantities)

print(f'Total sold: {total_sum} $')