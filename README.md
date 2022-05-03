# wordleapp


This code is the first step before creating a flutter app that helps you play wordle.
Currently I have created the python code that will run the logic. 
What is missing is an interface for the user to input which letters are grey/yellow/green


The functioning is simple, we give a value to letters, depending on how often they appear in all five letter words.
If a letter appears 1000 times, its value its a 1000.
Thus the word or words with the higest value will have the most common letters on a five letter word
Furthermore we add a function to change the value of letters depending on its position, first, second, third... in the word.
This way we can increase and reduce the value of letters depending if that letter returns grey, yellow or green.  
Whenever we get a grey letter, we will greatly reduce the value of that letter in all positions.
If it returns blue we will highly increase the value of that letter in that position.
If it returns yellow we will highly decrease the value of that eltter in that position while increasing its value everywhere else. 

Improvements to do:
    - This can be done much quicker if we directly create a dictionary file with all words and their values, instead of always creating it at the beginning from the five word dictionary.
    - The grey function could instead remove from the word value dictionary all words that include the grey letter (only if that letter has not been added to green) This could be done quickly by having 26 dictionaries, one for each letter.
       so when one letter is grey, we remove all values from that dictionary from the word value dictionary
    - Currently words that have duplicated letters, and one is green/yellow and another is grey can lead to problems. 
