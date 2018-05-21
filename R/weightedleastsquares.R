d1 <- read.csv("./data_1_1.csv")
plot(d1$x,d1$y)
l1 <- lm(d1$y~(1/d1$x))
summary(l1)
plot(d1$x,l1$residuals)
n <- length(d1$x)
X <- cbind(rep(1,length(d1$x)),d1$x)
Y <- d1$y
X1 <- d1$x<=(-2)
v1 <- var(d1$y[X1])
v2 <- var(d1$y[d1$x>=-2 & d1$y<=2])
v3 <- var(d1$y[d1$x>=2])
W <- diag(0,n)
for (i in 1:n){
  if (d1$x[i]<(-2)){
    W[i,i] <- v1
  }else if (d1$x[i]>=(-2) & d1$x[i]<=2){
    W[i,i] <- v2
  }else{
    W[i,i] <- v3
  }
}
betahat <- solve(t(X)%*%solve(W)%*%X)%*%t(X)%*%solve(W)%*%Y
yhat <- X%*%betahat
plot(d1$x,d1$y)
lines(d1$x,yhat,col="red")

mean((Y-yhat)^2)
mean((Y-l1$fitted.values)^2)
