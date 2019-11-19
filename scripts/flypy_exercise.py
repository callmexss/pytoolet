'''
File:          flypy_exercise.py
File Created:  Tuesday, 19th November 2019 11:25:11 am
Author:        xss (callmexss@126.com)
Description:   flypy learn
-----
Last Modified: Tuesday, 19th November 2019 11:25:33 am
Modified By:   xss (callmexss@126.com)
-----
'''
import random

from pprint import pprint

class Card:
    def __init__(self, front, back, hint, wrong):
        self.front = front
        self.back = back
        self.hint = hint
        self.wrong = int(wrong)
    
    def __str__(self):
        return '\t\t'.join([self.front, self.back, self.hint, str(self.wrong)]) + "\n"

        
class CardBuilder:
    def __init__(self):
        self.cards = []
        # with open("zi.txt", encoding="utf-16le") as f:
        with open("new_zi.txt", encoding="utf-8") as f:
            # li = f.readlines()[8:-4]
            li = f.readlines()
            for i, line in enumerate(li):
                # print(line.strip().split("\t\t"))
                # if i == len(li):
                #     li[i] = line.strip() + "\t\t0"
                # else:
                #     li[i] = line.strip() + "\t\t0\n"
                self.cards.append(Card(*line.strip().split("\t\t")))
        
        # with open("new_zi.txt", encoding="utf-8", mode="w") as f:
            # f.writelines(li)

    def get_cards(self):
        return self.cards
    
    
class Examiner:
    def __init__(self, cards):
        self.cards = cards
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        with open("new_zi.txt", "w") as f:
            f.writelines([str(card) for card in self.cards])
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_tb}')
            print('exception handled')
        return True

    def random_test(self, cnt=10):
        cards = random.sample(self.cards, cnt)
        for card in cards:
            self.test(card)

    def review_test(self, cnt=10):
        need_review = [card for card in self.cards if card.wrong > 0]
        if len(need_review) > cnt:
            need_review = random.sample(need_review, cnt)
        for card in need_review:
            self.test(card)

    def test(self, card):
        user_ans = input(f"请输入{card.front}的编码：")
        if user_ans == card.back:
            card.wrong += 1 if card.wrong < 0 else 0
            print("恭喜你，回答正确！")
        else:
            card.wrong += 1
            print("不好意思你答错了。")
            print("正确答案是：", end="")
            print(card.hint)
            print(card.back)


if __name__ == "__main__":
    bd = CardBuilder()
    with Examiner(bd.get_cards()) as teacher:
        teacher.random_test()
        teacher.review_test(3)
