
import sys


def goof(s_old):
    s_new = ""
    should_be_upper = False
    for i in range( len(s_old) ):
        c = s_old[i]
        if should_be_upper and c != ' ':
            c = s_old[i].upper()
        if c != ' ':
            should_be_upper = not should_be_upper

        s_new = s_new + c

    return s_new

if __name__=="__main__":
    new_str = ""
    for j in range(1, len(sys.argv) ):
        new_str = new_str + sys.argv[j] + ' '
    
    print( new_str )
    print( goof(new_str) ) 


