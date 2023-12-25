import unittest
import main
import copy

class TestFunc(unittest.TestCase):
    def test_func(self):
        # value1 = 1 # 引数１
        # value2 = 2 # 引数２
        # ...
        # expected = 3 # 期待される値
        # actual = main.func(value1, value2 , ...)
        # self.assertEqual(expected, actual)
        """
        expected = "hello world"
        actual = main.forTest()
        self.assertEqual(expected, actual)
        """
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
        deck_now = copy.deepcopy(deck)
        cond = 1
        school_card_list = school_card_list = ["a","b","d","e","j","k"]
        hand = []
        deck_now, hand = main.draw(deck_now, cond, school_card_list, hand)
        expected = True
        actual = bool()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()