product = {'p1':'Pen','p2': 'Pencil','p3':'Compass box'}
duplicate_product= product.copy()
print(duplicate_product)
print(product)

name = ('prod4','prod5','prod6')
print(product.fromkeys(name,'Eraser'))

print(product.get('p1'))
print(product.keys())
print(product.values())
print(product.pop('p2'))
print(product)

print(product.setdefault('ppp','Triangle'))
print(product)

print(product.popitem())

print(product.update({'p9':'Slate','p8':'Rular'}))
print(product)

product.update({'p9':'Notebook'})
product.update({'p10':'Notebook'})

print(product)
product.clear()
print(product)