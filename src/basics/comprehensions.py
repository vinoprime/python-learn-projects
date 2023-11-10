print("Hello list comper")


m_list = []

for char in "hello":
    m_list.append(char)

print(m_list)

# Syntax
# list_var = [param for param in iterable]

m_list = [char for char in "hello"]
print(m_list)

m_list = [num**2 for num in range(0,100) if num %2 == 0]
print(m_list)

m_list = {char for char in "hello"}
print(m_list)


simple_dict = { 'a':1, 'b':2}
m_dict = {key:value**2 for key,value in simple_dict.items()}
print(m_dict)
m_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(m_dict)