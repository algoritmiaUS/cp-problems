import Data.List as L
import Data.Maybe
import Data.Set as S
import Text.Read

solve n = last . L.foldl' sumInSpiral ((1 :: Integer) : replicate n 0) . S.toList . S.fromList

sumInSpiral m x = spiral
    where (w, r) = L.splitAt x m
          spiral = w <> zipWith (+) r spiral

parse :: String -> Maybe (Int, [Int])
parse s = case fmap words . lines $ s of
    ((n:_:_):coins:_) -> (,) <$> readMaybe n
                             <*> traverse readMaybe coins
    _                 -> Nothing

run = fmap (uncurry solve) . parse

main = interact (show . fromMaybe 0 . run)
