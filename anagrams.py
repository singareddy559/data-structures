class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        if A is None: 
            return A
        n=len(A)
        list_of_integers = []
        groupcount = 0
        hashmap = {}
        for i in range(n):
            groupstring = ''.join(sorted(A[i]))
            if groupstring not in hashmap:
                list_of_integers.append([i+1])
                hashmap[groupstring] = groupcount
                groupcount += 1
            else:
                list_of_integers[hashmap[groupstring]].append(i+1)
        
        return  list_of_integers
