def nested_list(list):
    result=0
    for item in list:
        if type(item)==type([]):
            result=result+nested_list(item)
        else:
            result=result+item
    return result

print(nested_list([1,2,3,[4,5],6,7,8,9,105]))