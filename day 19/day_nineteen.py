class Solution:
    def __init__(self):
        self.push = []
        self.enqueue = []

    def pushCharacter(self, character):
        push_c = str(character)
        self.push.append(push_c)
        return self.push

    def enqueueCharacter(self, character):
        enqueue_c = str(character)
        self.enqueue.append(enqueue_c)
        return self.enqueue

    def dequeueCharacter(self):
        dequeue = reversed(self.enqueue)
        dequeue_s = ''.join(dequeue)
        return str(dequeue_s)

    def popCharacter(self):
        pop = self.push
        pop_s = ''.join(pop)
        return str(pop_s)

# Write your code here

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():

        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
