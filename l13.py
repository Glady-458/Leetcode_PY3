class Solution:
    def romanToInt(self, s: str) -> int:
        Rom = s
        Num = 0
        SSym = {'I':1, 'V':5 ,'X':10 ,'L':50 ,'C':100 ,'D':500,'M':1000}
        Comb = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        r = 0
        #I = 1
        #V = 5
        #X = 10
        #L = 50
        #C = 100
        #D = 500
        #M = 1000
        #Roman = [I,V,X,L,C,D,M]
        while r < len(Rom):
            if(r < len(Rom)-1 and Rom[r:r+2]in Comb):
                Num = Num+Comb[Rom[r:r+2]]
                r = r + 2
                #processing to sym at a time
            else:
                Num = Num+SSym[Rom[r]]
                r = r + 1
        return Num
