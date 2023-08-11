# program_string 을 딕셔너리 형태로 바꿈
def program_str_to_dict(text):
    elements = text.split('), (')
    result = {}
    for element in elements:
        key, value = element.replace('(', '').replace(')', '').split(' : ')
        result[key] = value
    return result