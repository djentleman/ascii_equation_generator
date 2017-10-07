# -*- encoding=utf-8 -*-


def mk_sigma(bottom, top, sequence):
    return ' '*(3-(len(top)/2))+top+'\n \\‾‾‾\n  \\\n   |  ' + sequence + '\n  /\n /___\n' + ' '*(3-(len(bottom)/2))+bottom

def check_bracket_weight_valid(instr, bracket_type='()'):
    if bracket_type == '()':
        start_token = '('
        end_token = ')'
    elif bracket_type == '{}':
        start_token = '{'
        end_token = '}'
    elif bracket_type == '[]':
        start_token = '['
        end_token = ']'
    else:
        return False #invalid bracket type
    weight = 0
    for char in instr:
        if char == start_token:
            weight +=1
        elif char == end_token:
            if weight > 0:
                weight -= 1
            else:
                return False
    return weight == 0

def handle_division(instr):
    segments = instr.split('/')
    divisor_size = max([len(s) for s in segments])
    # add padding to segments
    segments = map(lambda x: ' '*((divisor_size/2)-(len(x)/2)) + x, segments)
    return ('\n'+('-'*divisor_size)+'\n').join(segments)

def handle_sum_operator(instr):
    sums = instr.split('\\sum')
    result  = sums[0]
    for sum_section in sums[1:]:
        # verify valid
        if check_bracket_weight_valid(sum_section, bracket_type='{}') and len([c for c in sum_section if c == '{']) == 3:
            bottom = sum_section.split('{')[1].split('}')[0]
            top = sum_section.split('{')[2].split('}')[0]
            sequence = sum_section.split('{')[3].split('}')[0]
            sigma = mk_sigma(bottom, top, sequence)
            result += sigma
        else:
            print 'invalid brackets!'
            print sum_section
            return ''
        
    return result

def handle_bracketless_string(instr):
    # brackets needs to be handled outside of this - as their size varies based on
    # the output of their contents
    result = instr

    # handle division
    result = handle_division(result)
    # handle the sum operator
    if '\\sum' in result:
        result = handle_sum_operator(result)
    return result

def handle_string(instr):
    return handle_bracketless_string(instr)

def main():
    print handle_string('2x*y/z')
    print handle_string('5/\\sum{i=0}{5}{2x}')
    #print handle_string('\\sum{i=0}{5}{2x}{}')
    #print handle_string('\\sum{i=0}{5}2x}{}')
     

if __name__ == '__main__':
    main()
