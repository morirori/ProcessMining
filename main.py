import nltk
import os

from file_utils import import_data, tag_data, extract_important_words, extract_simple_model

FILE = "model2"


def prepare_tools():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')


if __name__ == "__main__":
    prepare_tools()
    path = "{}/data/{}.txt".format(os.curdir, FILE)
    data = import_data(path)
    tagged_data = tag_data(data)
    extracted_data = extract_important_words(tagged_data)
    model = extract_simple_model(extracted_data)
    print(model)