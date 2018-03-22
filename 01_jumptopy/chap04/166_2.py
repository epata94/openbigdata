# f = open("foo.txt",'w',encoding='UTF8')
# f.write("Life is too short, you need python")
with open("foo.txt",'w',encoding='UTF8') as f:
    f.write("인생은 너무 짧네요. 그래서 당신은 파이썬이 필요해요!")
