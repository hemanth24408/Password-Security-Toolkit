import zxcvbn as z

result={}
def password_strength(word):
    global result
    result=z.zxcvbn(word)
def attempts():
    return result["guesses"]
def pattern():
    if result["sequence"]:
        return result["sequence"][0]["pattern"]
    return "No pattern detected"
def cracking_time_online():
    return result["crack_times_display"]["online_throttling_100_per_hour"]
def cracking_time_offline():
    return result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
def score():
    if result["score"]==0:
        return "Very Weak"
    elif result["score"]==1:
        return "Weak"
    elif result["score"]==2:
        return "Fair"
    elif result["score"]==3:
        return "Strong"
    elif result["score"]==4:
        return "Very Strong"

def feedback_warning():
    return result["feedback"]["warning"] if result["feedback"]["warning"]!="" else "No Warning"
def feedback_suggestions():
    if result["feedback"]["suggestions"]:
        return result["feedback"]["suggestions"][0]
    else:
        return "No Suggestions"
def score1(word):
    return z.zxcvbn(word)["score"]