# Heterosked reg models

## Current Progress

| file                      | 1              | 2              | 3               | 4                | 5              |
| ------------------------- | -------------- | -------------- | --------------- | ---------------- | -------------- |
| Heterosked (White's test) | Y              | N              | N               | Y                | Y              |
| LE R^2                    | 0.163986312281 | 0.398089441097 | 0.1031999573    | 0.027594735935   | 0.28057579266  |
| GLSE R^2                  | 0.227443715771 | 0.682328114379 | 0.119530914514  | 0.974586224299   | 0.71159278082  |
| LASSO                     | 0.163973990216 | 0.398089437116 | 0.103195243847  | 0.0275947356591  | 0.280575789854 |
| Ridge*                    | 0.163863435553 | 0.398087700033 | 0.103198862016  | 0.0267030878068  | 0.280516513454 |
| Huber*                    | 0.157375913988 | 0.393786465426 | 0.0830787080623 | 0.00603328964472 | 0.258185671467 |
| WLSE*                     | 0.166408557566 | 0.35761847788  | 0.0305516704417 | 0.834229243125   | 0.438599268994 |

* - rough try, maybe can do better if we adjust the parameters

## Main questions
1. Which metrics other than R^2 we can use to evaluate the performance of our models?
2. What other rgression types efficently deal with heteroskedacity?
