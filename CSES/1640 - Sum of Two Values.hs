{-# LANGUAGE TupleSections #-}

import Control.Monad
import Data.IntMap.Strict as M
import Data.Maybe
import Text.Read

swapMinMax t@(x, y) | x > y = (y, x)
                    | otherwise = t

solve :: Int -> [Int] -> Maybe (Int, Int)
solve s ns = listToMaybe $ (\(n, i) -> maybe [] (pure . swapMinMax . (i,)) $ M.lookup (s - n) nm) =<< M.toList nm
    where nm = M.fromListWith const . flip zip [1..] $ ns

parse :: String -> Maybe (Int, [Int])
parse s = case fmap words $ lines s of
    ((_:x:_):ns:_) -> (,) <$> readMaybe x
                          <*> traverse readMaybe ns
    _              -> Nothing

run = uncurry solve <=< parse

main = interact $ maybe "IMPOSSIBLE" (\(a, b) -> show a <> " " <> show b) . run
