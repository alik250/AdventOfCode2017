from Part1 import parse_line

debug = False

def concatenate(list_of_strings):
    string = ""
    for i in list_of_strings:
        string += i
    return string


def _main():
    debug = True

    ## Get our input
    with open("input.txt") as f:

        ## We could keep track of all of the phrases, but we only care about which ones are legitimate.
        # phrases = {}
        legit_phrases = 0

        for line in f.readlines():
            temp_phrase = []
            phrase_is_legit = True

            if debug:
                print("NEW LINE!!!!! ------------- ")

            try:

                for word in parse_line(line):
                    sorted_word = concatenate(sorted(word))

                    if debug:
                        print(f"{word} --- {sorted_word}")

                    ## If {sorted_word} is in the phrase, then it is not legit. We can skip processing it.
                    if sorted_word in temp_phrase:

                        if debug:
                            print("Duplicate word found in phrase! ")

                        raise StopIteration
                    
                    temp_phrase.append(sorted_word)

                legit_phrases += 1

            except StopIteration:
                pass
            
        print(legit_phrases)

if __name__ == "__main__":
    _main()