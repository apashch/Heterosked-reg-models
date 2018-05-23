# Heterosked reg models


## Main questions
1. Which metrics other than R^2 we can use to evaluate the performance of our models?
2. What other rgression types efficently deal with heteroskedacity?


## Current Progress

| file                      | 1            | 2            | 3             | 4              | 5            |
| ------------------------- | ------------ | ------------ | ------------- | -------------- | ------------ |
| Heterosked (White's test) | Y            | N            | N             | Y              | Y            |
| LE R^2                    | 0.1639863122 | 0.3980894410 | 0.1031999573  | 0.0275947359   | 0.280575792  |
| GLSE R^2                  | **0.2274437157** | **0.6823281143** | **0.11953091451** | **0.9745862243**   | **0.711592781**  |
| LASSO                     | 0.1639739902 | 0.3980894371 | 0.1031952438  | 0.02759473566  | 0.2805757898 |
| Ridge*                    | 0.1638634355 | 0.3980877000 | 0.1031988620  | 0.02670308780  | 0.2805165134 |
| Huber*                    | 0.1573759139 | 0.3937864654 | 0.08307870806 | 0.006033289645 | 0.2581856714 |
| WLSE*                     | 0.1664085575 | 0.357618477  | 0.03055167044 | **0.8342292431**   | **0.4385992690** |

\* - rough try, maybe can do better if we adjust the parameters
