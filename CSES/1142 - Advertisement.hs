import Data.List
import Data.Maybe
import Data.Set as S
import Text.Read

solve heights = maximum $ areaFrom q heights : areas qs [heights]
    where (q:qs) = S.toList . S.fromList $ heights

areaFrom :: Int -> [Int] -> Int
areaFrom h hs = h * genericLength hs

areas []     _        = []
areas _      []       = []
areas (h:hs) oldZones = fmap (areaFrom h) newZones <> areas hs newZones
    where newZones = splitBy h =<< oldZones

splitBy _ [] = []
splitBy x xs = case gs of
        []      -> [g]
        (_:gs') -> g : splitBy x gs'
    where (g, gs) = break (== x) xs

parse :: String -> Maybe [Int]
parse = traverse readMaybe . words . (!! 1) . lines

run = fmap solve . parse

main = interact (show . fromMaybe 0 . run)
