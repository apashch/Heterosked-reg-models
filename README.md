# Heterosked reg models


## Main questions
1. Which metrics other than R^2 we can use to evaluate the performance of our models?
2. What other rgression types efficently deal with heteroskedacity?


## Current Progress

### R^2 table

| file/ reg type            | 1            | 2            | 3             | 4              | 5            |
| ------------------------- | ------------ | ------------ | ------------- | -------------- | ------------ |
| LE                        | 0.1639863122 | 0.3980894410 | 0.1031999573  | 0.0275947359   | 0.280575792  |
| GLSE                      | **0.2274437157** | **0.6823281143** | **0.11953091451** | **0.9745862243**   | **0.711592781**  |
| LASSO                     | 0.1639739902 | 0.3980894371 | 0.1031952438  | 0.02759473566  | 0.2805757898 |
| Ridge*                    | 0.1638634355 | 0.3980877000 | 0.1031988620  | 0.02670308780  | 0.2805165134 |
| Huber*                    | 0.1573759139 | 0.3937864654 | 0.08307870806 | 0.006033289645 | 0.2581856714 |
| WLSE*                     | 0.1664085575 | 0.357618477  | 0.03055167044 | **0.8342292431**   | **0.4385992690** |

\* - rough try, maybe can do better if we adjust the parameters


### RMSE table 

| file/ reg typ | 1                 | 2                  | 3                  | 4                  | 5                  |
|---------------|-------------------|--------------------|--------------------|--------------------|--------------------|
| LE            | 5.294970100722123 | 15.423781909816453 | 17.518018349312523 | 5.0732698413588375 | 11.102325107379786 |
| GLSE          | 5.649484470013933 | 23.974759956553925 | 18.96526967901268  | 8.518752862964678  | 14.685501018671081 |
| LASSO         | 5.295009122046357 | 15.42378196082108  | 17.518064385353462 | 5.073269842078679  | 11.102325129029348 |
| Ridge         | 5.295359211991653 | 15.423804216927811 | 17.51802904689963  | 5.075595278718663  | 11.102782503341396 |
| Huber         | 5.315862667257233 | 15.478814975122575 | 17.7134516245657   | 5.129207063129075  | 11.273766249778449 |
| WLSE          | 5.846770837240601 | 19.88008011506033  | 19.014696464711808 | 7.705631806696538  | 14.800132094553431 |
