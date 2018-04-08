# Welcome to Weblearn.js
Weblearn.js is a javascript library which allows web developers to perform advanced mathematical
tasks and rudimentary machine learning in the browser. Recognizing that JavaScript is, in most cases,
too inefficient and lacking many of the tools needed to perform advanced computation such as this, in addition
to the fact that the library is intended to bring machine learning capabilities to underpowered
web browsers, Weblearn funcionality is based entirely in Python on servers. Weblearn is versatile, usable for
anything from education to face recognition. Read on for more information.

## Setup
Setting up Weblearn for use on your website is as simple as a JavaScript import, simply paste `<script src="https://cdn.rawgit.com/prathgan/weblearn.js/2b4682e4c77480922d4816280c08162a2da42177/JavaScript/weblearn.js"></script>` (valid as of build on 04/02/2018) <b>before</b> any other JavaScript imports or code in your HTML file. Then, anywhere you choose
below that import, insert your script.

## Use
Weblearn has a variety of functions and capabilities available to you to use, and for refrence, see the table of functions, their purpose,
paramaters, and returns below.
#### General Use
A weblearn call has the following format: `weblearn(functionID, parameters)`. All parameters to the `weblearn()` function
are Strings. Below is a code snippet exemplifying general use of Weblearn. You must define an `acceptWeblearnResult(result)` function, where you do what you choose with the result returned from the weblearn call, passed into the function as the `result` parameter.
```js
weblearn("vector_add","[[1,1,1],[3,3,3]]");

function acceptWeblearnResult(result){
    console.log(result);
}
```
This will output "3,3,3" in the console.
#### Functions List and Other Information

|    Function ID    |          Use          |                     Parameters                    |                                        Return                                        |
|:-----------------:|:---------------------:|:-------------------------------------------------:|:------------------------------------------------------------------------------------:|
| `linear_regression`      | predicts points by training a regression model based on x,y points        | `[[x1,x2,x3...],[y1,y2,y3...],prediction_value]` | A single rounded int corresponding to the predicted value of the input point `prediction_value` |
| `support_vector_machine`      | predicts labels by training an SVM model based on feature vectors and corresponding labels         | `[[[feature_vector_1], [feature_vector_2],..,[feature_vector_n]],[[label_1,label_2,...,label_n]],[prediction_feature_vector_1,...,prediction_feature_vector_z]]` | a list containing the labels corresponding to all features put in as a `prediction_feature_vector` |
| `neural_network`      | predicts labels by training multilayer perceptron feedforward neural network based on feature vectors and corresponding labels         | `[[[feature_vector_1], [feature_vector_2],..,[feature_vector_n]],[[label_1,label_2,...,label_n]],[prediction_feature_vector_1,...,prediction_feature_vector_z]]` | a list containing the labels corresponding to all features put in as a `prediction_feature_vector` |
| `vector_add`      | adds two vectors      | `[[vector_one],[vector_two]]`                     | a vector of length same as`vector_one` and `vector_two`, with the added values       |
| `vector_subtract` | subtracts two vectors | `[[vector_one],[vector_two]]`                     | a vector of length same as`vector_one` and `vector_two`, with the subtracted values  |
| `vector_sum`      | sums n vectors        | `[[vector_one],[vector_two],[vector_three], etc]` | a vector of length same as all the vectors in the parameters, with the summed values |


multilayer perceptron feedforward neural network