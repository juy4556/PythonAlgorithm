if __name__ == "__main__":
    cosonants = set('aeiou')

    while True:
        st = input().rstrip()
        consonant_count = 0
        vowel_count = 0
        cons_check = 0
        acceptable = 1
        before = ''
        if st == "end":
            break

        for s in st:
            if before == s:
                if s == 'e' or s == 'o':
                    pass
                else:
                    acceptable = 0
                    break

            if s in cosonants:
                consonant_count += 1
                vowel_count = 0
                cons_check = 1
            else:
                vowel_count += 1
                consonant_count = 0

            if consonant_count >= 3 or vowel_count >= 3:
                acceptable = 0
                break

            before = s
        if not cons_check:
            acceptable = 0

        if acceptable:
            print("<{0}> is acceptable.".format(st))
        else:
            print("<{0}> is not acceptable.".format(st))
