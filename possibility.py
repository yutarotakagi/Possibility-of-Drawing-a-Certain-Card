def write_mulligan(hand):
    s = ""
    for i in hand:
        s += i
    f = open('data/mulligan.txt', "a")
    f.write(s)
    f.write('\n')
    f.close

def P_mulligan():
    f = open('data/mulligan.txt')
    hands = f.readlines()
    f.close()
    length = len(hands)
    num_of_i = 0
    num_of_k = 0
    num_of_l = 0
    num_of_both = 0
    num_of_perf = 0
    num_of_dup = 0
    for h in hands:
        if "i" in h:
            num_of_i += 1
        if "k" in h:
            num_of_k += 1
        if "l" in h:
            num_of_l += 1
        if ("k" in h or "l" in h) and "i" in h:
            num_of_both += 1
            if "c" in h:
                num_of_perf += 1
        if "k" in h and "l" in h:
            num_of_dup += 1
    p_i = num_of_i /length * 100
    p_k = num_of_k / length * 100
    p_l = num_of_l / length * 100
    p_b = num_of_both / length * 100
    p_p = num_of_perf /length * 100
    p_d = num_of_dup / length * 100
    print(
        "mulligan\n",
        "有翼 :", p_i, "\n",
        "エルヴィーラ :", p_k, "\n",
        "アイテール :", p_l, "\n",
        "両方 :", p_b, "\n",
        "完璧 :", p_p, "\n",
        "だぶり :", p_d, "\n"
    )

def write_turn4_field(field):
    s = ""
    for i in field:
        s += i
    f = open('data/turn4.txt', "a")
    f.write(s)
    f.write('\n')
    f.close

def P_turn4():
    f = open('data/turn4.txt')
    fields = f.readlines()
    f.close()
    length = len(fields)
    num_of_i = 0
    num_of_k = 0
    for f in fields:
        if "i" in f:
            num_of_i += 1
        if "k" in f:
            num_of_k += 1
    p_i = num_of_i / length * 100
    p_k = num_of_k / length * 100
    print(
        "turn4\n",
        "灯火 :", p_i, "\n",
        "エルヴィーラ :", p_k
    )

def write_turn5_field(field):
    s = ""
    for i in field:
        s += i
    f = open('data/turn5.txt', "a")
    f.write(s)
    f.write('\n')
    f.close

def P_turn5():
    f = open('data/turn5.txt')
    fields = f.readlines()
    f.close()
    length = len(fields)
    num_of_i = 0
    num_of_k = 0
    num_of_both = 0
    for f in fields:
        if "i" in f and "k" in f:
            num_of_i += 1
            num_of_k += 1
            num_of_both += 1
        elif "i" in f:
            num_of_i += 1
        elif "k" in f:
            num_of_k += 1
    p_i = num_of_i / length * 100
    p_k = num_of_k / length * 100
    p_b = num_of_both / length * 100
    print(
        "turn5",
        "灯火 :", p_i, "\n",
        "エルヴィーラ :", p_k, "\n",
        "両方 :", p_b
    )