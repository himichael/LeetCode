题目内容：
给你一个正整数，比如n=3，要求你返回如下内容
输入:3
返回:
["1","2*3","4*5*6","4*5*6","2*3","1"]
解释:
这是打印一个三角形，三角形的高度是n*2，
1
2*3
4*5*6
4*5*6
2*3
1
当n=3时，第一列输入1，第二列输出2*3，第三列输出4*5*6
这是三角形的上半部分，之后再输出下半部分，下半部分和上半部分的内容一样，是倒序输出的
下半部分第一列输出 4*5*6，下半部分第二列输出2*3，下半部分第三列输出1

输入:5
返回:
['1', '2*3', '4*5*6', '7*8*9*10', '11*12*13*14*15', '11*12*13*14*15', '7*8*9*10', '4*5*6', '2*3', '1']
解释:
输入n=5之后，输出的三角形格式为:
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1

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