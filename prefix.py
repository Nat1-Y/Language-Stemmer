prefixes_set = ['እንደ', 'እስኪ', 'በየ', 'ከነ', 'ያለ', 'እነ', 'ስለ', 'ለ', 'ከ', 'የ', 'በ' , 'ላል']

def prefix(input):
    for prefix in prefixes_set:
        if input.startswith(prefix):
            input = input.removeprefix(prefix)
            return input
        