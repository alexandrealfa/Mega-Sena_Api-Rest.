def compare_string(number_result, number_choice):
    number_ms =  number_result.replace(',', ' ').split()
    number_user = number_choice.replace(',', ' ').split()
    value2 = [int(value) for value in number_ms]
    value1 = [int(value) for value in number_user]
    result = [current_value for current_value in value1 if current_value in value2]
    if len(result) == 0:
        return "you didn't hit any numbers"
    return str(result).replace('[', "").replace(']', "")