    

# faster
def romanToInt1(s: str) -> int:
    roman_dict = {'I': 1,'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
            integer_value += roman_dict[s[i]] - 2*roman_dict[s[i-1]]
        else:
            integer_value += roman_dict[s[i]]
    return integer_value


def romanToInt2(s: str): 
    keys ={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    val = 0
    for k,v in keys.items():
        if len(s)>0:
            occr = s.count(k)
            if occr>0:
                val = val + (v*occr)
                s = s.replace(k,'')
                print(k)
                print(v*occr)
    return val
