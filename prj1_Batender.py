questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

import pandas as pd
import numpy as np
data = pd.DataFrame(list(questions.items()), columns=['taste','question'])
data.head()

tasteChoice=pd.DataFrame(ingredients)
tasteChoice.head()

while(True):
    while (True):
        print("Please choice taste you like: (strong, salty, bitter, sweet or fruity)")
        inputTaste = input().lower()
        if (inputTaste not in data.taste.tolist()):
            print("So sorry that Don't have this taste. Please choice taste again :D ")
        else: break
    print('Question: ', data.question[data.taste==inputTaste].to_string(index=False))
    
    print('Press "Y" if Yes and "N" if No: ')
    inputChoice = input().upper()
    if (inputChoice=='Y'):
        print(np.random.choice(tasteChoice[inputTaste].tolist()))
        print('Thank you and nice to enjoy!')
        break
    else: 
        print('Oops, choice again!')
