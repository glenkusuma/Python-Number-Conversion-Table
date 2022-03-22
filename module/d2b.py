# Recursive function to calculate decimal to binary using division method
def d2b(num=int,binary=list(),quotient=list(),division=list()):
    if num == 0:
        return binary,quotient,division
    if num % 2 == 0:
        binary.append("0")
    else:
        binary.append("1")
    division.append(num)
    num //= 2
    quotient.append(num)
    d2b(num,binary,quotient,division)
    return binary,quotient,division

# Helper function to print decimal to binary table
def print_d2b(num,binary,quotient,division):
    rown1 = 'Divison by 2'
    rown2 = 'Quotient'
    rown3 = 'Remainder'
    rown4 = '#'
    if len(str(division[0]))+2 <= len(rown1):
        row1 = len(rown1)
    else:
        row1 = len(str(division[0]))+2
    if len(str(quotient[0])) <= len(rown2):
        row2 = len(rown2)
    else:
        row2 = len(str(quotient[0]))+1
    row3 = len(rown3)
    row4 = len(str(len(binary)))
    table_cap = f"+-{''.center(row1,'-')}-+-{''.center(row2,'-')}-+-{''.center(row3,'-')}-+-{''.center(row4,'-')}-+"
    print(f"Decimal to Binary")
    print(table_cap)
    print(f"| {rown1.ljust(row1)} | {rown2.ljust(row2)} | {rown3.ljust(row3)} | {rown4.ljust(row4)} |")
    print(table_cap)
    for i in range(0,len(binary)):
        print(f"| {(f'{str(division[i])}/2').ljust(row1)} | {str(quotient[i]).ljust(row2)} | {str(binary[i]).ljust(row3)} | {str(i).ljust(row4)} |")
    binary.reverse()
    print(table_cap)
    print(f"Decimal : {num}\nBinary  : {''.join(binary)}")

# Wraper function decimal to binary
def decimal_to_binary(decimal=int):
    binary,quotient,division = d2b(decimal)
    print_d2b(decimal,binary,quotient,division)

if __name__ == "__main__":
    decimal_to_binary(69420)