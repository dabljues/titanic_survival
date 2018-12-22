# titanic_survival
# Analysing the features
## 1. Age
The first idea was to check if age is somehow connected with survival rate.
```python
# Check if survival rate is connected with Age
self._facet_grid(plt.hist, col='Survived', x=['Age'])
```
Using `DataAnalyzer` class, we print this graph which shows correlation between Age and survival rate (very young and very old passengers) have better chance to survive than passengers in age `15-45`:

![alt text](https://i.imgur.com/UkkawqA.png "")
## 2. Sex
As many would think - sex is correlated with survival rate - females had a better chance to survive.
```python
# Check if survival rate is connected with Sex
self._facet_grid(sns.barplot, col='Sex', row='Pclass', x=['Survived'])
```
This plot shows us how the sex of the passengers affected their survival chance:

![alt text](https://i.imgur.com/NpaeW0k.png "")

As we can see - women were 3/4 times more likely to survive the disaster than men. Knowing that, we will include `Sex` feature.
## 3. Pclass
Naturally we would think, that the class of travel would have an impact on the survivability chance (at least back then). This figure shows us the percentage of survival by `Pclass`.

![alt text](https://i.imgur.com/GdKJ2xt.png "")
## 4. Fare
## 5. Embarked