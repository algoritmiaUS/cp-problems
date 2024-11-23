import Control.Monad
import Data.Bool
import Data.Bifunctor
import Data.Graph
import Data.List
import Data.Maybe
import Text.Read

solve n = maybe False check . listToMaybe . flip dfs [1] . buildG (1, n) . flip zip [2..n]

check :: Tree a -> Bool
check (Node _ []) = False 
check (Node _ cs) = and . uncurry (:) . bimap ((>= 3) . length) (fmap check) . partition isLeaf $ cs

isLeaf (Node _ cs) = null cs

parse :: String -> Maybe (Int, [Int])
parse = uncurry (liftA2 (,)) . bimap readMaybe (traverse readMaybe) <=< uncons . lines

run = fmap (uncurry solve) . parse

main = interact $ maybe "" (bool "No" "Yes") . run
