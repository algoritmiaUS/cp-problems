import Data.List as L
import Data.Map.Strict as M
import Data.Maybe
import Text.Read

solve bosses = length . takeWhile (not . L.null) . iterate (subordinatesOf =<<) $ subordinatesOf (-1)
    where bossesToSubordinates = M.fromListWith (<>) . zipWith (\s b -> (b, [s])) [1..] $ bosses
          subordinatesOf b     = fromMaybe [] $ M.lookup b bossesToSubordinates

parse :: String -> Maybe [Int]
parse = traverse readMaybe . L.drop 1 . lines

run = fmap solve . parse

main = interact (show . fromMaybe 0 . run)
