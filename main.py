import numpy as np
from time import time

def evaluate_formula(P, PL, W, L, R, S):
    if not P:
        return 0
    
    terms = [
        # Add or remove your terms here, code will dynamically update the formula
        1 / (1 + np.exp(-((W - L) / P))),
        (R / 100) + 1,
        (S / 10) + 1,
        (P - L) / P,
        1 / (1 + np.exp(PL / P)),
    ]
    
    score = 1
    for term in terms:
        score *= term
    return score



def insert_dash_row(output_file, width=110):
    print(f"\n{'-' * width}")
    output_file.write(f"\n{'-' * width}\n")

O = (2, 5, 0, 1, 3, 4) # This specifies the column order in output table, the numbers are the indices in 'input_ranges' list (starting zero)
param_column_width = (10, 10, 10, 10, 10, 10)  # this is output table column size; set this values as the near-maximum digits of the value might have. 
# Mistaking in this width values will f with table shape 
index_width = 10
score_width = '.10f'

if __name__ == '__main__':
    print("Enter ranges separated by space/tab/whatever.")
    outputfilename = input('Enter output filename: ')
    outfile = open(f'{outputfilename}.txt', 'w')
    if not outfile:
        print('File open failure mean that app can not save results in file, but still you can see results in this terminal.\n')
    input_ranges = []
    params = ('W', 'L', 'P', 'R', 'S', 'PL',)
    for idx, param in enumerate(params):
        inp = input(f'{param}_i, {param}_f = ').split()
        _i, _f = [int(num or 0) for num in (inp if len(inp) > 1 else (inp[0], inp[0],))]
        input_ranges.append((_i, _f))
        outfile.write(f"{param}: {input_ranges[idx][0]} -> {input_ranges[idx][1]}\tOR\t[{input_ranges[idx][0]}, {input_ranges[idx][1]}]\n" \
            if input_ranges[idx][0] != input_ranges[idx][1] else f"{param} = {input_ranges[idx][0]}\n") # used input_ranges list to print ranges in file, in order to chekck it everything is appended OK
    
    #calculating compute time
    start_time = time()    
    # printing headers of output table
    print(f"{'#':{index_width}}", end='')
    outfile.write(f"\n{'#':{index_width}}")
    
    for p_i in O:
        print(f" | {params[p_i]:{param_column_width[p_i]}}", end='')
        outfile.write(f" | {params[p_i]:{param_column_width[p_i]}}")
    
    print(" | Score", end='')
    outfile.write(" | Score")
            
    insert_dash_row(outfile)
    # TODO: 
    # Find a way to reduce order of algorithm, Possible Approaches:
    # 1. Construct all rows (all n inputs for putting inside formula) , one by one, exactly insider ranges
    row_idx = 1
    for p0 in range(input_ranges[O[0]][0], input_ranges[O[0]][1] + 1):
        for p1 in range(input_ranges[O[1]][0], input_ranges[O[1]][1] + 1):
            for p2 in range(input_ranges[O[2]][0], input_ranges[O[2]][1] + 1):
                for p3 in range(input_ranges[O[3]][0], input_ranges[O[3]][1] + 1):
                    for p4 in range(input_ranges[O[4]][0], input_ranges[O[4]][1] + 1):
                        for p5 in range(input_ranges[O[5]][0], input_ranges[O[5]][1] + 1):
                            print(f"{row_idx:{index_width}} | {' ' + str(p0) + ' ':{param_column_width[0]}}", end='')
                            outfile.write(f"{row_idx:{index_width}} | {' ' + str(p0) + ' ':{param_column_width[0]}}")

                            print(f" | {' ' + str(p1) + ' ':{param_column_width[1]}}", end='')
                            outfile.write(f" | {' ' + str(p1) + ' ':{param_column_width[1]}}")
                            
                            print(f" | {' ' + str(p2) + ' ':{param_column_width[2]}}", end='')
                            outfile.write(f" | {' ' + str(p2) + ' ':{param_column_width[2]}}")
                            
                            print(f" | {' ' + str(p3) + ' ':{param_column_width[3]}}", end='')
                            outfile.write(f" | {' ' + str(p3) + ' ':{param_column_width[3]}}")
                            
                            print(f" | {' ' + str(p4) + ' ':{param_column_width[4]}}", end='')
                            outfile.write(f" | {' ' + str(p4) + ' ':{param_column_width[4]}}")
                            
                            print(f" | {' ' + str(p5) + ' ':{param_column_width[5]}}", end='')
                            outfile.write(f" | {' ' + str(p5) + ' ':{param_column_width[5]}}")
                            
                            f_out = evaluate_formula(p0, p1, p2, p3, p4, p5)
                            print(f"| {f_out:{score_width}}", end='')
                            outfile.write(f"| {f_out:{score_width}}")
                            
                            insert_dash_row(outfile)
                            row_idx += 1
       
    time_elapsed = time() - start_time
    print(f"\nTime Elasped: {time_elapsed:.2f} secs.")
    outfile.write(f"\nTime Elasped: {time_elapsed:.2f} secs.")
    
    outfile.close()