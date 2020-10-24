bubble [] = []
--List to be ordered
bubble list = bubbleOrdenation list (length list)

--Goes through the list changing the numbers
bubbleOrdenation list 0 = list
bubbleOrdenation list n = bubbleOrdenation (change list) (n-1)

-- Changes the higher number so it goes to the end of the list
change [x] = [x]
change (x:y:zs)
    | x > y = y : change (x:zs)
    | otherwise = x : change (y:zs)

-- Testing our algorithm
main :: IO()
main = do
let out = bubble [9,3,4,65,6,2,6]
print out