# Create your tests here.
Dir_sensitive = './static/forbiddenword/words.txt'
Dir_stopWord = './static/forbiddenword/words.txt'
class SensitiveFilter:
    def __init__(self):
        # file把敏感词库加载到列表中
        file = open(Dir_sensitive, 'r', encoding='utf-8')
        file_lst = file.readlines()
        self.sensitiveWordList = [i.split('\n')[0] for i in file_lst]
        # print(sensitiveWordList[:10])
        # >>['1234', '12345', '123456', '甲基麻黄碱', '来曲唑', '依西美坦', '阿那曲唑', '螺内酯', '沙美特罗', '丙磺舒']
        # file1把停用词加载到列表中
        file1 = open(Dir_stopWord, 'r', encoding='utf-8')
        file1_lst = file1.readlines()
        self.stopWordList = [i.split('\n')[0] for i in file1_lst]
        ##得到sensitive字典
        self.sensitiveWordMap = self.initSensitiveWordMap(self.sensitiveWordList)

    # 构建敏感词库
    def initSensitiveWordMap(self, sensitiveWordList):
        sensitiveWordMap = {}
        # 读取每一行，每一个word都是一个敏感词
        for word in sensitiveWordList:
            nowMap = sensitiveWordMap
            # 遍历该敏感词的每一个特定字符
            for i in range(len(word)):
                keychar = word[i]
                wordMap = nowMap.get(keychar)
                if wordMap != None:
                    # nowMap更新为下一层
                    nowMap = wordMap
                else:
                    # 不存在则构建一个map,isEnd设置为0，因为不是最后一个
                    newNextMap = {}
                    newNextMap["isEnd"] = 0
                    nowMap[keychar] = newNextMap
                    nowMap = newNextMap
                # 到这个词末尾字符
                if i == len(word) - 1:
                    nowMap["isEnd"] = 1
        # print(sensitiveWordMap)
        return sensitiveWordMap

    def checkSensitiveWord(self, txt, beginIndex=0):
        '''
        :param txt: 输入待检测的文本
        :param beginIndex:输入文本开始的下标
        :return:返回敏感词字符的长度
        '''
        nowMap = self.sensitiveWordMap
        sensitiveWordLen = 0  # 敏感词的长度
        containChar_sensitiveWordLen = 0  # 包括特殊字符敏感词的长度
        endFlag = False  # 结束标记位

        for i in range(beginIndex, len(txt)):
            char = txt[i]
            if char in self.stopWordList:
                containChar_sensitiveWordLen += 1
                continue

            nowMap = nowMap.get(char)
            if nowMap != None:
                sensitiveWordLen += 1
                containChar_sensitiveWordLen += 1
                # 结束位置为True
                if nowMap.get("isEnd") == 1:
                    endFlag = True
            else:
                break
        if endFlag == False:
            containChar_sensitiveWordLen = 0
        # print(sensitiveWordLen)
        return containChar_sensitiveWordLen

    def getSensitiveWord(self, txt):
        cur_txt_sensitiveList = []
        # 注意，并不是一个个char查找的，找到敏感词会i增强敏感词的长度
        for i in range(len(txt)):
            length = self.checkSensitiveWord(txt, i)
            if length > 0:
                word = txt[i:i + length]
                cur_txt_sensitiveList.append(word)
                i = i + length - 1  # 出了循环还要+1 i+length是没有检测到的，下次直接从i+length开始

        return cur_txt_sensitiveList

    def replaceSensitiveWord(self, txt, replaceChar='*'):
        Lst = self.getSensitiveWord(txt)
        # print(Lst)
        for word in Lst:
            replaceStr = len(word) * replaceChar
            txt = txt.replace(word, replaceStr)

        return txt


if __name__ == "__main__":
    str = "尼玛死了"
    Filter = SensitiveFilter()
    replaceStr = Filter.replaceSensitiveWord(str)
    print(replaceStr)
