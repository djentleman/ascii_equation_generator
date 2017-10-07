

def handle_division(instr):
    segments = instr.split('/')
    divisor_size = max([len(s) for s in segments])
    # add padding to segments
    segments = map(lambda x: ' '*((divisor_size/2)-(len(x)/2)) + x, segments)
    return ('\n'+('-'*divisor_size)+'\n').join(segments)


def handle_bracketless_string(instr):
    # brackets needs to be handled outside of this - as their size varies based on
    # the output of their contents
    # handle division
    result = handle_division(instr)
    return result

def handle_string(instr):
    return handle_bracketless_string(instr)

def main():
    print handle_string('2x*y/z')
     

if __name__ == '__main__':
    main()
