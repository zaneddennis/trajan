
from textblob.classifiers import NaiveBayesClassifier

def extractFields(transcript):
    print(transcript)

    with open('/home/zane/Documents/tamuhack/trainingData.tsv', 'r') as fp:
        cl = NaiveBayesClassifier(fp, format='tsv')

    return {}

