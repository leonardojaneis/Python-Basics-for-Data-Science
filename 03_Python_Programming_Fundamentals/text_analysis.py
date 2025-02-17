# Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large dataset of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks: 

# Task 1. String in lower case: You want to Pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.

# Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

# Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in the customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

# Part-A 
# Step-1 Define a string. Use a variable and store the string: "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

string_text = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# For achieving the tasks mentioned in the scenario, We need to create a class with 3 different methods.
# Step-2 Define the class and its attributes
# Step-3 Implement a code to Format the text in Lowercase:
#   1. Inside the constructor,we will convert the text argument to lowercase using the lower() method.
#   2. Then, will Remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the replace() method.
#   3. At last, we will Assign the formatted text to a new attribute called fmtText.
# Step-4 Implement a code to count the Frequency of all unique words
# In this step, we will Implement the freqAll() method with the below parameters:
#   1. Split the fmtText attribute into individual words using the split() method.
#   2. Create an empty dictionary to store the word frequency.
#   3. Iterate over the list of words and update the frequency dictionary accordingly.
#   4. Use count method for counting the occurence
#   5. Return the frequency dictionary.
# Step-5 Implement a code to count the Frequency of a specific word:
# *In step-5, we have to Implement the freqOf(word) method that takes a word argument:
#   1. Create method and pass the word that need to be found
#   2. Get the freqAll method for look for count and check if that word is in the list.
#   3. Return the count.

class TextAnalyser(object):
    
    def __init__(self, text):
        new_text = text.replace('.', '').replace('!', '').replace(',', '').replace('?', '')
        new_text = text.lower()
        self.fmtText = new_text
       
   
    def freqAll(self):
        individual_words = self.fmtText.split(' ')
        freq_words = {}

        for word in set(individual_words):
            freq_words[word] = individual_words.count(word)
        return freq_words
    
    def freqOf(self, word):
        freq_word = self.freqAll()

        if word in freq_word:
            return freq_word[word]
        else:
            return 0

# Part_B
# In Part B, we will be calling the functions created in Part A, allowing the functions to execute and generate output.
# Step-1 Create an instance of TextAnalyzer Class.
# Instantiate the TextAnalyzer class by passing the given string as an argument
text_analyser = TextAnalyser(string_text)

# Step-2 Call the function that converts the data into lowercase
print(text_analyser.fmtText)

# Step-3 Call the function that counts the frequency of all unique words from the data.
freq_words = text_analyser.freqAll()
print(freq_words)

# Step-4 Call the function that counts the frequency of specific word.
# Here, we will call the function that counts the frequency of the word "lorem" 
freq_word = text_analyser.freqOf("lorem")
print(f"The word lorem appears {freq_word} times.")
