# titanic_survival
# Analysing the features
## 1. Age
The first idea was to check if age is somehow connected with survival rate.
```python
# Check if survival rate is connected with Age
self._facet_grid(plt.hist, col='Survived', x=['Age'])
```
Using `DataAnalyzer` class, we print this graph which shows correlation between Age and survival rate (very young and very old passengers) have better chance to survive than passengers in age `15-45`
![alt text](https://i.imgur.com/9WRDnaM.png "")
## 2. Sex
As many would think - sex is correlated with survival rate - females had a better chance to survive.
```python
# Check if survival rate is connected with Sex
self._facet_grid(sns.barplot, col='Sex', row='Pclass', x=['Survived'])
```
This plot shows us how the `Pclass` feature and the sex of the passengers affected their survival chance:
![alt text](https://i.imgur.com/RHse0XG.png "")
As we can see - most of the females were able to survive in first/second class, but in the third class its only half of them, who managed to survive. Knowing that, we will include `Sex` feature and probably `Pclass` feature as well.