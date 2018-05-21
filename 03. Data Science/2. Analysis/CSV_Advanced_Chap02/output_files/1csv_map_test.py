header_list= ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']

result = map(str,header_list)
print(result)
result2 = ','.join(result)
print(result2)
result3 = ','.join(header_list)
print(result3)
