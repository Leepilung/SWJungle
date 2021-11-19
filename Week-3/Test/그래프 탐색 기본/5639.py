# 백준 알고리즘 - 5639 이진 검색 트리
# https://www.acmicpc.net/problem/5639
# 시도 횟수 : 
# 실패 : 
# 통과 : 

import sys
sys.setrecursionlimit(100000)

arr = []
while True:
  try:
    arr.append(int(sys.stdin.readline().strip()))
  except:
    break

def postorder(arr):
  if len(arr) <= 1:
    return arr
  for i in range(1, len(arr)):
    if arr[i] > arr[0]:
      return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]
  return postorder(arr[1:]) + [arr[0]]

arr = postorder(arr)
for i in arr:
  print(i)`