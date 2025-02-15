# Quiz on Functions

# Come up with a function that divides the first input by the second input:
def function(a, b):
    return (a / b)
result = function(12, 4)
print(result)

# Use the function "con" for the following question.
def con(a, b):
    return(a + b)

# Can the "con" function we defined before be used to add two integers or strings?
print(con(1, 2)) # Yes
print(con("StringA", "StringB")) # Yes

# Can the "con" function we defined before be used to concatenate lists or tuples?
print(con([1, 2], [3, 4])) # Yes
print(con((1, "A"), (2, "B"))) # Yes

# Write a function code to find total count of word "little" in the given string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def freq(string, passedKey):
    words = []
    words = string.split()
    n = 0

    for key in words:
        if (key == passedKey):
            n = n + 1
    print(f"Total Count: {passedKey} : {n}")

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")

# Using dictionary
def freqDic(string, passedKey):
    words = []
    words = string.split()
    Dict = {}
    for key in words:
        if (key == passedKey):
            Dict[key] = words.count(key)
    print("Total count:", Dict)

freqDic("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")