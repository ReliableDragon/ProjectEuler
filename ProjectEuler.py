import math
import itertools

def pe33():
  fracs = []
  
  for i in range(1, 10):
    for j in range(0, 10):
      for k in range(1, i+1):
        for m in range(0, 10 if k < i else j):
          if not (k == m and i == j):
            originFrac = (10*k+m)/(10*i+j) 
            if i != 0 and k == j and originFrac == m/i:
              fracs.append(((10*k+m, 10*i+j), (m, i)))
            elif j != 0 and i == m and originFrac == k/j:
              fracs.append(((10*k+m, 10*i+j), (k, j)))

  return fracs

def pe34():
  nums = [3]
  total = 0
  for i in range(0, 2600000):
    factNum = 0
    realNum = 0
    for j in range(0, len(nums)):
      realNum += nums[j] * 10**j
      factNum += math.factorial(nums[j])
    if realNum == factNum:
      total += realNum
    carryNum = 0
    while nums[carryNum] == 9:
      nums[carryNum] = 0
      carryNum += 1
      if len(nums)-1 < carryNum:
        nums.append(0)
    nums[carryNum] += 1
  print(total)

def pe34Num():
  facts = {}
  total = 0
  for i in range(3, 2600000):
    factSum = 0
    tmp = i
    while tmp > 0:
      digit = tmp % 10
      if digit not in facts:
        facts[digit] = math.factorial(tmp % 10)
      factSum += facts[digit]
      tmp = tmp // 10
    if i == factSum:
      total += i
  print(total)

def isPrime(num):
  smallPrimes = [2, 3, 5, 7, 11] # 5, 7, and 11 are repeated.
  if num in smallPrimes:
    return True
  elif num < 11:
    return False
  
  for i in smallPrimes:
    if num % i == 0:
      return False
  for i in range(6, math.ceil(math.sqrt(num))+6, 6):
    if num % (i+1) == 0 or num % (i-1) == 0:
      return False
  return True

def numLength(num):
  return math.floor(math.log(num, 10)) + 1

def rotations(num):
  rots = [num]
  numLen = numLength(num)
  for i in range(0, numLen - 1):
    end = num % 10
    num //= 10
    num += end * 10 ** (numLen - 1)
    rots.append(num)
  return rots

def pe35(limit = 1000000):
  total = 0
  for i in range(2, limit):
    prime = True
    rots = rotations(i)
    for j in rots:
      if not isPrime(j):
        break
    else:
      # No break.
      total += 1
  return total

def isPal(num, base=10):
  src = num
  dst = 0
  i = 0
  while src > 0:
    dst *= base
    dst += src % base
    src //= base
  return num == dst

def pe36():
  total = 0
  for i in range(0, 1000000):
    if isPal(i, 10) and isPal(i, 2):
      total += i
  return total

def rem1st(num):
  return num % 10 ** (numLength(num) - 1)

def isTruncPrime(num):
  numLen = numLength(num)
  valid = True
  rNum = num
  for i in range(0, numLen):
    if not isPrime(rNum):
      return False
    rNum //= 10
  lNum = num
  for i in range(0, numLen):
    if not isPrime(lNum):
      return False
    lNum = rem1st(lNum)
  return True
  
def pe37():
  found = 0
  total = 0
  i = 10
  while found < 11:
    if i % 100000 == 0:
      print(i)
    if isTruncPrime(i):
      print(i)
      total += i
      found += 1
    i += 1
  return total

def arrToNum(arr):
  arr = arr[::-1]
  total = 0
  for i in range(0, len(arr)):
    total += arr[i] * 10 ** i
  return total

def isPanMult(arrNum):
  for l in range(1, len(arrNum)//2+1):
    base = arrToNum(arrNum[0:l])
    #print(base)
    index = l
    for i in range(2, 10):
      multLen = numLength(base * i)
      slc = arrNum[index:index+multLen]
      resNum = arrToNum(slc)
      #print(resNum)
      if not resNum == base * i:
        #print("Bad num!")
        break
      index += multLen
      if index == len(arrNum):
        return True
  return False

def pe38():
  nums = [9,8,7,6,5,4,3,2,1]
  for i in itertools.permutations(nums):
    if isPanMult(i):
      return i

def pe39():
  counts = {}
  for i in range(0, 1001):
    counts[i] = 0
  for i in range(0, 500):
    for j in range(i//2-1, i+1):
      for k in range(i-j-1, j+1):
        if k**2 + j**2 == i**2 and i+k+j < 1001:
          counts[i+k+j] += 1
  maxx = 0
  maxKey = 0
  for k, v in counts.items():
    if v > maxx:
      maxx = v
      maxKey = k
  return (maxKey, maxx)

def pe48():
  num = 0
  for i in range(1, 1001):
    num += i**i
  return num % 10000000000

def getDig(num, dig):
  return (num // 10**(dig-1))%10

def chamDig(dig):
  if dig <= 9:
    return dig
  if dig <= 189:
    startNum = 10
    tenPow = 10
    numDig = 2
    #return getDig(10+(dig-10)//2, 2 - dig % 2)
  elif dig <= 2889:
    startNum = 190
    tenPow = 100
    numDig = 3
    #return getDig(100+(dig-100)//3, 3 - dig%3)
  elif dig <= 38889:
    startNum = 2890
    tenPow = 1000
    numDig = 4
  elif dig < 488889:
    startNum = 38890
    tenPow = 10000
    numDig = 5
  elif dig < 5888889:
    startNum = 488890
    tenPow = 100000
    numDig = 6
  return getDig(tenPow+(dig-startNum)//numDig, numDig - (dig-startNum) % numDig)

def pe40():
  prod = 1
  for i in range(0, 7):
    cham = chamDig(10**i)
    print(cham)
    prod *= cham
  return prod

def pe41():
  nums = [9,8,7,6,5,4,3,2,1]
  for i in range(9, 1, -1):
    nums = []
    for j in range(i, 0, -1):
      nums.append(j)
    print(nums)
    for j in itertools.permutations(nums):
      if isPrime(arrToNum(j)):
        return j

def firstNTriangleNums(n):
  nums = []
  for i in range(1, n+1):
    nums.append((i*(i-1))//2)
  return nums

def pe42():
  triangles = 0
  file = open("p42words.txt")
  words = file.read().split(",")
  for i in range(0, len(words)):
    words[i] = words[i][1:-1]
  tris = firstNTriangleNums(100)
  largest = 0
  for word in words:
    total = 0
    for char in word:
      total += ord(char) - ord('A') + 1
    if total in tris:
      triangles += 1
    if total > largest:
      largest = total
  return triangles

def getNthPrime(n):
  return getPrimes(n)[-1]

def getFirstNPrimes(n):
  primes = []
  i = 2
  while len(primes) < n:
    prime = True
    for p in primes:
      if i % p == 0:
        prime = False
    if prime:
      primes.append(i)
    i += 1
  return primes

def yPrimes():
  p = 2
  yield 2
  p = 3
  while True:
    if isPrime(p):
      yield p
    p += 2

def isSubDiv(arrNum, primes = getFirstNPrimes(10)):
  for j in range(1, 8):
    slcNum = arrToNum(arrNum[j:j+3])
    prime = primes[j-1]
    if slcNum % prime != 0:
      return False
  return True

def pe43():
  nums = [9,8,7,6,5,4,3,2,1,0]
  total = 0
  primes = getFirstNPrimes(10)
  for i in itertools.permutations(nums):
    if isSubDiv(i, primes):
      total += arrToNum(i)
  return total

def calcPentagon(n):
  return n*(3*n-1)//2

def isPentagon(n):
  return float.is_integer((1/6)*(1+math.sqrt(1+24*n)))
  

def pe44():
  D = 10**10
  pents = {}
  for i in range(1, 10000):
    if not i in pents:
      pents[i] = calcPentagon(i)
    for j in range(1, i):
      if not j in pents:
        pents[j] = calcPentagon(j)
      Pi = pents[i]
      Pj = pents[j]
      if isPentagon(Pi - Pj) and isPentagon(Pi + Pj) and (Pi - Pj) < D:
        D = Pi - Pj
        print(D)
  return D

def yTriNums(startTerm = 1):
  d = startTerm
  n = startTerm*(startTerm+1)//2
  while True:
    yield n
    d += 1
    n += d

def isHexagonal(n):
  return float.is_integer((1/4)*(-1 - math.sqrt(1 + 8*n)))

def pe45():
  for i in yTriNums(50):
    if isHexagonal(i) and isPentagon(i):
      print(i)

def ySquares():
  i = 1
  while True:
    yield i**2
    i += 1

def getPrimeFactors(num, primes = []):
  facts = []
  
  if num % 2 == 0:
    while num % 2 == 0:
      num //= 2
    facts.append(2)
    
  for p in primes:
    if num <= 1:
      return facts
    if num % p == 0:
      while num % p == 0:
        num //= p
      facts.append(p)
      
  c = p if len(primes) > 0 else 3
  while num > 1:
    if num % c == 0 and isPrime(c):
      while num % c == 0:
        num //= c
      facts.append(c)
    c += 2
##  for i in range(2, num // 2 + 1):
##    if num % i == 0 and isPrime(i):
##      facts.append(i)
  if isPrime(num):
    facts.append(num)
  return facts

def pe46():
  primes = []
  squares = [0]
  squareGen = ySquares()
  primeGen = yPrimes()
  primes.append(primeGen.__next__())
  primes.append(primeGen.__next__())
  primes.remove(2)
  i = 3
  while True:
    found = False
    while primes[-1] <= i:
      pg = primeGen.__next__()
      primes.append(pg)
    for p in primes:
      dub = i - p
      dub = dub // 2
      if dub >= 0 and (dub == 0 or float.is_integer(math.sqrt(dub))):
        found = True
        break
    if not found:
      print(i)
    i += 2

def pe47(pfs = 4):
  num = 2
  facts = []
  primes = getFirstNPrimes(100)
  facts.append(len(getPrimeFactors(num)))
  facts.append(len(getPrimeFactors(num+1)))
  facts.append(len(getPrimeFactors(num+2)))
  while True:
    #print(num)
    facts.append(len(getPrimeFactors(num+3, primes)))
    if facts[0] >= 4 and facts[1] >= 4 and facts[2] >= 4:
      print(str(num) + ": " + str(facts))
    if facts[0] >= pfs and facts[1] >= pfs and facts[2] >= pfs and facts[3] >= pfs:
      return num
    num += 1
    facts.pop(0)

def numToArr(num):
  arr = []
  while num > 0:
    arr.append(num % 10)
    num //= 10
  return arr[::-1]

def primesUpTo(num):
  primes = []
  nums = [0] * (num+1)
  for i in range(2, num+1):
    if nums[i] == 0:
      primes.append(i)
      j = i+i
      while j < num+1:
        nums[j] += 1
        j += i
  return primes

##  for i in range(2, num+1):
##    if i % 10000 == 0:
##      print("Calculating P_{0}.".format(i))
##    for p in primes:
##      if i % p == 0:
##        break
##    else:
##      primes.append(i)
##  return primes

def pe49():
  digs = [1, 0, 0, 0]
  base = arrToNum(digs)
  while base < 10000:
    seq = []
    base = arrToNum(digs)
    seq.append(base)
    if isPrime(base):
      perms = [arrToNum(i) for i in itertools.permutations(digs)]
      toRemove = []
      for i in range(len(perms)-1, -1, -1):
        if not isPrime(perms[i]) or perms[i] <= base:
          toRemove.append(i)
      for i in toRemove:
        perms.pop(i)
      for i in perms:
        diff = i - base
        for j in perms:
          if j - i == diff:
            seq.append(i)
            seq.append(j)
            print(seq)
    base += 1
    digs = numToArr(base)

def pe50():
  highLength = 0
  highSum = 0
  primes = primesUpTo(1000000)
  print(len(primes))
  start = 0
  length = 2
  for length in range(, len(primes)):
    if length % 1000 == 0:
      print(length)
    total = sum(primes[0:length])
    if total > 1000000:
        break
    for i in range(1, len(primes) + 1 - length):
      if total > 1000000:
        break
      if isPrime(total) and length > highLength:
        highLength = length
        highSum = total
      total = sum(primes[i:i+length])
  print("{0}: {1}".format(highSum, highLength))
      
    
        

        
  
  

















