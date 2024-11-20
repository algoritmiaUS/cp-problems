import Data.List
import Text.Read

-- O(n) time complexity, it moves the window for intermediate sums
-- by using the same list twice. One of the resulting instances
-- moves forward a single step every iteration as the right bound
-- of the window while the other one only moves forward when an
-- intermediate sum is greater than the maximum time allowed,
-- acting as a stack whose top value is the value in the left
-- bound of the window. Because of lazy evaluation and structural
-- sharing, when the runtime discards the values from this stack
-- as the are popped, it is actually freeing that part of the
-- same input list, so it only needs to keep in memory the part
-- of the list that is within the window. Hence this is not only
-- the most idiomatic implementation in Haskell, but the most
-- efficient one possible in any language, save for memory
-- garbage collection.
--
-- Typeclass boundaries make this function useful for any types
-- required as long as they are numbers.
solve :: (Ord a, Ord b, Num a, Num b) => a -> [a] -> b
solve t bs = maximum $ validWindowSums t bs 0 0 bs

validWindowSums _ _        _    accB []                 = [accB]
validWindowSums _ []       _    _    _                  = [0]  -- This is so `maximum` never throws an exception
validWindowSums t l@(i:is) accT accB (j:js) | accT' > t = accB : advanceStart t is (accT' - i) accB js
                                            | otherwise = validWindowSums t l accT' (accB + 1) js
    where accT' = accT + j

advanceStart _ []       _    _    _             = []
advanceStart t l@(i:is) accT accB r | accT > t  = advanceStart t is (accT - i) (accB - 1) r
                                    | otherwise = validWindowSums t l accT accB r

parse :: String -> Maybe (Int, [Int])
parse s = case fmap words . lines $ s of
    ((_:t:_):bs:_) -> (,) <$> readMaybe t
                          <*> traverse readMaybe bs
    _              -> Nothing

run = fmap (uncurry solve) . parse

main :: IO ()
main = interact (maybe "" show . run)
