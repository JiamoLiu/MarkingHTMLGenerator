def generate_html(marks_data,title = ["Question", "Points deducted", "Comments"]):
    questions = list(marks_data.keys())
    res = "<p>Marker: {} <br> Student name: {} </p>\n".format(marker,student_name) + "<table style=\"width:100%\">\n" + 1*"\t" + "<tbody>\n"
    subtotal_deduction = 0
    #add heading
    res = res + "\t\t<{}>\n".format(table_row_tag)
    res = res+add_row(title[0],3,table_heading_tag)
    res = res+add_row(title[1],3,table_heading_tag)
    res = res+add_row(title[2],3,table_heading_tag) 
    res = res + "\t\t</{}>\n".format(table_row_tag)
    
    for question in questions:
        data_row = marks_data[question]
        res = res + "\t\t<{}>\n".format(table_row_tag)
        subtotal_deduction = subtotal_deduction + int(data_row[1])
        res = res+add_row(data_row[0],3,table_body_tag) + add_row(data_row[1],3,table_body_tag) + add_row(data_row[2],3,table_body_tag)
        res = res + "\t\t</{}>\n".format(table_row_tag)

    res = res + "\t" + "</tbody>\n"
    res = res +"</table>\n"
    res = res + "<subtotal>Subtotal deduction: {}</subtotal>\n".format(str(subtotal_deduction))

    return res

def add_row(data, numberoftabs, table_row_tag):
    return  numberoftabs * "\t"+"<{}>".format(table_row_tag) + str(data) + "</{}>\n".format(table_row_tag)





debug =False
table_heading_tag = "th"
table_body_tag = "td"
table_row_tag = "tr"
marker = "Jiamo Liu"
questions = "1a,1b,2a,2b,2c,2d,2e,2f,2g,3a,3b,4".split(",")
student_name = ""

if (debug == False):
    student_name = input("What is the student's name?\n")
else:
    student_name = "abc"

marks_data = {}

for question in questions:
    print("Marking question: {}\n".format(question))
    lost_points = input("How many points did he lose? Press enter to skip to next question.\n")
    comments = ""
    if (lost_points == ""):
        marks_data[question] = [question, 0, "None"]
        continue
    if (lost_points != ""):
        comments = input("What are your comments?\n")
    marks_data[question] = [question, lost_points, comments]


print(generate_html(marks_data))
#question_list = questions.split(",")

