#coding:utf8

from pyexcel_xls import XLBook
import jsonpickle
import sys, getopt

def xls2json(sheet):
    '''
    将excel表格转换成json
    :param sheet:excel表sheet数据
    :return:json数组
    '''
    lineMax = len(sheet)
    if lineMax < 2:
        return []

    title = sheet[0]
    size = len(title)
    data = []
    for ln in range(1,lineMax):
        tmp = sheet[ln]
        map = {}
        for i in range(0,size):
            if title[i][0]=='i': #把float数转成int
                map[title[i]] = int(tmp[i])
            else:
                map[title[i]] = tmp[i]
        data.append(map)
    return data

def xls2jsonString(sheet):
    '''
    将excel表格转换成json格式字符串
    :param sheet:excel表sheet数组
    :return:json数组字符串
    '''
    data = xls2json(sheet)
    return jsonpickle.encode(data)

def xls2jsonFrmFile(filename):
     book = XLBook(filename)
     if book != None:
         xlsData = dict(book.sheets())
         return xls2json(xlsData["Sheet1"])
     return []

def jsonStringToFile(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "i:o:") #i:o:表格key，value形式如果只有一个h这种的标示开关项，没有值
    inputFile = ""
    outputFile = ""

    for op, value in opts:
        if op == "-i":
            inputFile = value
        elif op == "-o":
            outputFile = value

    if inputFile != "" and outputFile != "":
        book = XLBook(inputFile)
        xlsData = dict(book.sheets())
        data = xls2jsonString(xlsData["Sheet1"])
        jsonStringToFile(outputFile,data)



