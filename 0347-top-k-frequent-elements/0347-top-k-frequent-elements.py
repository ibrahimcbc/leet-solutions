class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count= -1 
        max_number= None
        result=[]
        dictim= dict()

        for i in nums:
            if i not in dictim:
                dictim[i]= 1
            else:
                dictim[i]= dictim.get(i)+1

        while k:
                    
            for i in dictim:
                if dictim[i]>max_count:
                    max_number=i
                    max_count= dictim[i]
            
            result.append(max_number)
            del dictim[max_number]
            max_number=None
            max_count=-1
            k-=1

        return result