def find_match(string_list, wanted):
    wanted_list = []
    for string in string_list:
        stringCheck = string.lower()
        wanted = wanted.lower()
        if stringCheck.startswith(wanted):
            wanted_list.append(string)

    if wanted_list:
        return wanted_list
    else:
        return None


lugares = ["Ri Happy - Boa Viagem", "Ri Happy - Cordeiro", "Planeta brinquedo"]

string = "Ri"

print(find_match(lugares, string))
