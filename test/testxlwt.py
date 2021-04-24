import xlwt

workbook = xlwt.Workbook(encoding='GBK')
worksheet = workbook.add_sheet('sheet1')
for i in range(9):
    for j in range(0, i+1):
        worksheet.write(i, j, "%d * %d = %d" % (j+1, i+1, (j+1)*(i+1)))
workbook.save('123.xls')
