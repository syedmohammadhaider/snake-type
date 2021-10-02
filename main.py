import random, colorama, sys, time, os, signal
from colorama import Fore

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

colorama.init()
last_word = ""
words = [
    "the", "be", "and", "a", "of", "to", "in", "I", "you", "it", "can", "come", "could", "do", "find", "get", "give", "go", "have", "know", "like", "look", "make", "say", "see", "take", "tell", "think", "use", "want", "will", "would", "day", "man", "need", "people", "thing", "time", "way", "year" "he", "him", "me", "she", "that", "them", "these", "they", "this", "us", "we", "what", "who", "all", "any", "first", "good", "her", "his", "just", "more", "my", "new", "one", "other", "our", "some", "their", "two", "your", "about", "also", "as", "here", "how", "no", "not", "now", "out", "so", "then", "there", "up", "very", "well", "when", "which", "at", "by", "for", "from", "into", "on", "to", "with", "because", "but", "if", "or", "than", "the", "of", "to", "and", "a", "in", "is", "it", "you", "that"
]

word = random.choice(words)
next_word = random.choice(words)

def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def prompt(this_word):
    delete_last_lines(5)

    global last_word
    global word
    global next_word

    if not this_word == last_word:
        last_word = this_word
        next_word = random.choice(words)

        print(Fore.CYAN, this_word)
        print(Fore.WHITE)

        delete_last_lines()

        w = input(" > ")

        if w == this_word:
            print(Fore.GREEN, w)
            delete_last_lines(2)
            print(Fore.GREEN, "> %s" % w)
            time.sleep(0.5)
            prompt(next_word)
            prev_words.append(last_word)

        elif w == ".":
            os.kill(os.getppid(), signal.SIGHUP)

        else:
            print(Fore.RED, w)
            delete_last_lines(2)
            print(Fore.RED, "> %s" % w)
            time.sleep(0.5)
            prompt(next_word)
            prev_words.append(last_word)

    else:
        word = random.choice(words)
        prompt(word)

prompt(word)
