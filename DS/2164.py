import sys
import collections

N = int(sys.stdin.readline())
deck = collections.deque([i for i in range(1, N+1)])

while (len(deck) != 1):
    deck.popleft()
    deck.append(deck.popleft())
print(deck[0])