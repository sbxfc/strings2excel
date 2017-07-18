# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import xlwt
import xlrd
import re

if len(sys.argv) < 2:
	print 'No file specified.'
	sys.exit()

fopen=open(sys.argv[1],'r')
lines=fopen.readlines()
#新建一个excel文件
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
#新建一个sheet
sheet=file.add_sheet('App语言')

############################
sheetNum=0
steetIndex=0
for line in lines:
	if line.startswith('#') or line.startswith('/*') or not line.split():
		continue
	rst=re.findall('"(.*?)"',line)
	if len(rst) > 0:
		sheet.write(steetIndex,sheetNum,rst[0])
		steetIndex=steetIndex+1

#################################
file.save('language.xls')

print("Import Success")
