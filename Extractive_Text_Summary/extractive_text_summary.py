from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

#print(set(stopwords.words("english")))

def extractive_text_summary(text : str, num_sentences : int):
    # preprocessing
    # creates sentence_list, word_list (with punctuation), and token_list
    sentence_list = []
    for sentence in text.split("."):
        if len(sentence) > 0:
            if sentence[0] == " ":
                sentence = sentence[1:]
        sentence_list.append(sentence + ".")
    if "." in sentence_list: ### this is extremely inelegant
        sentence_list.remove(".")
    print("sentence_list: " + str(sentence_list)) # check #
    word_list = word_tokenize(text) # with punctuation
    print("word_list: " + str(word_list)) # check
    punctuation_list = []
    for item in string.punctuation:
        punctuation_list.append(item)
    remove_list = stopwords.words("english") + punctuation_list
    token_list = []
    for word in word_list:
        if not(word in remove_list):
            token_list.append(word)
    print("token_list: " + str(token_list)) # check #
    # Calculate weighted frequencies of each sentence
    lowercase_token_list = [token.lower() for token in token_list]
    print("lowercase_token_list: " + str(lowercase_token_list)) # check #
    token_frequencies = Counter(lowercase_token_list)
    print("token_frequencies: " + str(token_frequencies)) # check #
    avg_sentence_scores = {}
    for sentence_number, sentence in zip(range(1, len(sentence_list)+1), sentence_list):
        # for each sentence, compute sentence_tokens = no. tokens in sentence
        # for each word, find frequencies of each token, and sum into total_score
        # compute total_score/sentence_tokens
        # store results in avg_sentence_scores, with sentence numbers as keys
        sentence_tokens = []
        words = sentence[:len(sentence)-1].split(" ")
        for word in words:
            if not(word in remove_list):
                sentence_tokens.append(word)
        print("sentence_tokens, s" + str(sentence_number) + ": " + str(sentence_tokens)) # check #
        total_score = 0
        for token in sentence_tokens:
            total_score += token_frequencies[token.lower()]
        print("total_score, s" + str(sentence_number) + ": " + str(total_score))
        if len(sentence_tokens) == 0:
            avg_sentence_scores[sentence_number] = 0
        else:
            avg_sentence_scores[sentence_number] = total_score/len(sentence_tokens)
    print("avg_sentence_scores: " + str(avg_sentence_scores)) # check #
    # Produce output
    ranked_sentence_nos = sorted(avg_sentence_scores.items(), key=lambda item: item[1], reverse=True)
    ranked_sentence_nos = [i[0] for i in ranked_sentence_nos]
    print("ranked_sentence_nos: " + str(ranked_sentence_nos)) # check #
    summary_sentence_nos = ranked_sentence_nos[0:(num_sentences)]
    print("summary_sentence_nos: " + str(summary_sentence_nos)) # check #
    summary_sentences = []
    for sentence_number, sentence in zip(range(1, len(sentence_list)+1), sentence_list):
        if sentence_number in summary_sentence_nos:
            summary_sentences.append(sentence)
    return " ".join(summary_sentences)

print(extractive_text_summary("Hello. Blue cow. Blue as the water.", 2))