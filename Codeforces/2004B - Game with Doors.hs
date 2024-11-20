{-# LANGUAGE ApplicativeDo #-}

import Data.List
import Data.Maybe
import Text.Read

solve (l, r) (l', r') = a - b + c
    where a = if r < r' then r  else r'
          b = if l < l' then l' else l
          c = (if l == l' then 0 else 1) + (if r == r' then 0 else 1)

parse = catMaybes . go . fmap words . drop 1 . lines
    where go ((l:r:_):(l':r':_):ss) =
              let parsed = do a :: Int <- readMaybe l
                              b :: Int <- readMaybe r
                              c :: Int <- readMaybe l'
                              d :: Int <- readMaybe r'
                              pure ((a, b), (c, d))
              in parsed : go ss
          go (_:_:ss)               = go ss
          go _                      = []

run = fmap (uncurry solve) . parse

main :: IO ()
main = interact (unlines . fmap show . run)
