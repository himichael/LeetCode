class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        def one_row_words(i):
            # 至少 一行能放下一个单词, cur_row_len
            left = i
            cur_row_len = len(words[i])
            i += 1
            while i < n:
                # 当目前行 加上一个单词长度 再加一个空格
                if cur_row_len + len(words[i]) + 1 > maxWidth:
                    break
                cur_row_len += len(words[i]) + 1
                i += 1
            return left, i

        while i < n:
            left, i = one_row_words(i)
            # 该行几个单词获取
            one_row = words[left:i]
            # 如果是最后一行了
            if i == n :
                res.append(" ".join(one_row).ljust(maxWidth," "))
                break
            # 所有单词的长度
            all_word_len = sum(len(i) for i in one_row)
            # 至少空格个数
            space_num = i - left - 1
            # 可以为空格的位置
            remain_space = maxWidth - all_word_len
            # 单词之间至少几个空格,还剩几个空格没用
            if space_num:
                a, b = divmod(remain_space, space_num)
            # print(a,b)
            # 该行字符串拼接
            tmp = ""
            for word in one_row:
                if tmp:
                    tmp += " " * a
                    if b:
                        tmp += " "
                        b -= 1
                tmp += word
            #print(tmp, len(tmp))
            res.append(tmp.ljust(maxWidth, " "))
        return res
