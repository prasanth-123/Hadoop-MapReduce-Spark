
import sys

curr_key = None
curr_val = 0
key = None

# input comes from STDIN
for key_val in sys.stdin:
    key_val = key_val.strip()


    key, str_val = key_val.split('\t', 1)

    # convert str_val (currently a string) to int
    try:
        str_val = int(str_val)
    except ValueError:
        
        continue


    if curr_key == key:
        curr_val += str_val
    else:
        if curr_key:
            # write result to STDOUT
            print '%s\t%s' % (curr_key, curr_val)
        curr_val = str_val
        curr_key = key

# do not forget to output the last key if needed!
if curr_key == key:
    print '%s\t%s' % (curr_key, curr_val)





