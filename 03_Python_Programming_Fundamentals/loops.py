# Quiz on Loops

# Write a for loop that prints out all the elementes between -5 and 5 using the range functions

for i in range(-4, 5):
    print(i)

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']. Make sure you follow Python conventions.

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 
for i in Genres:
    print(i)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in squares:
    print(i)

# Write a while loop to display the values of the Rating of an album playlist stored in the PlayListRatings list. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
r = PlayListRatings[0]
n = len(PlayListRatings)
while(i < n and r >= 6):
    print(r)
    i = i + 1
    r = PlayListRatings[i]

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
n2 = len(squares)
while(i < n2 and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1 
print(new_squares)