def question_1(name):
    return "Hello my name is " + name

def question_2(name):
    return "Hello my name is " + name.capitalize()

def question_3(name):
    return "My first name is " + name

def question_4(name):
    return "My first name is " + name.capitalize()

def question_5(first_name, last_name):
    return "My full name is " + first_name + " " + last_name

def question_6(first_name, last_name):
    return "My full name is " + first_name.capitalize() + " " + last_name.capitalize()

def question_7(str):
    return [idx for idx in range(len(str)) if str[idx].islower()]

def question_8(str):
    return [idx for idx in range(len(str)) if str[idx].isupper()]

def question_9(str):
    return [idx for idx in range(len(str)) if str[idx].isspace()]

def question_10(str):
    word_list = str.split(" ")
    return len(word_list)

def question_11(str):
    word_int = [idx for idx in range(len(str)) if str[idx].isnumeric()]
    return len(word_int)

def question_12(str1, str2):
    return str1 + " " + str2

def question_13(str1, str2):
    return str1.capitalize() + " " + str2.capitalize()

def question_14(str):
    return str.replace(" ", "_")

def question_15(list):
    return max(list, key = len)

def question_16(list):
    return min(listing, key = len)

def question_17(list):
    return len(''.join(list)) / len(list)

def question_18(list):
    import statistics 
    list_len = []
    for i in range(0, len(list)):
        len_word = len(list[i])
        list_len.append(len_word)
    return statistics.median(list_len)

def question_19(list):
    listing_even = []
    for i in list:
        if i % 2 == 0:
            listing_even.append(i)
        else:
            pass
    return listing_even

def question_20(list):
    listing_odd = []
    for i in list:
        if i % 2 == 1:
            listing_odd.append(i)
        else:
            pass
    return listing_odd

def question_21(list):
    list.sort()
    return list[-3:]

def question_22(list):
    list.sort()
    return list[0:3]

def question_23(list):
    return sum(list) / len(list)

def question_24(list):
    from statistics import mode
    return mode(list)

def question_25(list):
    list.reverse()
    return list

def question_26(list):
    cum_listing = []
    x = 0
    for i in range(0, len(list)):
        x += list[i]
        cum_listing.append(x)
    return cum_listing

def question_27(list):
    diff_listing = []
    x = 0
    for i in range(0, len(list)-1):
        x = abs(list[i] - list[i+1])
        diff_listing.append(x)
    return diff_listing

def question_28(n):
    F=[0, 1, 1]
    for i in range(3, n):
        result = F[i-1] + F[i-3]
        F.append(result)
    return F

def question_29(n):
    F = [1, 2]
    for i in range(2, n):
        result = 1
        for j in F:
            result *= j
        F.append(result)
    return F

def question_30(n):
    F = []
    for i in range (0, n):
        listing = []
        for x in range (1, i+1):
            listing.append(x)
        sum_listing = sum(listing)
        twotothepower = 2 ** sum_listing
        F.append(twotothepower)
    return F
