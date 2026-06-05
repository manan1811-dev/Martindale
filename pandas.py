import re

my_list = ["hello        world", "python       code", "chat        gpt"]

result = list(map(lambda x: re.sub(r' {2,}', ' ', x), my_list))

print(result)