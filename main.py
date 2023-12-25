import random
import copy
import possibility


def main():
    deck = [
        "a","a","a", #ルゥ
        "b","b","b", #試験場
        "c","c","c", #噴水
        "d","d", #学び舎
        "e","e","e", #ベルディリア
        "f","f","g", #ミュース
        "h","h", #コンディクター
        "i","i","i", #有翼
        "j","j", #令嬢
        "k","k","k", #エルヴィーラ
        "l","l","l", #アイテール
        "m","m", #オリシル
        "n","n", #アルミラ
        "o","o", #エルラーデ
        "p","p","p", #ジャンヌ
        "q" #アポストロアームズ
    ]

    school_card_list = ["a","b","d","e","j","k"]

    for i in range(70000):
        deck_mulligan= copy.deepcopy(deck)
        deck_now = copy.deepcopy(deck)
        hand = []
        field = []
        f_or_l = random.randint(0,1)
        # 0: first, 1: last
        deck_now, hand = mulligan(deck_mulligan, deck_now, school_card_list, hand)
        possibility.write_mulligan(hand)
        deck_now, hand, field, hunsui_draw_at_4 = Turn1(deck_now, hand, school_card_list, field, f_or_l)
        deck_now, hand, field, hunsui_draw_at_5, exam_draw_at_4 = Turn2(deck_now, hand, school_card_list, field)
        deck_now, hand, field, exam_draw_at_5 = Turn3(deck_now, hand, school_card_list, field)
        deck_now, hand, field = Turn4(deck_now, hand, school_card_list, field, f_or_l, hunsui_draw_at_4, exam_draw_at_4)
        possibility.write_turn4_field(field)
        deck_now, hand, field = Turn5(deck_now, hand, school_card_list, field, hunsui_draw_at_5, exam_draw_at_5)
        possibility.write_turn5_field(field)

def mulligan(deck_mulligan, deck_now, school_card_list, hand):
    for j in range(3):
        cond = 0
        deck_mulligan, hand = draw(deck_mulligan, cond, school_card_list, hand)
    keep = []
    if "k" in hand:
        keep.append("k")
    elif "l" in hand:
        keep.append("l")
    if "i" in hand:
        keep.append("i")
    if ("k" in hand or "l" in hand) and "i" in hand:
        if "c" in hand:
            keep.append("c")
    for card_keep in keep:
        deck_now.remove(card_keep)
    #print(keep, len(deck_now))
    hand = keep
    for j in range(3-len(keep)):
        cond = 0
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    return deck_now, hand

def draw(deck_now, cond, school_card_list, hand):
    # condition -> 0:ノーマル　1:学園
    if cond == 1:
        drawn_card = ""
        while drawn_card not in school_card_list and drawn_card != "d":
            drawn_card = deck_now[random.randint(0,len(deck_now)-1)]
    else:
            drawn_card = deck_now[random.randint(0,len(deck_now)-1)]
    deck_now.remove(drawn_card)
    if len(hand) < 9:
        hand.append(drawn_card)
    return deck_now, hand

def Turn1(deck_now, hand, school_card_list, field, f_or_l):
    for i in range(f_or_l + 1):
        cond = 0
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    hunsui_draw_at_4 = 0
    if "c" in hand:
        # play c
        hand.remove("c")
        field.append("c")
        hunsui_draw_at_4 = 1
    return deck_now, hand, field, hunsui_draw_at_4

def Turn2(deck_now, hand, school_card_list, field):
    cond = 0
    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    exam_draw_at_4 = 0
    hunsui_draw_at_5 = 0
    if "b" in hand and "d" in hand:
        if ("k" in hand or "l" in hand) and "i" in hand:
            # play d
            hand.remove("d")
            field.append("d")
            cond = 1
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        elif "k" in hand:
            # play b
            hand.remove("b")
            field.append("b")
            cond = 0
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
            exam_draw_at_4 = 1
        else:
            deck_len = len(deck_now)
            school_len = 0
            for j in school_card_list:
                school_len += deck_now.count(j)
            num_of_k = deck_now.count("k")
            num_of_l = deck_now.count("l")
            if num_of_k / school_len <= (num_of_k + num_of_l) / deck_len:
                # play b
                hand.remove("b")
                field.append("b")
                cond = 0
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
                exam_draw_at_4 = 1
            else:
                # play d
                hand.remove("d")
                field.append("d")
                cond = 1
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "b" in hand:
        # play b
        hand.remove("b")
        field.append("b")
        cond = 0
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        exam_draw_at_4 = 1
    elif "d" in hand:
        # play d
        hand.remove("d")
        field.append("d")
        cond = 1
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "c" in hand:
        # play c
        hand.remove("c")
        field.append("c")
        hunsui_draw_at_5 = 1
    return deck_now, hand, field, hunsui_draw_at_5, exam_draw_at_4

def Turn3(deck_now, hand, school_card_list, field):
    cond = 0
    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    exam_draw_at_5 = 0
    if "b" in hand and "d" in hand:
        if ("k" in hand or "l" in hand) and "i" in hand:
            # play d
            hand.remove("d")
            field.append("d")
            cond = 1
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        elif "k" in hand:
            # play b
            hand.remove("b")
            field.append("b")
            cond = 0
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
            exam_draw_at_5 = 1
        else:
            deck_len = len(deck_now)
            school_len = 0
            for j in school_card_list:
                school_len += deck_now.count(j)
            num_of_k = deck_now.count("k")
            num_of_l = deck_now.count("l")
            if num_of_k / school_len <= (num_of_k + num_of_l) / deck_len:
                # play b
                hand.remove("b")
                field.append("b")
                cond = 0
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
                exam_draw_at_5 = 1
            else:
                # play d
                hand.remove("d")
                field.append("d")
                cond = 1
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "b" in hand:
        # play b
        hand.remove("b")
        field.append("b")
        cond = 0
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        exam_draw_at_5 = 1
    elif "d" in hand:
        # play d
        hand.remove("d")
        field.append("d")
        cond = 1
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    return deck_now, hand, field, exam_draw_at_5

def Turn4(deck_now, hand, school_card_list, field, f_or_l, hunsui_draw_at_4, exam_draw_at_4):
    cond = 0
    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    if hunsui_draw_at_4 == 1:
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        field.remove("c")
    if exam_draw_at_4 == 1:
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        field.remove("b")
    if "i" in hand:
        #play i
        hand.remove("i")
        field.append("i")
        if hunsui_draw_at_4 != 1 and exam_draw_at_4 != 1:
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        if f_or_l:
            if "b" in hand and "d" in hand:
                if ("k" in hand or "l" in hand) and "i" in hand:
                    # play d
                    hand.remove("d")
                    field.append("d")
                    cond = 1
                    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
                elif "k" in hand:
                    # play b
                    hand.remove("b")
                    field.append("b")
                    cond = 0
                    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
                else:
                    deck_len = len(deck_now)
                    school_len = 0
                    for j in school_card_list:
                        school_len += deck_now.count(j)
                    num_of_k = deck_now.count("k")
                    num_of_l = deck_now.count("l")
                    if num_of_k / school_len <= (num_of_k + num_of_l) / deck_len:
                        # play b
                        hand.remove("b")
                        field.append("b")
                        cond = 0
                        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
                    else:
                        # play d
                        hand.remove("d")
                        field.append("d")
                        cond = 1
                        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
            elif "b" in hand:
                # play b
                hand.remove("b")
                field.append("b")
                cond = 0
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
            elif "d" in hand:
                # play d
                hand.remove("d")
                field.append("d")
                cond = 1
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "k" in hand:
        # play k
        hand.remove("k")
        field.append("k")
    elif "b" in hand and "d" in hand:
        if "l" in hand:
            # play b
            hand.remove("b")
            field.append("b")
            cond = 0
            deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        else:
            deck_len = len(deck_now)
            school_len = 0
            for j in school_card_list:
                school_len += deck_now.count(j)
            num_of_k = deck_now.count("k")
            num_of_l = deck_now.count("l")
            if num_of_k / school_len <= (num_of_k + num_of_l) / deck_len:
                # play b
                hand.remove("b")
                field.append("b")
                cond = 0
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
            else:
                # play d
                hand.remove("d")
                field.append("d")
                cond = 1
                deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "b" in hand:
        # play b
        hand.remove("b")
        field.append("b")
        cond = 0
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    elif "d" in hand:
        # play d
        hand.remove("d")
        field.append("d")
        cond = 1
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    return deck_now, hand, field

def Turn5(deck_now, hand, school_card_list, field, hunsui_draw_at_5, exam_draw_at_5):
    cond = 0
    deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    if hunsui_draw_at_5 == 1:
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        field.remove("c")
    if exam_draw_at_5 == 1:
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
        field.remove("b")
    if "i" in field and (hunsui_draw_at_5 == 1 or exam_draw_at_5 == 1):
        deck_now, hand = draw(deck_now, cond, school_card_list, hand)
    if "l" in hand and "k" not in field:
        # play l
        hand.remove("l")
        field.append("l")
        field.append("k")
    elif "k" in hand and "k" not in field:
        #play k
        hand.remove("k")
        field.append("k")
    elif "i" in hand:
        #play i
        hand.remove("i")
        field.append("i")
    return deck_now, hand, field

"""
def forTest():
    a = "hello world"
    return a
"""

if __name__ == "__main__":
    main()
    possibility.P_mulligan()
    possibility.P_turn4()
    possibility.P_turn5()