class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        
        def rotate(s):
            stack = []
            queue = []
            for i in s:
                queue.append(i)
            def rotate_assemble(queue,stack):
                if(not queue):
                    res.add( "".join(list(stack)) )
                    return
                size = len(queue)
                for _ in xrange(size):
                    stack.append(queue.pop(0))
                    rotate_assemble(queue, stack)
                    queue.append(stack.pop())
            rotate_assemble(queue, stack)
            
        
        def recursive(i,tmp):
            #res.add(tmp)
            rotate(tmp)
            for j in range(i,len(tiles)):
                x = tmp
                recursive(j+1, x+tiles[j])
        recursive(0, "")
        return len(res)-1
    
    