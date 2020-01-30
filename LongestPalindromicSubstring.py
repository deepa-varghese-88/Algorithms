#Longest Palindromic Substring
import string
import random
import datetime
import matplotlib.pyplot as plt

# ----------------Brute Force: O(n3)------------#

def brute(Input):
    LongestPalindromicBrute = ""
    if not Input:
        return ""

    n = len(Input)
    for left in range(0, n):
        for right in range(left + 1, n + 1):
            substr = Input[left:right]
            IsPalindrome = True
            for i in range(0, int(len(substr)/2)):
                 if substr[i] != substr[len(substr) - i - 1]:
                     IsPalindrome = False
            if IsPalindrome and len(substr) > len(LongestPalindromicBrute):
                LongestPalindromicBrute = substr
    return LongestPalindromicBrute

# ----------Dynamic Programming: O(n2)------------#
def dynamic(Input):
    if not Input:
        return ""

    # A 2D array to act as memo, size is len(s) * len(s)
    dp = [[False] * len(Input) for _ in range(len(Input))]

    # 2. initial lps related char index
    lpsStartIndex = 0
    lpsEndIndex = 0

    for i in range(len(Input)):
        start = i
        end = i
        while start >= 0:
            # For singleton charater substrings
            if start == end:
                dp[start][end] = True
            # For substrings of length in multiples of 2
            elif start + 1 == end:
                dp[start][end] = Input[start] == Input[end]
            # For substring of length in odd number
            else:
                dp[start][end] = dp[start + 1][end - 1] and (Input[start] == Input[end])

            # if dp[start][end] is palidromic, check is it longer than current solution
            if dp[start][end] and (end - start + 1) > (lpsEndIndex - lpsStartIndex + 1):
                lpsStartIndex = start
                lpsEndIndex = end

            start = start - 1
    return Input[lpsStartIndex:lpsEndIndex + 1]

# -------------Manacher's Algorithm: O(n)----------------#
def manacher(Input):
    LongestPalindromicMan = ""
    if not Input:
        return ""

    temp = '#' + '#'.join(Input) + '#'
    n = len(temp)
    RL = [0] * n
    maxLen = 0
    maxRight = 0
    pos = 0
    for i in range(n):
        RL[i] = min(maxRight - i, RL[pos * 2 - i]) if i < maxRight else 1
        while i >= RL[i] and i + RL[i] < len(temp) and temp[i + RL[i]] == temp[i - RL[i]]:
            RL[i] += 1
        if i + RL[i] - 1 > maxRight:
            maxRight = i + RL[i] - 1
            pos = i
        if RL[i] > maxLen:
            maxLen = RL[i]
            LongestPalindromicMan = Input[int((i + 1 - maxLen) / 2): int((i - 1 + maxLen) / 2)]
    return LongestPalindromicMan


def runningFunctions(Input):
    # Brute Force
    try:
        print("Brute Force's Output:")
        startTime = datetime.datetime.now()
        print(brute(Input))
        finishTime = datetime.datetime.now()
        BF_Time.append((finishTime - startTime).microseconds)
    except:
        BF_Time.append(-1)
        pass

    # Dynamic Programming
    try:
        print("Dynamic Programming's Output:")
        startTime = datetime.datetime.now()
        print(dynamic(Input))
        finishTime = datetime.datetime.now()
        DP_Time.append((finishTime - startTime).microseconds)
    except:
        DP_Time.append(-1)
        pass

    # Manacher's Algorithm
    try:
        print("Manacher's Algorithm's Output:")
        startTime = datetime.datetime.now()
        print(manacher(Input))
        finishTime = datetime.datetime.now()
        MA_Time.append((finishTime - startTime).microseconds)
    except:
        MA_Time.append(-1)
        pass


# ---------------------Input-----------------------#
def varyingPalindromeSize():

    #Set the InputSize that is supposed to be constant during the function run
    InputSize = 1024

    PalindromeSize = 1
    while PalindromeSize <= InputSize:
        Input_Size.append(PalindromeSize)

        #Create the list of inputs: Input
        PalindromeInput = ''.join(random.choice(string.ascii_lowercase) for i in range(int(PalindromeSize / 2)))
        if (PalindromeSize % 2 != 0):
            Palindrome = PalindromeInput + 'z' + PalindromeInput[::-1]
        else:
            Palindrome = PalindromeInput + PalindromeInput[::-1]
        Input = Palindrome + ''.join(random.choice(string.ascii_uppercase) for i in range(InputSize - PalindromeSize))
        print("Input: ")
        print(Input)

        runningFunctions(Input)

        PalindromeSize += 1

def varyingPalindromeSizeCSV():
    varyingPalindromef = open("VaryingPalindromOutput.csv", "w+")
    varyingPalindromef.write("InputSize, BF_TIME, DP_TIME, MA_TIME\n")
    for i in range(len(Input_Size)):
        varyingPalindromef.write(str(Input_Size[i]) + ' , ' + str(BF_Time[i]) + ' , ' + str(DP_Time[i]) + ' , ' + str(MA_Time[i]) + '\n')
    varyingPalindromef.close()

def varyingInputSize():

    #Add values to array InputValues for the different types of inputs the function is supposed to run for
    InputValues = [16]#[16, 256, 1024, 4096, 8192, 16384]
    #Specify the percentage of the input that should be a palindrome
    PalindromeCurrentSize = 25 #% 50% #100%

    for InputSize in InputValues:
        PalindromeSize = int(((PalindromeCurrentSize/100)*InputSize))
        PalindromeInput = ''.join(random.choice(string.ascii_lowercase) for i in range(int(PalindromeSize/2)))
        if (PalindromeSize % 2 != 0):
            Palindrome = PalindromeInput + 'z' + PalindromeInput[::-1]
        else:
            Palindrome = PalindromeInput + PalindromeInput[::-1]
        Input = Palindrome + ''.join(random.choice(string.ascii_uppercase) for i in range(InputSize - PalindromeSize))
        print("Input: ")
        print(Input)
        for count in range(10):
            Input_Size.append(InputSize)
            runningFunctions(Input)

def varyingInputSizeCSV():
    varyingInputf = open("VaryingInputOutput.csv", "w+")
    varyingInputf.write("InputSize, BF_TIME, DP_TIME, MA_TIME\n")
    for i in range(len(Input_Size)):
        varyingInputf.write(str(Input_Size[i]) + ' , ' + str(BF_Time[i]) + ' , ' + str(DP_Time[i]) + ' , ' + str(MA_Time[i]) + '\n')
    varyingInputf.close()

def varyingSingleDimPlot():
    print(Input_Size)
    print(BF_Time)
    print(DP_Time)
    print(MA_Time)
    plt.plot(Input_Size, BF_Time, color='blue', label='BruteForce')
    plt.plot(Input_Size, DP_Time, color='olive', label='DynamicProgramming')
    plt.plot(Input_Size, MA_Time, color='orange', label='ManachersAlgorithm')
    plt.legend()
    plt.tight_layout()
    plt.show()

# ----------------------MAIN-----------------------#

#For the two cases of Inputs being provided (given below), uncomment the appropriate lines of code
#	Case 1: Varying Input size, with fixed palindrome size: uncomment 198 - 202, comment 204 - 208
#		The required changes, specific input sizes, and the constant palindrome size can be made in the function's block
#	Case 2: Varying Palindrome size, with fixed input size: uncomment 204 - 208, comment 198 - 202
#		The required changes to the input size can be made in the function's block

BF_Time = []
DP_Time = []
MA_Time = []
Input_Size = []

#The 3 functions, with constant InputSize and varying PalindromeSize from 1 to InputSize
varyingPalindromeSize() #NOTE: Set the desired InputSize inside the function
#NOTE: comment below two lines if plot is not required
varyingSingleDimPlot()
varyingPalindromeSizeCSV()

# #The 3 functions, with varying InputSize and three options for PalindromSize = 0% 50% 100% of the InputSize
# varyingInputSize() #NOTE: Set the desired varying Input size values inside the function
# #NOTE: comment below two lines if plot is not required
# varyingSingleDimPlot()
# varyingInputSizeCSV()