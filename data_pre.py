import os
from os import path
import glob

# Link
def dirwalk(dir, bag, wildcards):
    bag.extend(glob.glob(path.join(dir, wildcards)))
    for f in os.listdir(dir):
        fullpath = os.path.join(dir, f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            dirwalk(fullpath, bag, wildcards)

files = []
dirwalk("./", files, "*.utt")

#Xu li
label_li = []
sentence_li = []
person_li = []
#Bo trg hop "%"
li_1 = ['ba','qy', 'x', 't1', 't3', '^t', '^c', 'oo', 'o', 'qw', 'qo', 'qrr', 'qr', 'qh', '^d',
'^g', 'ad', 'co', 'cc', 'fp', 'fc', 'fx', 'fe', 'fo', 'ft', 'fw', 'fa', 'aap', 'aa', 'am', 
'arp', 'ar', '^h', 'br^m', 'br', 'bk', '^m', '^2', 'bf', 'by', 'bd', 'bc', 'bh', 'b', 'nn^e',
'ny^e', 'sd^e', 'sv^e', 'sd', 'sv', 'ny', 'nn', 'na', 'ng', 'no', '^e', 'nd', '^q', 'h', '+', '"']
li_2 = ['appreciation','yes-no-question', 'non-verbal', 'seft-talk', '3rd-party-talk', 'task-management', 'comunication-management', 'open-option', 'other', 'wh-question', 'open-question', 
'or-clause', 'or-question', 'rhetorical question', 'declarative-question', 'tag-question', 'action-directive', 'offer', 'commit', 'conventional-opening', 'conventional-closing', 'explicit-performative', 
'exclamation', 'other-forward-function', 'thanking', "you're-welcome", 'apology', 'accept-part', 'accept', 'maybe', 'reject-part', 'reject', 
'hold before answer', 'signal-understanding', 'signal-non-understanding', 'acknowledge-answer', 'repeat-phrase', 'completion', 'summarize', 'sympathy', 'downplayer', 'correct-misspeaking', 
'acknowledge', 'acknowledge', 'no plus expasion', 'yes plus expasion', 'statement expanding y/n answer', 'statement expanding y/n answer', 'statement-non-opinion', 'statement-opinion', 'yes answers', 'no answers', 
'affirmative non-yes answers', 'negative non-no answers', 'other answers', 'expansions of y/n answers', 'dispreferred answers', 'quoted material', 'hedge', 'segment (multi-utterance)', 'other']
print(len(li_1))
print(len(li_2))


now = []
for item in files:
    file = open(item, 'r')
    s = file.read().splitlines()
    now += s




for sentence in now:
        sentence = sentence.strip()

        if (sentence.find('A.') != -1 or sentence.find('B.') != -1) and sentence.find("utt") != -1:

        #label
                if sentence.startswith('%') == True:
                        if sentence.find('-/') != -1 or sentence.find('- /') != -1:
                                label_li.append('abandoned')
                        else:
                                label_li.append('uninterpretable')
                else:
                        for i in range(61):
                                a = sentence.startswith(li_1[i])
                                if a == True:
                                        label_li.append(li_2[i])
                                        break
                                else:
                                        continue
        else:
                continue
#A,B
for sentence in now:
        if sentence.find('A.') != -1 and sentence.find("utt") != -1:
                person_li.append('A')
        elif sentence.find('B.') != -1 and sentence.find("utt") != -1:
                person_li.append('B')
        else:
                continue
        
#content
for sentence in now:
        sentence = sentence.strip().rstrip('/')
        
        if (sentence.find('A.') != -1 or sentence.find('B.') != -1) and sentence.find("utt") != -1:
                m = sentence.split(':', 1)
                sentence_li += m
        else:
                continue
print(len(sentence_li))

for i in range(447210, -2, -2):
        del sentence_li[i]
        


        
print(label_li[10:40])
print(len(label_li))
print(person_li[0:10])
print(len(person_li))
print(sentence_li[0:10])
print(len(sentence_li))

#Write
file_w = open("./con_swbd.py", 'wb')
d = '| {:^6} | {:^30} | {:<10} |\n'.format('Person', 'Tag', 'Sentence')
file_w.write(d.encode())
for i in range(len(label_li)):
        c = '| {:^6} | {:^30} | {:<10} |\n'.format(person_li[i], label_li[i], sentence_li[i])
        file_w.write(c.encode())

file_w.close()




    



