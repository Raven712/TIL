#1이 집 0이 집아님
import sys
sys.stdin = open('2667.txt', 'r')
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().strip())) for i in range(n)]
# print(graph)
dy = [-1, 1, 0, 0]#상하좌우
dx = [0, 0, -1, 1]

# def dfs(start):
#     for y in range(n):
#         for x in range(n):
#             if graph[y][x] == 0:
#                 continue
#             for adj in range(4):
#                 ny = 