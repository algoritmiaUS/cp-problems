{-# LANGUAGE LambdaCase, TupleSections #-}

import Data.Array
import Data.Foldable
import Data.Graph
import Data.Maybe
import Data.Tuple
import Text.Read

solve n edges | odd n     = -1
              | otherwise = maybe 0 (subtract 1 . nodesWithEvenChildren)
                          . listToMaybe . dfs graph
                          . fmap fst . filter ((== 1) . snd) . assocs . outdegree
                          $ graph
    where graph = buildG (1, n) . foldMap swapDup $ edges

nChildrenFrom (Node v cs) | null cs   = Node (v, 0) []
                          | otherwise = Node (v, sum . fmap ((+1) . getNumChildren) $ countedChildren) countedChildren
    where countedChildren = fmap nChildrenFrom cs

getNumChildren (Node (_, n) _) = n

swapDup t = [t, swap t]

isRootALeaf (Node _ cs) = length cs == 1

nodesWithEvenChildren = length . filter (even . snd) . toList . nChildrenFrom

(>>>) = flip (.)

parse :: String -> Maybe (Int, [(Int, Int)])
parse = lines >>> \case
    (n:e) -> fmap (, mapMaybe (listToTuple . words) e) $ readMaybe n
    _     -> Nothing

listToTuple (x:y:_) = (,) <$> readMaybe x
                          <*> readMaybe y
listToTuple _       = Nothing

run = fmap (uncurry solve) . parse

main = interact $ maybe "" show . run
