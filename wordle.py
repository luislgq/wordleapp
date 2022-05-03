
def main():
    import copy

    # We set the variables. A dictionary of all five letter words. A list of all letters. A dictionary with the value of al the words used to create 5 value dictionaries, one for each letter. 
    five_word_dictionary = ("euros","rapid", "world", "happy")
    letter_list = list()
    for i in five_word_dictionary:
        letter_list+= list(i)
    letter_set = set(letter_list)
    
    # We create an original Value dictonary where we map words to their value, this will give us the initial word
    value_dict={}
    for i, item in enumerate(letter_set):
        y = [letter_list.count(x) for x in letter_set][i]
        value_dict[item]=y
    max_points_word=max(value_dict, key=value_dict.get)

    # We create 5 dictionaries from the value dictionary. Each dictionary represents a letter in a word, dictionary 1 = first letter....
    dict1, dict2,dict3,dict4,dict5 =[copy.copy(value_dict) for _ in range(5)]   
    all_dicts = (dict1, dict2,dict3,dict4,dict5)

    # We create a new value dictionary that will change as the dict1-dict2 change. 
    word_value_dict = {}
    for i in five_word_dictionary:
        x = 0
        value = 0
        for b in all_dicts:
            word_value_dict[i]=value
            x +=1


    # The grey function changes the value of a letter to -1000 in all locations
    def grey(letter):
        for i, item in enumerate (all_dicts):
            all_dicts[i][letter] = -500
            

    # The green  function changes the value of a letter to 1000 on the specified location      
    def green(letter, position):
        all_dicts[position][letter] = 500

    # The yellow function changes the value of a letter to -1000 in the specified location, and add +100 to all other locations
    def yellow(letter, position):
        all_dicts[position][letter] = -1000
        for i, item in enumerate (all_dicts):
            if i != position:
                all_dicts[i][letter] = 100*all_dicts[i][letter]
    
    #This function will update the dictionary and return the newest highest word.  
    def changevalues():

        for i in five_word_dictionary:
            x = 0
            value = 0
            for b in all_dicts:
                key= (i[x])
                value += (all_dicts[x][key])
                word_value_dict[i]=value
                x +=1
        max_points_word=max(word_value_dict, key=word_value_dict.get)
        return  max_points_word
    
        

        


    
