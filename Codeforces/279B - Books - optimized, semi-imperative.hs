{-# LANGUAGE TupleSections, ApplicativeDo #-}

import Control.Monad
import Control.Monad.ST
import Data.Foldable
import Data.Function
import Data.List
import Data.Maybe
import Data.STRef
import Data.Traversable
import GHC.Arr
import Text.Read


-- O(n) time complexity, it only makes
-- the minimum required sums by moving
-- the sum window as necessary
solve :: Int -> [Int] -> Int
solve t b = maximum $ runST $ do

    let bounds@(start, end) = (0, length b - 1)

    arr <- newSTArray bounds 0
    traverse_ (uncurry $ writeSTArray arr) . zip [0..] $ b

    i    <- newSTRef start
    accT <- newSTRef 0
    accB <- newSTRef 0
    for [0..end] $ \j -> do
        nb <- readSTArray arr j
        accT <=: (+nb)
        accB <=: (+1)

        fix $ \advanceStart -> do
            st <- readSTRef accT
            when (st > t) $ do
                x <- readSTArray arr =<< readSTRef i
                accT <=: (subtract x)
                accB <=: (subtract 1)
                i <=: (+1)
                advanceStart

        readSTRef accB

(<=:) = modifySTRef

parse :: String -> Maybe (Int, [Int])
parse s = case fmap words . lines $ s of
    ((_:t:_):bs:_) -> (,) <$> readMaybe t
                          <*> traverse readMaybe bs
    _              -> Nothing

run = fmap (uncurry solve) . parse

main :: IO ()
main = interact (maybe "" show . run)
