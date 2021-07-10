# Data Analytics
Breast cancer dataset description;


How many features? 	30
How many examples (rows)?	178
How many classes? 	2
class_0  Benign
class_1  Malignant

# Features od dataset
30 features (3*10)
a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal

![image](https://user-images.githubusercontent.com/50274550/125157845-7af7f280-e182-11eb-930b-6fec7e924ef3.png)

Now lets visualize the data!
![image](https://user-images.githubusercontent.com/50274550/125157853-86e3b480-e182-11eb-81a5-d82852ad3255.png)

Correlation between features:
Radius vs perimeter
![image](https://user-images.githubusercontent.com/50274550/125157860-97942a80-e182-11eb-95c5-3a36f77bf452.png)

Some bad features:
Smoothness vs symmetric
![image](https://user-images.githubusercontent.com/50274550/125157882-b85c8000-e182-11eb-80a0-bbd0ff2c9db6.png)

PCA (Principal component analysis)

pca = PCA(0.99)
principal_components = pca.fit_transform(data)

Explained variance ratio:
[0.98204467,  0.01617649]

![image](https://user-images.githubusercontent.com/50274550/125157901-d32ef480-e182-11eb-9ebe-a595ac9bef3c.png)





