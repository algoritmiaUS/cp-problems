import Data.Foldable
import Data.List as L
import Data.Set as S

data Counter = Counter { singleWinner :: Int
                       , pairWinner   :: Int }

instance Semigroup Counter where
    (Counter s1 p1) <> (Counter s2 p2) = Counter (s1 + s2) (p1 + p2)

instance Monoid Counter where
    mempty = Counter 0 0

instance Show Counter where
    show (Counter s p) = show s <> "\n" <> show p <> "\n"

count l = case length . S.fromList $ l of
    1 -> Counter 1 0
    2 -> Counter 0 1
    _ -> Counter 0 0

diagonal = fmap (head . uncurry L.drop) . zip [0..2] . fmap cycle

solve :: [String] -> Counter
solve c = foldMap count $ c <> r <> [d] <> [d']
    where r  = transpose c
          d  = diagonal c
          d' = diagonal $ fmap reverse c

main = writeFile "tttt.out" . show . solve . lines =<< readFile "tttt.in"
