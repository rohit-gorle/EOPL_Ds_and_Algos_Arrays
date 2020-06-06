class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 =0
        n2 =0
        new_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        
        for i,j in enumerate(reversed(num1)):
            n1+=new_dict[j]*pow(10,i)
        
        for i,j in enumerate(reversed(num2)):
            n2+=new_dict[j]*pow(10,i)
        
        return str(n1*n2)
                                
            
            
