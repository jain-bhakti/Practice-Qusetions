ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
freqr = {}
freqm = {}
flag = False

for i in ransomNote:
    if i not in freqr:
        freqr[i] = 1
    else:
        freqr[i] += 1

for i in magazine:
    if i not in freqm:
        freqm[i] = 1
    else:
        freqm[i] += 1

for i in ransomNote:
    if i in magazine:
        if freqr[i] <= freqm[i]:
            flag = True
        else:
            flag = False
            break
print(flag)
print(freqm)
print(freqr)