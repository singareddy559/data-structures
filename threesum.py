class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n=len(A)
        A=sorted(A)
        
        minvalue=float('inf')
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                sum1=A[i]+A[j]+A[k]
                dif =abs(sum1-B)
                if dif==0:
                    return sum1
                if dif<minvalue:
                    minvalue=dif
                    closetsum=sum1
                if sum1<=B:
                    j=j+1
                else:
                    k=k-1
        return closetsum
            
