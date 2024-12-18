import Data.Bifunctor
import Data.IntSet as S
import Data.List as L
import Text.Read

intercalate' :: [a] -> [a] -> [a]
intercalate' xs [] = xs
intercalate' [] ys = ys
intercalate' (x : xs) (y : ys) = y : x : intercalate' xs ys

triangleChop xs = stopAtEnd . adapt $ splits
  where
    splitter = flip L.splitAt . snd
    splits = L.scanl' splitter ([], xs) [1 ..]
    adapt = fmap fst . L.drop 1
    stopAtEnd = takeWhile (not . L.null)

solve xs = (iceToBuy, foldl1' intercalate' . triangleChop . S.toAscList $ sorted)
  where
    sorted = S.fromList xs
    iceToBuy = (S.size sorted - 1) `quot` 2

parse :: String -> Maybe [Int]
parse s = case words <$> lines s of
  (_ : l : _) -> traverse readMaybe l
  _ -> Nothing

run = fmap solve . parse

main = interact $ maybe "" (\(n, arr) -> show n <> "\n" <> unwords (fmap show arr)) . run
