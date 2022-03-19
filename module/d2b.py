# recursive function to calculate decimal to binery using division method
def d2b(num=int,binery=list(),quotient=list(),division=list()):
    if num == 0:
        return binery,quotient,division
    if num % 2 == 0:
        binery.append("0")
    else:
        binery.append("1")
    division.append(num)
    num //= 2
    quotient.append(num)
    d2b(num,binery,quotient,division)
    return binery,quotient,division

# helper function to print decimal to binary table
def print_d2b(num,binery,quotient,division):
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
    row4 = len(str(len(binery)))
    print(f"Decimal to binery")
    print(f"{rown1.ljust(row1)} | {rown2.ljust(row2)} | {rown3.ljust(row3)} | {rown4.ljust(row4)}")
    for i in range(0,len(binery)):
        print(f"{(f'{str(division[i])}/2').ljust(row1)} | {str(quotient[i]).ljust(row2)} | {str(binery[i]).ljust(row3)} | {str(i).ljust(row4)}")
    binery.reverse()
    print(f"Decimal : {num}\nBinery  : {''.join(binery)}")

# wraper function decimal to binery
def decimal_to_binery(decimal=int):
    binery,quotient,division = d2b(decimal)
    print_d2b(decimal,binery,quotient,division)

if __name__ == "__main__":
    decimal_to_binery(69420)