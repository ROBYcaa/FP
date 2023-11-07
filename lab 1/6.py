def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product

nums = [2, 3, 4, 5, 6, 10000000, 10]

result = prod(nums)

rez = 0
while result != 0:
    if result % 10 == 0:
        rez += 1
    result = result / 10
print(rez)

# def isprime(vector)
# vector = [2, 3, 4, 5, 6, 10000000, 10]

def primenumber(num):
  n = 0
  i = 2
  for i in range(2, (num//2)+1):
    if num % i == 0:
      n = n + 1
  if n == 0:
      return True

def longest_sequence(nums):

    sequence = [nums[0]]
    longest_seq = [nums[0]]

    for i in range(1, len(nums)):
        if primenumber(nums[i] + nums[i - 1]):
            sequence.append(nums[i])
        else:
            sequence = [nums[i]]

        if len(sequence) > len(longest_seq):
            longest_seq = sequence

    return longest_seq

nums = [1, 2, 3, 4, 1, 5, 6, 8]
print(longest_sequence(nums))