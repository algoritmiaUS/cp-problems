{-# LANGUAGE LambdaCase #-}

import Data.Graph
import Data.Maybe
import Text.Read

solve n = reverse . flip reachable n . buildG (1, n) . zip [2..n]

(>>>) = flip (.)

parse :: String -> Maybe (Int, [Int])
parse = lines >>> \case
    (n:rs:_) -> (,) <$> readMaybe n
                    <*> traverse readMaybe (words rs)
    _        -> Nothing

run = fmap (uncurry solve) . parse

main = interact $ maybe "" (unlines . fmap show) . run
