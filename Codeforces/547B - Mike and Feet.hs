import Data.List
import Text.Read

solve = fmap maximum . takeWhile (not . null) . iterate (mapWindow min)

mapWindow :: (a -> a -> a) -> [a] -> [a]
mapWindow f (x:xs@(y:ys)) = f x y : mapWindow f xs
mapWindow _ _             = []

parse :: String -> Maybe [Int]
parse = traverse readMaybe . words . (!! 1) . lines

run = fmap solve . parse

main = interact (maybe "" (unwords . fmap show) . run)
