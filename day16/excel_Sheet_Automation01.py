import xlwings as xw

# Open or create a new Excel workbook
wb = xw.Book()

# Alternative way: Launch a new Excel application instance explicitly and add a workbook
# app = xw.App(visible=True)
# wb = app.books.add()

# Print the full path of the workbook (empty string if unsaved)
# print(wb.fullname)


# --- ADDING WORKSHEETS ---

# Add worksheets before 'sheet1'
wb.sheets.add(name='TEST1', before='sheet1')
wb.sheets.add(name='TEST2', before='sheet1')
wb.sheets.add(name='Bangla', before='sheet1')
wb.sheets.add(name='Math', before='sheet1')

# Add a worksheet using user input
wb.sheets.add(name=input("Enter Sheet name: "), before='sheet1')

# Print the list of all sheets and the total sheet count
print(wb.sheets)
print(wb.sheets.count)

# Add 'TEST3' after the last sheet (using index count)
wb.sheets.add('TEST3', after=wb.sheets.count)

# Iterate through all sheets and print each sheet object
for wrk in wb.sheets:
    print(wrk)


# --- DELETING & SELECTING SPECIFIC SHEETS ---

# Delete a specific worksheet by name
wb.sheets['TEST3'].delete()  # Note: Modified string call to dictionary syntax

# Access a specific worksheet object and activate it
ws = wb.sheets['TEST2']
ws.activate()

# Print sheet details
print("Active Sheet Name:", ws.name)
print("Cells Object:", ws.cells)
print("Sheet Index Position:", ws.index)


# --- RENAMING WORKSHEETS ---

# Rename an existing worksheet
wb.sheets['TEST1'].name = 'First_WSH'


# --- HIDING & UNHIDING SHEETS ---

# Hide individual sheets using the underlying COM API (.api.Visible)
wb.sheets['Bangla'].api.Visible = False  # Hide sheet
wb.sheets['Math'].api.Visible = False    # Hide sheet

# Unhide multiple sheets using a loop (prevents pywintypes.com_error)
sheet_names = ['Bangla', 'Math']
for name in sheet_names:
    wb.sheets[name].api.Visible = True  # Unhide sheet


# --- SELECTING & COPYING SHEETS ---

# Select multiple worksheets simultaneously
wb.sheets[['Bangla', 'Math']].select()

# Copy a worksheet (creates a duplicate placed after 'Math' with a new name)
# Default copy: wb.sheets['Math'].copy()
wb.sheets['Math'].copy(after=wb.sheets['Math'], name='Math Copied')


# --- MOVING & PROTECTING SHEETS ---

# Move a sheet after 'sheet1' using COM API
# Syntax: Move(Before, After) -> Set Before=None when using After
wb.sheets['Bangla'].api.Move(None, After=wb.sheets['sheet1'].api)

# Protect and unprotect a worksheet with a password
# wb.sheets['Math'].api.Protect("abc")
# wb.sheets['Math'].api.Unprotect("abc")








































# import xlwings as xw

# wb = xw.Book()

# # app = xw.App(visible=True)
# # wb = app.books.add()

# # print(wb.fullname)

# # add worksheets
# wb.sheets.add(name= 'TEST1', before='sheet1')
# wb.sheets.add(name= 'TEST2', before='sheet1')
# wb.sheets.add(name= 'Bangla', before='sheet1')
# wb.sheets.add(name= 'Math', before='sheet1')
# wb.sheets.add(name= input("Enter Sheet name: "), before='sheet1')

# print(wb.sheets)
# print(wb.sheets.count)

# wb.sheets.add('TEST3', after=wb.sheets.count)

# for wrk in wb.sheets:
#     print(wrk)

# wb.sheets('TEST3').delete()

# # particular work sheets
# ws = wb.sheets['TEST2']
# ws.activate()
# print(ws.name)
# print(ws.cells)
# print(ws.index)

# # rename worksheet
# wb.sheets['TEST1'].name = 'First_WSH'

# # hide & unhide
# wb.sheets['Bangla'].api.Visible = False         # hide
# wb.sheets['Math'].api.Visible = False         # hide

# sheet_names = ['Bangla', 'Math']
# for name in sheet_names:
#     wb.sheets[name].api.Visible = True

# # how to select multiple work sheet
# wb.sheets[['Bangla', 'Math']].select()

# # copy a sheet
# # wb.sheets['Math'].copy()
# wb.sheets['Math'].copy(after=wb.sheets['Math'], name='Math Copied')

# # move particularly or in existing sheet
# # wb.sheets['Bangla'].api.Move(After= wb.sheets['sheet1'].api)
# wb.sheets['Bangla'].api.Move(None, After= wb.sheets['sheet1'].api)

# # wb.sheets['Math'].api.Protect("abc")
# # wb.sheets['Math'].api.Unprotect("abc")

