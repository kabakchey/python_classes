epmty_dict = {}

# initialization
dict_vocab_en_es = {'world': 'mundo', 'language': 'idioma', 'See you later': 'Hasta la vista'}
dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
dict_planets_2 = {'earth': (345778, 894202), 'mars': (47789, 898902), 'venus': (4679339, 238000)}
print(dict_planets)

# real examples
person_1 = {'name':'Richard Feynman',
            'age': 99,
            'birth_place': 'USA',
            'birth_date': "1918-01-01",
            'awards':['Nobel Prize in Phisics', 'USA Science Medal']}

person_2 = {'name':'Albert Einstein',
            'age': 138,
            'birth_place': 'Germany',
            'birth_date': "1879-03-14",
            'awards':['Nobel Prize in Physics', 'Planck Medal']}

person_2 = {'name':'Nicola Tesla',
            'age': 161,
            'birth_place': 'Croatia',
            'birth_date': "1856-07-10",
            'awards':['Edison Medal']}

physicits = [person_1, person_2]

# add new key-value pairs
person_1['hobby'] = "painting"
person_2['hobby'] = "violin"
person_3['hobby'] = "pigeons"
person_3['hobby'] = "electricity" # second assignment overrides the 1st one

person_3['wiki_url'] = "https://en.wikipedia.org/wiki/Nikola_Tesla"

print(person_1)
print(person_2)
print(person_3)

del person_1['age']
print(person_1)

# read value by key
print(person_3['wiki_url'])
print(person_2['wiki_url'])         # error
print(person_1['wiki_url'])         # error with default

# check existance
if 'wiki' in person_3:
    print(person_3['wiki_url'])
else:
    print("key 'wiki_url' is missing")

# get with default
employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}

employees = [employee_1, employee_2, employee_3, employee_4]

print(person_1.get('bonus', 0))
print(person_2.get('bonus', 100))
# update bonus and salary

# printing
for key in person_1:
    print (key)

for key in dict:
    print (key, "->", person_1[key])

for key, value in dict.items():
    print ("%s -> %s" % (key, value))

for key in sorted(person_1):
    print (key, "->",  dict_planets[key])

for key in sorted(dict_planets, key=dict_planets.get):# reverse=True):
    print (key, "->",  dict_planets[key])

# comprehension
symbols = {chr(code): 0 for code in range(ord("a"), ord("z"))}

# practice
# - letters frequency
# - sort by keys/value
# - top 5 letters

# idiomatic python for incrementing values in dicts 
if key in dict:
    dict[key] += 1
else:
    dict[key] = 1

<==>

dict["key"]= dict.get("key", 0) + 1


# advanced
######################################################
def print_top_n_words(filename, top_n):
    f = open(filename)
    words_list = f.read().split()
    print (len(words_list))
    words_freq = {}
    for word in words_list:
        if word[:1].isupper():
            words_freq[word] = words_freq.get(word, 0) + 1

    print (len(words_freq))
    for key in sorted(words_freq, reverse=True, key=words_freq.get)[:top_n]:
        print ("%-20s -> %d" % (key, words_freq[key]))
    f.close()


######################################################
def print_top_ngrams(filename):
    import string

    f = open(filename)
    words_list = f.read().split()
    print (len(words_list))
    words_freq = {}
    symb_dict = {}
    _ngram_freq = {}
    words = []
    limit = 4

    # skip_words = ["the", "to", "in", "on", "of", "by", "in", "from", "with", "no"
    # "he", "she", "and", "it", "was", "a", "said", "be", "would", "have", "had", "been", 
    # "were", "i", "as", "that", "this", "are", "at", "do", "not", "is", "her", "if", "i"]

    skip_words = [ 'в', 'время', 'же', 'бы', 'было', 'ни', 'то', 'более', 'всё', 'и',
     'в', 'же', 'но', 'то', 'до', 'не', 'пор', 'сих', 'ж', 'ну', 'так', 'что',
     'всё', 'это', 'к', 'а', 'вместе', 'с', 'тем', 'и', 'не', 'он', 'сам', 'до',
     'же', 'что', 'он', '']

    for word in words_list:
        word = word.lower().strip(",. !?:'\"-")
        if word not in skip_words:
            if len(words) == limit:
                words.pop(0)
            words.append(word)
            _ngram = tuple(sorted(words))
            _ngram_freq[_ngram] = _ngram_freq.get(_ngram, 0) + 1

    for key in sorted(_ngram_freq, reverse=True, key=_ngram_freq.get)[:20]:
        print("%s: %d" % (key, _ngram_freq[key]))

