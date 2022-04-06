class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        # count = 0
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         for k in range(len(arr)):
        #             if i < j and j < k:
        #                 if arr[i] + arr[j] + arr[k] == target:
        #                     count +=1
        # return count
        
        # arr.sort()
        # count = 0
        # for i in range(len(arr)-2):
        #     j = i+1
        #     k = len(arr)-1
        #     while j < k:
        #         if arr[j] + arr[k] == target - arr[i]:
        #             print(i,j,k)
        #             count +=1
        #             tempj = j
        #             while(arr[tempj+1] == arr[tempj] and (tempj+1 < k)):
        #                 print("j: ",j, j+1)
        #                 tempj +=1
        #                 count +=1
        #             while(arr[k-1] == arr[k] and (j < k-1)):
        #                 print("k: ",k, k-1)
        #                 k -=1
        #                 count +=1
        #             else:
        #                 j +=1
        #                 tempj = j
        #                 k -=1
        #             j = tempj
        #         elif arr[j] + arr[k] < target - arr[i]:
        #             j +=1
        #         elif arr[j] + arr[k] > target - arr[i]:
        #             k -=1
        # return count%1000000007
        
        arr.sort()
        cnt = Counter(arr)  # obtain the number of instances of each number
        res, i, l = 0, 0, len(arr)
        while i < l:  # in replacement of the for-loop, so that we can increment i by more than 1
            j, k = i, l-1  # j should be the leftmost index, hence j=i instead of j=i+1
            while j < k:  # i <= j < k; arr[i] <= arr[j] <= arr[k]
                if arr[i]+arr[j]+arr[k] < target:
                    j += cnt[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= cnt[arr[k]]
                else:  # arr[i]+arr[j]+arr[k] == target
                    if arr[i] != arr[j] != arr[k]:  # Case 1: All the numbers are different
                        res += cnt[arr[i]]*cnt[arr[j]]*cnt[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:  # Case 2: The smaller two numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*cnt[arr[k]]//2  # math.comb(cnt[arr[i]], 2)*cnt[arr[k]]
                    elif arr[i] != arr[j] == arr[k]:  # Case 3: The larger two numbers are the same
                        res += cnt[arr[i]]*cnt[arr[j]]*(cnt[arr[j]]-1)//2  # math.comb(cnt[arr[j]], 2)*cnt[arr[i]]
                    else:  # Case 4: All the numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*(cnt[arr[i]]-2)//6  # math.comb(cnt[arr[i]], 3)
					# Shift pointers by the number of instances of the number
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]]  # Shift pointer by the number of instances of the number
        return res%1000000007
                    