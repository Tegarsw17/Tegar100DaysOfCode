def palindrome(nums):
    # First Attempt
    # try:
    #     # change to string and then we reverse and then make it to integer
    #     to_reverse = int(str(nums)[::-1])
    #     return nums == to_reverse
    # except:
    #     # if number is negative absolutely False
    #     return False
    # -----------------------------------------
    # Second Attempt
    # # if number is negative absolutely False
    # if nums < 0:
    #     return False
    # else:
    #     # change to string and then we reverse and then make it to integer
    #     to_reverse = int(str(nums)[::-1])
    #     return nums == to_reverse
    # -----------------------------------------
    # Final Attempt
    # check the number is not negative
    # or check the number if modulus with ten not equal to 0 except zero it self
    if nums < 0 or nums % 10 == 0 and nums != 0:
        return False
    # make sure half(front and back) of number is same
    revnum = 0
    while revnum < nums:
        revnum = revnum * 10 + nums % 10
        nums //= 10
    #and if lenght of number its odd we remove th last number
    return nums == revnum or nums == revnum // 10
