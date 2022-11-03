
def find_index(a,word:str):
    index = -1

    for i in a:
        index += 1
        if i == word:
            break

    return index



a = ["'Annie'", "'Bernard'", "'Daniel'", "'Jack'", "'Noel'","'Paul'",
"'Stela'", "'Tom'"]

word = "'Paul'"

print(find_index(a,word))