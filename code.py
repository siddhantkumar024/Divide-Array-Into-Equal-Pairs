class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)
        x=n//2
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        c=0
        for k,v in d.items():
            v=v//2
            c+=v
        if c==x:
            return True
        return False
        
