import requests
from bs4 import BeautifulSoup
import operator

# coding=utf8

"""
This function destroys the punctuations and returns an array filled with words without punctuations
"""


def punctuation_Destroyer(kelime_Dizisi):
    sembolsuzkelimeler = []
    semboller = "1234567890←!'^%&/()=?_-*|\}:][{½$#£\"><@.,;’א" + chr(775)
    for kelime in kelime_Dizisi:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")
        if len(kelime) > 0:
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler


"""
 This function contains an empty dictionary so that it roams in word list and counts the words.
 It contains words as a key and their amounts as a value.
"""


def dictionary_Converter(words_list):
    kelimesayar_sozluk = {}
    for kelime in words_list:
        if kelime in kelimesayar_sozluk:
            kelimesayar_sozluk[kelime] += 1
        else:
            kelimesayar_sozluk[kelime] = 1
    return kelimesayar_sozluk


"""
 These two functions below defined as a void.
 Thanks to stopwords array this for loops roam in (splitted) list of words and delete the stopwords inside.
"""


def stop_Word_remover_1(list_of_words_1):
    for i in stopwords:
        for j in list_of_words_1:
            if i == j:
                list_of_words_1.remove(i)


def stop_Word_remover_2(list_of_words_2):
    for i in stopwords:
        for j in list_of_words_2:
            if i == j:
                list_of_words_2.remove(i)


###

stopwords = ["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are",
             "aren", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between",
             "both", "but", "by", "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does",
             "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few", "for", "from",
             "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having",
             "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is",
             "isn", "isn't", "it", "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't",
             "more", "most", "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now",
             "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over",
             "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've", "shouldn",
             "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them",
             "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under",
             "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what",
             "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn",
             "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",
             "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've",
             "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're",
             "they've", "we'd", "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's",
             "would", "able", "abst", "accordance", "according", "accordingly", "across", "act", "actually",
             "added", "adj", "affected", "affecting", "affects", "afterwards", "ah", "almost", "alone", "along",
             "already", "also", "although", "always", "among", "amongst", "announce", "another", "anybody",
             "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently",
             "approximately", "arent", "arise", "around", "aside", "ask", "asking", "auth", "available", "away",
             "awfully", "b", "back", "became", "become", "becomes", "becoming", "beforehand", "begin",
             "beginning", "beginnings", "begins", "behind", "believe", "beside", "besides", "beyond", "biol",
             "brief", "briefly", "c", "ca", "came", "cannot", "can't", "cause", "causes", "certain", "certainly",
             "co", "com", "come", "comes", "contain", "containing", "contains", "couldnt", "date", "different",
             "done", "downwards", "due", "e", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else",
             "elsewhere", "end", "ending", "enough", "especially", "et", "etc", "even", "ever", "every",
             "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "ff", "fifth",
             "first", "five", "fix", "followed", "following", "follows", "former", "formerly", "forth", "found",
             "four", "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving",
             "go", "goes", "gone", "got", "gotten", "h", "happens", "hardly", "hed", "hence", "hereafter",
             "hereby", "herein", "heres", "hereupon", "hes", "hi", "hid", "hither", "home", "howbeit", "however",
             "hundred", "id", "ie", "im", "immediate", "immediately", "importance", "important", "inc",
             "indeed", "index", "information", "instead", "invention", "inward", "itd", "it'll", "j", "k",
             "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "l", "largely", "last", "lately",
             "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely",
             "line", "little", "'ll", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes",
             "many", "may", "maybe", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might",
             "million", "miss", "ml", "moreover", "mostly", "mr", "mrs", "much", "mug", "must", "n", "na",
             "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs",
             "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "nobody", "non", "none",
             "nonetheless", "noone", "normally", "nos", "noted", "nothing", "nowhere", "obtain", "obtained",
             "obviously", "often", "oh", "ok", "okay", "old", "omitted", "one", "ones", "onto", "ord", "others",
             "otherwise", "outside", "overall", "owing", "p", "page", "pages", "part", "particular",
             "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible",
             "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily",
             "probably", "promptly", "proud", "provides", "put", "q", "que", "quickly", "quite", "qv", "r",
             "ran", "rather", "rd", "readily", "really", "recent", "recently", "ref", "refs", "regarding",
             "regardless", "regards", "related", "relatively", "research", "respectively", "resulted",
             "resulting", "results", "right", "run", "said", "saw", "say", "saying", "says", "sec", "section",
             "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven",
             "several", "shall", "shed", "shes", "show", "showed", "shown", "showns", "shows", "significant",
             "significantly", "similar", "similarly", "since", "six", "slightly", "somebody", "somehow",
             "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon",
             "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub",
             "substantially", "successfully", "sufficiently", "suggest", "sup", "sure", "take", "taken",
             "taking", "tell", "tends", "th", "thank", "thanks", "thanx", "thats", "that've", "thence",
             "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere",
             "theres", "thereto", "thereupon", "there've", "theyd", "theyre", "think", "thou", "though",
             "thoughh", "thousand", "throug", "throughout", "thru", "thus", "til", "tip", "together", "took",
             "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u", "un",
             "unfortunately", "unless", "unlike", "unlikely", "unto", "upon", "ups", "us", "use", "used",
             "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve",
             "via", "viz", "vol", "vols", "vs", "w", "want", "wants", "wasnt", "way", "wed", "welcome", "went",
             "werent", "whatever", "what'll", "whats", "whence", "whenever", "whereafter", "whereas",
             "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "whim", "whither", "whod",
             "whoever", "whole", "who'll", "whomever", "whos", "whose", "widely", "willing", "wish", "within",
             "without", "wont", "words", "world", "wouldnt", "www", "x", "yes", "yet", "youd", "youre", "z",
             "zero", "a's", "ain't", "allow", "allows", "apart", "appear", "appreciate", "appropriate",
             "associated", "best", "better", "c'mon", "c's", "cant", "changes", "clearly", "concerning",
             "consequently", "consider", "considering", "corresponding", "course", "currently",
             "definitely", "described", "despite", "entirely", "exactly", "example", "going", "greetings",
             "hello", "help", "hopefully", "ignored", "inasmuch", "indicate", "indicated", "indicates",
             "inner", "insofar", "it'd", "keep", "keeps", "novel", "presumably", "reasonably", "second",
             "secondly", "sensible", "serious", "seriously", "sure", "t's", "third", "thorough", "thoroughly",
             "three", "well", "wonder", " ", "  ", "   ", "    ", "     ", "      ", "       ", "        "]

""""
Experimented On:

-Non-Programmer%27s_Tutorial_for_Python_2.6
-Non-Programmer%27s_Tutorial_for_Python_3
-Knowing_Knoppix
-C Programming
-C Sharp Programming

I had a problem on "PYTHON 3" website i tried to solve it for days but i could not understand
where the problem was. The problem was counting words was not completely
correct on the website. I tried couple of different sollutions but it did
not worked well so I gave up because deadline was getting close.
Except the website  i told, on another websites program works well.

"""
"""I checked using try-except codes to check if there is an error"""
try:
    book_number = int(input("Please enter number of books (1 or 2):"))
    if book_number == 1:
        """Converts the book name to URL (printable wikibooks)"""
        book_name_1 = input("Please enter the name of book :")
        book_name_1_url = "https://en.wikibooks.org/wiki/" + book_name_1 + "/Print_version"

        print("Please Wait (That may take some time)...")

        r_1 = requests.get(book_name_1_url)
        website_code_1 = BeautifulSoup(r_1.content, "html.parser")
        datas_1 = website_code_1.find_all("html")

        text_1 = open("textfile_1.txt", "w", encoding="utf-8")
        """Writes the datas that we dig to txt"""
        for i in datas_1:
            text_1.write(str(i.text))
        text_1.close()

        """Opens the txt file to read"""
        text_1_reader = open("textfile_1.txt", "r", encoding="utf-8")

        list_of_words_1 = text_1_reader.read()
        list_of_words_1 = list_of_words_1.split()
        text_1_reader.close()

        """Make the letters lowecase int list of words"""
        for i in range(len(list_of_words_1)):
            list_of_words_1[i] = list_of_words_1[i].lower()

        stop_Word_remover_1(list_of_words_1)

        list_of_words_1 = punctuation_Destroyer(list_of_words_1)

        number_of_words_1 = dictionary_Converter(list_of_words_1)
        try:
            number_of_printed = int(input("Please enter how many words you would like to print:"))
        except ValueError:
            number_of_printed = 20

        sorted_1 = sorted(number_of_words_1.items(), key=operator.itemgetter(1), reverse=True)
        sorted_1_new = {key: value for (key, value) in sorted_1}
        a = 0
        print("BOOK:", book_name_1)
        print("{0:4s}{1:15s}{2:5}".format("NO", "WORD", "FREQ"))
        for i in sorted_1_new.keys():
            percentage = (sorted_1_new[i] / len(list_of_words_1)) * 100
            print("{0:3d} {1:15s} {2:^4d} %{3:3f}".format(a + 1, i, sorted_1_new[i], percentage))
            a = a + 1
            if (a == number_of_printed):
                break

    elif book_number == 2:
        """Converts the book name to URL (printable wikibooks)"""
        book_name_1 = input("Please enter the name of book 1:")
        book_name_1_url = "https://en.wikibooks.org/wiki/" + book_name_1 + "/Print_version"

        """Converts the book name to URL (printable wikibooks)"""
        book_name_2 = input("Please enter the name of book 2:")
        book_name_2_url = "https://en.wikibooks.org/wiki/" + book_name_2 + "/Print_version"

        print("Please Wait (That may take some time)...")
        r_1 = requests.get(book_name_1_url)
        r_2 = requests.get(book_name_2_url)

        website_code_1 = BeautifulSoup(r_1.content, "html.parser")
        website_code_2 = BeautifulSoup(r_2.content, "html.parser")

        datas_1 = website_code_1.find_all("html")
        datas_2 = website_code_2.find_all("html")

        text_1 = open("textfile_1.txt", "w", encoding="utf-8")
        text_2 = open("textfile_2.txt", "w", encoding="utf-8")

        """Writes the datas that we dig to txt"""
        for i in datas_1:
            text_1.write(str(i.text))
        text_1.close()

        """Writes the datas that we dig to txt"""
        for i in datas_2:
            text_2.write(str(i.text))
        text_2.close()

        text_1_reader = open("textfile_1.txt", "r", encoding="utf-8")
        text_2_reader = open("textfile_2.txt", "r", encoding="utf-8")

        list_of_words_1 = text_1_reader.read()
        list_of_words_1 = list_of_words_1.split()
        text_1_reader.close()

        list_of_words_2 = text_2_reader.read()
        list_of_words_2 = list_of_words_2.split()
        text_2_reader.close()

        for i in range(len(list_of_words_1)):
            list_of_words_1[i] = list_of_words_1[i].lower()
        stop_Word_remover_1(list_of_words_1)

        for i in range(len(list_of_words_2)):
            list_of_words_2[i] = list_of_words_2[i].lower()
        stop_Word_remover_2(list_of_words_2)

        stop_Word_remover_1(list_of_words_1)
        stop_Word_remover_2(list_of_words_2)

        list_of_words_1 = punctuation_Destroyer(list_of_words_1)
        list_of_words_2 = punctuation_Destroyer(list_of_words_2)

        number_of_words_1 = dictionary_Converter(list_of_words_1)
        number_of_words_2 = dictionary_Converter(list_of_words_2)

        try:
            number_of_printed = int(input("Please enter how many words you would like to print:"))
        except ValueError:
            number_of_printed = 20
        """To sort the dictionary according to values i used two code blocks below"""
        sorted_1 = sorted(number_of_words_1.items(), key=operator.itemgetter(1), reverse=True)
        sorted_1_new = {key: value for (key, value) in sorted_1}
        a = 0
        print("BOOK 1:", book_name_1)
        print("{0:4s}{1:15s}{2:5}".format("NO", "WORD", "FREQ_1"))
        for i in sorted_1_new.keys():
            percentage = (sorted_1_new[i] / len(list_of_words_1)) * 100
            print("{0:3d} {1:15s} {2:^4d} %{3:2f}".format(a + 1, i, sorted_1_new[i], percentage))
            a = a + 1
            if (a == number_of_printed):
                break

        print("****************************************************************************************************")
        """To sort the dictionary according to values i used two code blocks below"""
        sorted_2 = sorted(number_of_words_2.items(), key=operator.itemgetter(1), reverse=True)
        sorted_2_new = {key: value for (key, value) in sorted_2}
        a = 0
        print("BOOK 2:", book_name_2)
        print("{0:4s}{1:15s}{2:5}".format("NO", "WORD", "FREQ_2"))
        for i in sorted_2_new.keys():
            percentage = (sorted_2_new[i] / len(list_of_words_2)) * 100
            print("{0:3d} {1:15s} {2:^4d} %{3:2f}".format(a + 1, i, sorted_2_new[i], percentage))
            a = a + 1
            if (a == number_of_printed):
                break

        print("*****************************************************************************************************")

        keys_list_1 = list(sorted_1_new)
        keys_list_2 = list(sorted_2_new)

        a = 0
        print("BOOK 1 DISTINCT WORDS:", book_name_1)
        print("{0:4s}{1:15s}{2:5}".format("NO", "WORD", "FREQ"))
        for i in keys_list_1:
            if not i in keys_list_2:
                print("{0:3d} {1:15s} {2:4d}".format(a + 1, i, sorted_1_new[i]))
                a = a + 1
            if (a == number_of_printed):
                break

        print("*****************************************************************************************************")
        a = 0
        print("BOOK 2 DISTINCT WORDS:", book_name_2)
        print("{0:4s}{1:15s}{2:5}".format("NO", "WORD", "FREQ"))
        for i in keys_list_2:
            if not i in keys_list_1:
                print("{0:3d} {1:15s} {2:4d}".format(a + 1, i, sorted_2_new[i]))
                a = a + 1
            if (a == number_of_printed):
                break
        print("*****************************************************************************************************")
        a = 0
        sozlukk = {}

        print("COMMON WORDS:")
        print("{0:4s}{1:16s}{2:5} {3:5} {4}".format("NO", "WORD", "FREQ_1", "FREQ_2", "FREQ_SUM"))
        for i in keys_list_1:
            for j in keys_list_2:
                if i == j:
                    sozlukk[i] = sorted_1_new[i] + sorted_2_new[i]

        """To sort the dictionary according to values i used two code blocks below"""
        new_sozlukk = sorted(sozlukk.items(), key=operator.itemgetter(1), reverse=True)
        new_sozlukk = {key: value for (key, value) in new_sozlukk}
        for i in new_sozlukk.keys():
            print("{0:3} {1:16}{2:5}{3:5}  {4:4}".format(a + 1, i, sorted_1_new[i], sorted_2_new[i], sozlukk[i]))
            a = a + 1
            if a == number_of_printed:
                break

    else:
        print("You should enter 1 or 2")

except ValueError:
    print("Invalid Input")
