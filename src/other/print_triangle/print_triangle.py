class Solution(object):
    def print_triangle(self,n):
        index = 1
        content = ""
        res = []
        for i in range(n):
            for j in range(i+1):
               content = content+str(index)+"*"
               index += 1 
            content = content[:len(content)-1]
            res.append(content)
            #print content
            content = ""
        index -= 1
        for i in range(n):
            for j in range(i,n):
                content = "*" + str(index) + content
                index -= 1
            content = content[1:len(content)]
            #print content
            res.append(content)
            content = ""   
        return res