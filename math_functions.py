def mm_kor(socomo_props, a_value, kdsi, b_value):
    result = 1
    for x in socomo_props:
        result *= x
    result = (result*a_value) * (kdsi**b_value)
    print(result)
    return result

list_of_integers = [1.15, 1.06, 1.13, 1.17]
## example mm_kor
mmkor = mm_kor(list_of_integers, 3.2, 3.0, 1.05)
#print(list_of_integers[0], "soy el valor")
##



def t_dev(mm_kor_result, c_value):
    STANDARD = 2.5
    return STANDARD*mm_kor_result**c_value
##example t_dev
tdev = t_dev(mmkor, 0.38)
#print(tdev)



##example team members
def team_members(mmkor, tdev):
    return mmkor / tdev
#print (team_members(mmkor,tdev))
