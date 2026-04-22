# 2. Given a string, count vowels, consonants, and digits.

def string_ (statement_):
    vowel=0
    consonant=0
    digit=0

    for el in statement_:
        if (el in ("aeiou")):
            vowel+=1
            digit+=1
        elif (el is " "):
            digit+=1
        else :
            consonant+=1
            digit+=1
    return vowel,consonant,digit



str = "vishal sharma"
_vowel,consonant_,digit_= string_(str)
print(_vowel,'vowel',consonant_,'consonant_',digit_,'digit_')

            