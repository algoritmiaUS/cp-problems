import Data.List
import Text.Read

modNum = 10^9 + 7

remSum a b = (a + b) `rem` modNum

solve n = head . (!! n) . flip iterate [1] $ \prev -> foldl' remSum 0 prev : take 5 prev

parse :: String -> Maybe Int
parse = readMaybe

run = fmap solve . parse

main = interact (maybe "" show . run)
