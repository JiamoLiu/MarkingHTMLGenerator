comments = {
    "1a":{
        "1":"Failed to indicate circuit-switched is more suitable.",
        "2":"Failed to indicate that bandwidth can be reserved without much wastage due to predictable bandwidth requirement.",
        "3":"Failed to indicate the cost of connection set-up and teardown is amortized over the long session."
    },
    "1b":{
        "1":"Failed to indicate that no congestion control is required.",
        "2":"Failed to indicate that link is able to handle the traffic even though all applications are transmitting simultaneously."
    },
    "2a":{
        "1": "Answer should be: m/s seconds"
    },
    "2b":{
        "1": "Answer should be: L/R seconds"
    },
    "2c":{
        "1": "Answer should be: m/s + L/R seconds"
    },
    "2d":{
        "1": "Answer: The bit is just leaving Host A"
    },
    "2e":{
        "1": "Answer: The first bit is in the link and has not reached Host B"
    },
    "2f":{
        "1":"Answer: The first bit has reached Host B"
    },
    "2g":{
        "1":"Answer: m = sL/R = 893KM"
    },
    "3a":{
        "1":"Answer: d = L/R_1 + L/R_2 + d_1/s_1 + d_2/s_2 + d_proc"
    },
    "3b":{
        "1":"Answer: Plug into the equation to get: 8 + 8 +16 +4 +1 = 37 msec"
    },
    "4":{
        "1":"Answer: d = L/R + d_1/s_1 + d_2/s_2, 8+16+4 = 28 msec"
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
        if index not in comments[question_number]:
            return input_comments
        res = res + "{}. {}<br>".format(index,comments[question_number][index])
    return res
