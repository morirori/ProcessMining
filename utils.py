from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import path_similarity


def import_data(path):
    with open(path, 'r') as f:
        return f.read()


def tag_data(data):
    split_data = data.split(".")
    return [pos_tag(word_tokenize(data.lower())) for data in split_data]


def extract_important_words(sentences):
    parsed_sentences = []
    for sentence in sentences:
        parsed_sentance = []
        for word in sentence:
            if word[0] == "and":
                parsed_sentences.append(parsed_sentance)
                parsed_sentance = [{"word": word[0], "tag": word[1]}]

            elif __check_if_word_tag_is_not_excluded(word[1]) or \
                    __check_if_word_is_not_exception(word[0]):

                parsed_sentance.append({"word": word[0], "tag": word[1]})

        parsed_sentences.append(parsed_sentance)
    return parsed_sentences


def __check_if_word_tag_is_not_excluded(tag):
    included_tags = ("CC", "NN", "NNP", "NNPS", "VB", "VBD", "VBG", "VBP", "VBZ")
    return True if tag in included_tags else False


def __check_if_word_is_not_exception(examined_word):
    exceptions = {"IN": ("if",),
                  "RB": ("otherwise",),
                  "JJ": ("acceptable",)}

    # TODO implement synonyms( path_similarity or synset)

    for words in exceptions.values():
        for word in words:
            if examined_word.find(word) != -1:
                return True
    return False


def extract_simple_model(sentences):
    model = ""
    # TODO add further analysis
    for sentence_id, sentence in enumerate(sentences):
        print(sentence)
        if sentence_id == 0:
            model += __analyze_first_sentance(sentence)
        else:
            model += __analyze_sentence(sentence)
    return model


def __analyze_sentence(sentence):
    tags = {"verbs": ("VB", "VBD", "VBG", "VBP", "VBZ"),
            "nouns": ("NN", "NNP")}

    to_return = ""
    verb_is_set = False
    for word_idx, word in enumerate(sentence):
        if word["word"] == "and":
            to_return += "-> "

        elif word["word"] == "if":
            to_return += "/\\ "
        elif word["tag"] in tags["verbs"]:
            to_return += word["word"] + " "
            verb_is_set = True

        elif word["tag"] in tags["nouns"] and verb_is_set:
            to_return += word["word"] + " "
    return to_return


def __analyze_first_sentance(sentence):
    tags = {"verbs": ("VB", "VBD", "VBG", "VBP", "VBZ"),
            "nouns": ("NN", "NNP")}

    to_return = ""
    verb_is_set = False
    for word_idx, word in enumerate(sentence):
        if word["tag"] in tags["verbs"]:
            to_return += word["word"] + " "
            verb_is_set = True

        elif word["tag"] in tags["nouns"] and verb_is_set:
            to_return += word["word"] + " "
    print(to_return)
    return to_return
