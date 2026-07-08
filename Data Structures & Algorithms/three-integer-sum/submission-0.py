class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort()
        res=[]
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            
            left=i+1
            right=len(num)-1

            while left<right:
                sum=num[i]+num[left]+num[right]
                if sum<0:
                    left +=1
                elif sum>0:
                    right -=1
                else:
                    res.append([num[i],num[left],num[right]])

                    left +=1
                    right -=1
                
                    while left<right and num[left]==num[left-1]:
                        left +=1
                    while left <right and num[right]==num[right+1]:
                        right -=1
        return res
        