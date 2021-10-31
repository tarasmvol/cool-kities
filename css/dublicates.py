import re
def pretty_message(s):
    k = re.split("\s", s)
    final_string = []
    for i in k:
        check_3=re.sub(r'$(...)\1+', r'\1', i)
        check_2=re.sub(r'$(..)\1+', r'\1', check_3)
        check_1=re.sub(r'$(.)\1+', r'\1', check_2)
        final_string.append(check_1)
    final_string=" ".join(final_string)
    return(print (final_string))

pretty_message("In to the woods")
pretty_message("Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss")


