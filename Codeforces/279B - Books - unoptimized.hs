{-# LANGUAGE TupleSections #-}

import Data.List
import Text.Read

-- O(n^2) time complexity, it repeats several intermediate sums
solve :: Int -> [Int] -> Int
solve t = maximum . fmap (length . takeWhile (<= t) . scanl1 (+)) . tails

parse :: String -> Maybe (Int, [Int])
parse s = case fmap words . lines $ s of
    ((_:t:_):bs:_) -> (,) <$> readMaybe t
                          <*> traverse readMaybe bs
    _              -> Nothing

run = fmap (uncurry solve) . parse

main :: IO ()
main = interact (maybe "" show . run)
