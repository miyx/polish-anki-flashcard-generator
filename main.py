import random
from wordclasses import *
from grammarclasses import *
from grammarconstants import *
import _pickle as pkl

with open("verbs.pkl",'rb+') as f:
    obj = pkl.load(f)
    f.close()
    verbs = obj['verbs']
    transitive = obj['transitives']
    intransitive = obj['intransitives']
    ditransitive = obj['ditransitive']
    linkings = obj['linkings']
    auxiliaries = obj['auxiliaries']

with open("verbs.json",'rb+') as f:
    obj = pkl.load(f)
    f.close()
    verbs.append(obj['verbs'][1])
    print(verbs[1].variants)

# NOUNS
nouns = list()
nouns.append(Noun("kitten",["kotek","kotka","kotkowi","kotka","kotkiem","kotku","kotku"],SINGULAR,MALE))
nouns.append(Noun("book",["książka","książki","książce","książkę","książką","książce","książko"],SINGULAR,FEMALE))
nouns.append(Noun("egg",["jajko","jajka","jajku","jajko","jajkiem","jajku","jajko"],SINGULAR,NEUTER))
nouns.append(Noun("penises",["penisy","penisów","penisom","penisy","penisami","penisach","penisy"],PLURAL,MALE))
nouns.append(Noun("pussies",["cipki","cipek","cipkom","cipki","cipkami","cipkach","cipki"],PLURAL,FEMALE))

sentences = list()

def sentence1():

    subject = random.choice(nouns)
    v = Rand.randVerb(gender=subject.gender,mult=subject.mult,person=THIRD)
    pronoun = Pronoun.getPronoun(subject.gender,subject.mult,THIRD)
    return pronoun.get(NOM)+" "+verbs[0].get(v['tense'],subject.gender,subject.mult,subject.person,v['verbstate'])+" "+subject.get(NOM)

def sentence2():

    subject = random.choice(nouns)
    v = Rand.randVerb(gender=subject.gender,mult=subject.mult,True)
    pronoun = Pronoun.getPronoun(subject.gender,subject.mult,v['person'],True)
    verb = random.choice(verbs)
    return pronoun.get(NOM)+" "+verb.get(v['tense'],subject.gender,subject.mult,pronoun.person,v['verbstate'])+" "+subject.get(ACC)


def sentence3():
    verb = random.choice(verbs)
    return "Lubię "+verb.infinitive

def sentence4():
    subject = random.choice(nouns)
    verb = random.choice(verbs)
    return subject.nominative+" lubi "+verb.infinitive

#sentences.append(Sentence(sentence1))
sentences.append(Sentence(sentence2))

while True:
    print(random.choice(sentences).get())
    s = input()
    if(s=="x"):
        exit()
