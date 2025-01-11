import Control.Monad
import Text.Read

solve :: [String] -> [String] -> [String]
-- solve w = (>>= fmap mconcat . traverse (mapRule w))
solve w rules = do
  r <- rules
  groupsOfStrings <- sequence $ fmap (mapRule w) r
  return $ mconcat groupsOfStrings

mapRule :: [String] -> Char -> [String]
mapRule w r = case r of
  '0' -> fmap show [0 .. 9]
  '#' -> w
  _ -> [""]

parse :: String -> [([String], [String])]
parse = zipPairs . go . lines
  where
    go [] = []
    go (l : ls) = case readMaybe l of
      Nothing -> go ls
      Just n -> case splitAt' n ls of
        Nothing -> []
        Just (p, p') -> p : go p'

splitAt' :: (Eq t, Num t) => t -> [a] -> Maybe ([a], [a])
splitAt' 0 xs = Just ([], xs)
splitAt' n [] = Nothing
splitAt' n (x : xs) = do
  (xs', xs'') <- splitAt' (n - 1) xs
  return (x : xs', xs'')

zipPairs :: [b] -> [(b, b)]
zipPairs (x : y : ys) = (x, y) : zipPairs ys
zipPairs _ = []

run :: String -> String
run input = unlines $ do
  (w, r) <- parse input
  "--" : solve w r

main :: IO ()
main = interact run
