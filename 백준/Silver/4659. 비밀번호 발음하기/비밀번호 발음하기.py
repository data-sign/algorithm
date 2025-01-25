def check_word_quality(word): 
    pass_yn = False
    vowel_seq_cnt = 0
    consonant_seq_cnt = 0
    before_w = ''
    for w in word: 
        # 첫번재 조건
        if w in ('a', 'e', 'i', 'o', 'u'): 
            pass_yn = True
            # 두번째 조건 
            vowel_seq_cnt += 1
            consonant_seq_cnt = 0
            if vowel_seq_cnt >=3: 
                return False
        else: 
           vowel_seq_cnt = 0
           consonant_seq_cnt += 1
           if consonant_seq_cnt >=3: 
               return False
        # 3번째 조건 
        if before_w == w: 
            if (w != 'e')&(w != 'o'): 
                return False
        before_w = w
    return pass_yn

import sys 
input_ = sys.stdin.readlines()
for word in input_: 
    word = word.strip()
    if word == 'end': 
        break

    if check_word_quality(word): 
        print(f'<{word}> is acceptable.')
    else: 
        print(f'<{word}> is not acceptable.')
