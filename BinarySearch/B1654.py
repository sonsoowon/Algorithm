def max_len(k_arr, n):
    start = 1
    end = k_arr[-1]
    
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        # 현재 지정한 길이 mid가 K개의 랜선에서 잘라내는 랜선의 총 개수
        for k in k_arr:
            total += k // mid

        # 랜선의 개수가 n 이상이 아닐 경우 잘라내는 길이가 더 짧아져야 한다
        if total < n:
            end = mid - 1
        # 랜선의 개수가 n보다 크거나 같을 경우 반복문이 종료할 때까지 잘라내는 길이를 늘린다
        else:
            result = mid
            start = mid + 1

    return result


k, n = map(int, input().split())
inp_arr = [int(input()) for _ in range(k)]
inp_arr.sort()

print(max_len(inp_arr, n))



