{-# LANGUAGE LambdaCase #-}

import Data.Foldable
import Data.Graph
import qualified Data.Map.Strict as M
import Data.Maybe
import Text.Read

solve n = maybe [0] childrenList . listToMaybe . flip dfs [1] . buildG (1, n) . flip zip [2..n]

nChildrenFrom (Node v cs) | null cs   = Node (v, 0) []
                          | otherwise = Node (v, sum . fmap ((+1) . getNumChildren) $ countedChildren) countedChildren
    where countedChildren = fmap nChildrenFrom cs

getNumChildren (Node (_, n) _) = n

childrenList = M.elems . M.fromList . toList . nChildrenFrom

(>>>) = flip (.)

parse :: String -> Maybe (Int, [Int])
parse = lines >>> \case
    (n:p:_) -> (,) <$> readMaybe n
                   <*> traverse readMaybe (words p)
    _       -> Nothing

run = fmap (uncurry solve) . parse

main = interact $ maybe "" (unlines . fmap show) . run
