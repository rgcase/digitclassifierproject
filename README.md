Digit Classifier
================

This is a classifier for numerical digits 0-9 that was completed as a project for
CISC 859 at Queen's University.

Image files are accepted in .bmp format for both training and classification, 
and are dealt with using the Pillow library.

Classification methods include a naive implementation of k-nearest neighbours,
and multiple other methods that are available in the scikit-learn library.

The accuracy of the classifier is not really acceptable for any real use but
it does a better job than random guessing. The framework is here though, so 
it could be improved by doing better feature selection and tweaking the 
classifiers that are used.
