# 백준 알고리즘 - 2751 수 정렬하기2
# https://www.acmicpc.net/problem/2751
# 시도 횟수 : 2
# 실패 : 1
# 통과 : 1

import sys

N = int(sys.stdin.readline().strip())
bucket = []
for i in range(N):
    bucket.append(int(sys.stdin.readline().strip()))

def megaSort(bucket):
    if len(bucket) > 1:
        mid = len(bucket) // 2
        lbucket, rbucket = bucket[:mid],bucket[mid:]
        megaSort(lbucket)
        megaSort(rbucket)
        li, ri, i = 0,0,0
        while li < len(lbucket) and ri < len(rbucket):
            if lbucket[li] < rbucket[ri]:
                bucket[i] = lbucket[li]
                li += 1
            else:
                bucket[i] = rbucket[ri]
                ri += 1
            i += 1
        bucket[i:] = lbucket[li:] if li != len(lbucket) else rbucket[ri:]

megaSort(bucket)

for i in bucket:
    print(i)