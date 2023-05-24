from collections import defaultdict

if __name__ == "__main__":
    N = int(input())
    result = 0
    words = []
    alphabets = defaultdict(int)
    for _ in range(N):
        word = input()
        words.append(word)

    words.sort(key=lambda x: -len(x))
    for i in range(N):
        for j in range(len(words[i])):
            alphabets[words[i][j]] += pow(10, len(words[i]) - j - 1)

    alphabet = []
    for k, v in alphabets.items():
        alphabet.append([k, v])

    alphabet.sort(key=lambda x: -x[1])
    for i in range(len(alphabet)):
        result += alphabet[i][1] * (9 - i)

    print(result)
