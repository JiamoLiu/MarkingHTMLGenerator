comments = {
    "1a":{
        "1":"Failed to indicate circuit-switched is more suitable.",
        "2":"Failed to indicate that bandwidth can be reserved without much wastage due to predictable bandwidth requirement.",
        "3":"Failed to indicate the cost of connection set-up and teardown is amortized over the long session."
    },
    "1b":{
        "1":"Failed to indicate that no congestion control is required.",
        "2":"Failed to indicate that link is able to handle the traffic even though all applications are transmitting simultaneously."
    }
}


def print_question_comments(question_number):
    if (question_number not in comments):
        return
    
    keys = comments[question_number].keys()
    for key in keys:
        print("{}. {}".format(key,comments[question_number][key]))

def get_question_comments_html(question_number, input_comments):
    if (question_number not in comments):
        return input_comments
    indexes = input_comments.split(",")
    res = ""
    for index in indexes:
        res = res + "{}. {}<br>".format(index,comments[question_number][index])
    return res
