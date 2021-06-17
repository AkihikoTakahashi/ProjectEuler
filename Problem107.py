# coding: utf-8

# プリム法を使う
# https://ja.wikipedia.org/wiki/%E3%83%97%E3%83%AA%E3%83%A0%E6%B3%95

from queue import PriorityQueue


def download(url):
    import urllib.request
    import os

    save_name = url.split("/")[-1]
    if not os.path.isfile(save_name):
        urllib.request.urlretrieve(url, save_name)


def get_minimal_network(edges):
    pq = PriorityQueue()
    sum_weight = 0
    n = len(edges)
    used = [False] * n  # Falseなら未使用

    for e in edges[0]:
        pq.put(e)
    used[0] = True

    while not all(used):
        cost, to = pq.get()

        # 行き先がすでに使っていればやりなおす
        if used[to]:
            continue

        used[to] = True
        sum_weight += cost

        # 点to を PriorityQueue に追加する
        for e in edges[to]:
            pq.put(e)
    return sum_weight


def main():
    url = "https://projecteuler.net/project/resources/p107_network.txt"
    download(url)

    # edge[i] には 点i から出る辺 (重み, 終点) のリストを入れる
    edges = []
    total_weight = 0
    with open(url.split('/')[-1], 'r') as f:
        for line in f:
            e = []
            for j, weight in enumerate(line.rstrip().split(',')):
                if weight != '-':
                    e.append((int(weight), j))
                    total_weight += int(weight)
            edges.append(e)
    total_weight //= 2

    min_weight = get_minimal_network(edges)
    return total_weight - min_weight


if __name__ == '__main__':
    print(main())
