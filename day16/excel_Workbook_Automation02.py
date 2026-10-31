import xlwings as xw
import os

xlApp = xw.App(visible=False)
# xlApp.visible = True

# # print(type(xlApp))

# # app = xw.App(visible=True, add_book=False)
app = xw.App(visible=True, add_book=True)

# print(xlApp.version)

# open excel
path = "E:\\Code\\Python-Automation-60Days\\day16\\Random Sales Data.xlsx"
data_file = xw.books.open(path)
print(data_file.name)
data_file.close()

# print(os.getcwd())
# os.environ["userprofile"] + "\\" + "Desktop"                            # desktop location
xw.Book("Book10").save(os.environ["userprofile"] + "\\" + "Desktop"+"\\"+"testProject01.xlsx")
xw.Book("testProject01.xlsx").close()

