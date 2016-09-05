factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

lenNum :: (Integral a) => a -> a
lenNum a = ceiling $ logBase 10 $ fromIntegral a + 1

revNum :: (Integral a) => a -> a
revNum a
  | a < 0 = (*) (-1) $ revNum $ a * (-1)
  | a <= 10 = a
  | otherwise = rem a 10 * 10 ^ subtract 1 (lenNum a) + (revNum $ div a 10)

isPalindrome :: (Integral a) => a -> Bool
isPalindrome a = (==) a $ revNum a

listMax :: (Ord a) => [a] -> a
listMax [x] = x
listMax (x:t)
  | x > maxTail = x
  | otherwise = maxTail
  where maxTail = listMax t

--pe4 :: Num
pe4 = listMax $ filter isPalindrome $ (*) <$> [999,998..100] <*> [999,998..100]
