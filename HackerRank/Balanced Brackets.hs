import Data.Bool
import Data.List
import Data.Maybe

check pb []                      = null pb
check pb (x:xs) | x `elem` "{([" = check (x:pb) xs
                | otherwise      = maybe continue branchOnBracket $ lookup x bracketPairs
    where bracketPairs    = [ ('}', '{')
                            , (')', '(')
                            , (']', '[') ]
          isLastBracket c = maybe False (== c) $ listToMaybe pb
          approve         = check (tail pb) xs
          stop            = False
          branchOnBracket = bool stop approve . isLastBracket
          continue        = check pb xs

solve = bool "NO" "YES" . check []

parse = drop 1 . lines

run = fmap solve . parse

main = interact (unlines . run)
