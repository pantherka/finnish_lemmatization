import re

class Alternation:
    def forward(self, word):
        word = re.sub(r"(?<!s|t|k)k(?=\*)", r"", word, 1)
        word = re.sub(r"kk(?=\*)", r"k", word, 1)

        word = re.sub(r"(?<!p|m)p(?=\*)", r"v", word, 1)
        word = re.sub(r"mp(?=\*)", r"mm", word, 1)
        word = re.sub(r"pp(?=\*)", r"p", word, 1)

        word = re.sub(r"(?<!s|t|l|r)t(?=\*)", r"d", word, 1)
        word = re.sub(r"lt(?=\*)", r"ll", word, 1)
        word = re.sub(r"rt(?=\*)", r"rr", word, 1)
        word = re.sub(r"tt(?=\*)", r"t", word, 1)

        word = re.sub(r"(?<=r|l|h)k(?=e\*)", r"j", word, 1)
        return word

    def backward(self, word):
        word = re.sub(r"(?<!s|t|k)k(?=\*)", r"kk", word, 1)
        word = re.sub(r"(?<!s|t|k|p)(?=\*)", r"k", word, 1) # check -as -is in main code

        word = re.sub(r"(?<!p|m)p(?=\*)", r"pp", word, 1)
        word = re.sub(r"(?<!p|m)v(?=\*)", r"p", word, 1)
        word = re.sub(r"mm(?=\*)", r"mp", word, 1)

        word = re.sub(r"(?<!s|t|l|r)t(?=\*)", r"tt", word, 1)
        word = re.sub(r"(?<!s|t|l|r)d(?=\*)", r"t", word, 1)
        word = re.sub(r"ll(?=\*)", r"lt", word, 1)
        word = re.sub(r"rr(?=\*)", r"rt", word, 1)
  
        word = re.sub(r"(?<=r|l|h)j(?=e\*)", r"k", word, 1)
        return word


if __name__ == "__main__":
    alter = Alternation()
    words = ["aalt*o", "otta*a", "ott*a", "ot*a", "lampp*u", "amp*a", "ast*er"]
    words_back = ["aalt*o", "otta*a", "ott*a", "ot*a", "lampp*u", "amp*a", "ast*er", "all*on"]
    for word in words:
        print(word, alter.forward(word))
    for word in words_back:
        print(word, alter.backward(word))
