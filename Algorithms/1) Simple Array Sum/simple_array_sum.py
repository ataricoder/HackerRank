
def simpleArraySum(ar):
    #
    # Write your code here.
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum
    #


def main():

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)


main()
