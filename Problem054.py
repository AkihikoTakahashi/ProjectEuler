# coding: utf-8


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


class Card():
    def __init__(self, num_suit):
        num = num_suit[0]
        suit = num_suit[1]

        if num == 'T':
            num = 10
        elif num == 'J':
            num = 11
        elif num == 'Q':
            num = 12
        elif num == 'K':
            num = 13
        elif num == 'A':
            num = 14
        self.number = int(num)
        self.suit = suit


class Hand():
    def __init__(self, cards):
        card_dict = {i: 0 for i in range(2, 15)}
        for c in cards:
            card_dict[c.number] += 1
        self.cards = cards
        self.card_dict = {k: v for k, v in card_dict.items() if v != 0}

    def numbers(self):
        return sorted([card.number for card in self.cards], reverse=True)

    def suits(self):
        suit_dict = {'H': 0, 'C': 0, 'D': 0, 'S': 0}
        for card in self.cards:
            suit_dict[card.suit] += 1
        return suit_dict

    def sorted_card(self):
        cards = list(self.card_dict.items())
        cards.sort(key=lambda x: x[0] + x[1] * 15, reverse=True)
        sorted_numbers = list(map(lambda x: x[0], cards))
        return sorted_numbers

    def determine_hand(self):
        numbers = self.numbers()
        number_dict = self.card_dict
        suits = self.suits()

        is_same_suits = max(suits.values()) == 5
        is_consective = list(map(lambda x: x - min(numbers),
                                 numbers)) == [4, 3, 2, 1, 0]
        is_four_same_cards = 4 in number_dict.values()
        is_three_same_cards = 3 in number_dict.values()
        is_two_same_cards = 2 in number_dict.values()

        sorted_numbers = self.sorted_card()

        if is_consective:
            if is_same_suits:
                if numbers == [15, 14, 13, 12, 11, 10]:
                    return [9] + sorted_numbers  # ロイヤルストレートフラッシュ
                else:
                    return [8] + sorted_numbers  # ストレートフラッシュ
            else:
                return [4] + sorted_numbers  # ストレート

        if is_same_suits:
            return [5] + sorted_numbers  # フラッシュ

        if is_four_same_cards:
            return [7] + sorted_numbers  # フォーカード

        if is_three_same_cards:
            if is_two_same_cards:
                return [6] + sorted_numbers  # フルハウス
            else:
                return [3] + sorted_numbers  # スリーカード

        if sum(1 for i in number_dict.values() if i == 2) == 1:
            return [1] + sorted_numbers  # ワンペア
        if sum(1 for i in number_dict.values() if i == 2) == 2:
            return [2] + sorted_numbers  # ツーペア

        return [0] + numbers

    def __gt__(self, another):
        my_value = self.determine_hand()
        another_value = another.determine_hand()

        for i in range(5):
            if my_value[i] == another_value[i]:
                continue
            return my_value[i] > another_value[i]


def main():
    url = "https://projecteuler.net/project/resources/p054_poker.txt"
    download(url)

    cnt = 0
    with open(url.split('/')[-1], 'r') as f:
        for line in f:

            game = line.rstrip().split(' ')

            player1 = Hand(list(map(Card, game[:5])))
            player2 = Hand(list(map(Card, game[5:])))

            if player1 > player2:
                cnt += 1

    return cnt
