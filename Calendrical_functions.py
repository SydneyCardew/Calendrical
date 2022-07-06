import os
from Calendrical_Classes import Year


def header():
    return f'''<!DOCTYPE html>
<html>
<head>
<style>
tr, th, table{{
table-layout: fixed;
border: 1px solid;
border-collapse: collapse;
empty-cells: show;
max-width: 70%;
text-align: center;
vertical-align: middle;
padding: 5px;
margin-left: auto;
margin-right: auto;
}}
td{{
border:1px solid;
border-collapse: collapse;
width:4.17%;
overflow: hidden;
padding:5px;
}}
.over-table{{
border:none;
border-collapse: collapse;
}}
.grey-cell{{
background-color: LightGrey;
}}
.month-title{{
background-color: PaleGreen;
font-family: Arial, sans-serif;
font-weight: bold;
font-size: 20px;
padding-top: 2px;
padding-bottom: 2px;
}}
.saturday-column{{
background-color: LightGoldenRodYellow;
}}
.sunday-column{{
background-color: LightSalmon;
}}
.title-year{{
font-size: 80px;
font-family: Arial, sans-serif;
text-align: left;
}}
.big-table{{
bottom-margin: 10px;
}}
</style>
</head>
<body>
'''


def calendar(year):
    feed_year = Year(year)
    c_arr = []
    name_array = []
    for month in feed_year.months:
        c_arr.extend(month.calendar_array)
        name_array.append(month.name)
    calendar_string = f'''<div class="big-table">
<table>
<tr>
    <th colspan="24" class="title-year">{feed_year.year}</th>
</tr>
    '''
    m = 1  # month counter
    c = 0  # cell counter
    big_offset = 0
    for month_rows in range(1, 5):
        calendar_string += f'''<tr>
 <td colspan="8" class="month-title">{name_array[m]}</td>
 <td colspan="8" class="month-title">{name_array[m + 1]}</td>
 <td colspan="8" class="month-title">{name_array[m + 2]}</td>
</tr>

<tr>
        '''
        m += 3
        calendar_string += f''' <td class="grey-cell">wk</td>
    <td class="grey-cell">Mo</td>
    <td class="grey-cell">Tu</td>
    <td class="grey-cell">We</td>
    <td class="grey-cell">Th</td>
    <td class="grey-cell">Fr</td>
    <td class="saturday-column">Sa</td>
    <td class="sunday-column">Su</td>
        ''' * 3
        calendar_string += f'''</tr>'''
        for cell_rows in range(0, 6):
            i = ((cell_rows) * 8) + big_offset
            calendar_string += f'''<tr>
<td class="grey-cell">{str(c_arr[i]).zfill(2)}</td>
    <td>{c_arr[i + 1]}</td>
    <td>{c_arr[i + 2]}</td>
    <td>{c_arr[i + 3]}</td>
    <td>{c_arr[i + 4]}</td>
    <td>{c_arr[i + 5]}</td>
    <td class="saturday-column">{c_arr[i + 6]}</td>
    <td class="sunday-column">{c_arr[i + 7]}</td>
    <td class="grey-cell">{str(c_arr[i + 48]).zfill(2)}</td>
    <td>{c_arr[i + 49]}</td>
    <td>{c_arr[i + 50]}</td>
    <td>{c_arr[i + 51]}</td>
    <td>{c_arr[i + 52]}</td>
    <td>{c_arr[i + 53]}</td>
    <td class="saturday-column">{c_arr[i + 54]}</td>
    <td class="sunday-column">{c_arr[i + 55]}</td>
    <td class="grey-cell">{str(c_arr[i + 96]).zfill(2)}</td>
    <td>{c_arr[i + 97]}</td>
    <td>{c_arr[i + 98]}</td>
    <td>{c_arr[i + 99]}</td>
    <td>{c_arr[i + 100]}</td>
    <td>{c_arr[i + 101]}</td>
    <td class="saturday-column">{c_arr[i + 102]}</td>
    <td class="sunday-column">{c_arr[i + 103]}</td>
</tr>
            '''
            c += 8
        big_offset += 144
    calendar_string += '''
    </table>
    </div>'''
    return calendar_string


def footer():
    return '''
    </body>
    </html>
    '''


def html_writer(year_array, file_name):
    output_path = os.getcwd() + '\\Output\\'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    file_name = f"{file_name}.html"
    with open(output_path + file_name, 'w') as test_file:
        test_file.write(header())
        for year in year_array:
            test_file.write(calendar(year))
        test_file.write(footer())
