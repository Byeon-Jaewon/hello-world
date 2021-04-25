import heapq
import sys

input = lambda : sys.stdin.readline()

def maxheap_push(x):
    heapq.heappush(heap, x)
def maxheap_pop():
    if len(heap) == 0 :
        print(0)
    else :
        max_item = heapq.heappop(heap)
        print(max_item)

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        maxheap_pop()
    else :
        maxheap_push(x)