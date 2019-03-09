'''
A spam filter based off http://www.paulgraham.com/spam.html
For CS 344 at Calvin College

@student: ajs94
@version March 7, 2019
'''


class Filter:

    def __init__(self, bad_corpus, good_corpus, text):
        self.spam_corpus = self.sentences_to_corpus(bad_corpus)
        self.good_corpus = self.sentences_to_corpus(good_corpus)
        self.combined_corpus = text
        self.corpus_len = 0
        self.corpus_counts = self.hash_words()
        self.corpus_probs = {}

    # change a list of sentences into a list of just words
    def sentences_to_corpus(self, text):
        corpus = []
        for sentence in text:
            for word in sentence:
                corpus.append(word)
        return corpus

    # find the number of occurrences of each word
    def hash_words(self):
        word_dict = {}
        for sentence in self.combined_corpus:
            for word in sentence:
                if word not in word_dict.keys():
                    word_dict[word] = 0
                self.corpus_len += 1
                word_dict[word] += 1
        return word_dict

    def evaluate(self):
        # print(self.spam_corpus)
        # print(self.good_corpus)
        # print(self.corpus_counts)
        #print(self.combined_corpus)

        prob = 0
        for sentence in self.combined_corpus:
            for word in sentence:
                g = 0
                b = 0
                if word in self.good_corpus:
                    g = 2 * self.corpus_counts[word]
                if word in self.spam_corpus:
                    b = self.corpus_counts[word]

                if g + b >= 1:
                    temp = max(0.01,
                            min(0.99, min(1.0, b / len(self.spam_corpus)) /
                            (min(1.0, g / len(self.good_corpus)) +
                            min(1.0, b / len(self.spam_corpus)))))
                    prob += temp
                    self.corpus_probs[word] = temp
        return prob / self.corpus_len


if __name__ == '__main__':

    spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
    sample_mail = [["I", "am", "sam", "sam", "I", "am"], ["I", "do", "not", "like", "green", "eggs", "and", "ham"]]
    # sample_mail = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    # sample_mail = [["Sample", "message", "with", "nothing", "in", "common"], ["Idk", "what", "else", "to", "say"]]

    filter = Filter(spam_corpus, ham_corpus, sample_mail)
    print("Spam Probability: ", filter.evaluate())
    print("Nonzero word probabilities:\n\t" + str(filter.corpus_probs))

    '''
    This approach is Bayesian in that it determines the probabilities of individual words and uses
        them to determine the overall probability that an email is spam ae th conditional probability that
        if words are spam then email is spam.
    '''