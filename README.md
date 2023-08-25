# ML algorithms from Scratch!

> Machine Learning algorithm implementations from scratch.


## Algorithms Implemented

- KNN
- Linear Regression
- Logistic Regression
- Naive Bayes
- Perceptron
- SVM
- Decision Tree
- Random Forest
- Principal Component Analysis (PCA)
- K-Means
- AdaBoost
- Linear Discriminant Analysis (LDA)

## Installation and usage.

This project has 4 dependencies.

- `numpy` for the maths implementation and writing the algorithms
- `Scikit-learn` for the data generation and testing.
- `Matplotlib` for the plotting.
- `Pandas` for loading data.

**NOTE**: Do note that, Only `numpy` is used for the implementations. Others
help in the testing of code, and making it easy for us, instead of writing that
too from scratch.

You can install these using the command below!

```sh
# Linux or MacOS
pip3 install -r requirements.txt

# Windows
pip install -r requirements.txt
```

You can run the files as following.

```sh
python -m ML_Algorithms_From_Scratch.<algorithm-file>
```

with `<algorithm-file>` being the valid filename of the algorithm without the extension.

For example, If I want to run the Linear regression example, I would do 
`python -m mlfromscratch.linear_regression`

