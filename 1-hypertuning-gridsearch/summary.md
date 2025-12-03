# Summary week 1
REFLECTION 

Tuning the hyperparameters was not a straightforward task for me. First I had difficulty understanding the code and then I had difficulty running tensorboard. A lot of new concepts which I have to get familiar with. Second, I refreshed my knowledge about the meaning of an epoch, matrix multiplication and class inheritence. Also looking at the logging around running neural networks and making transparant what it is doing. Finally I tried training the neural network, this went fine until I made some changes to the number of layers and hidden units per layer. This made me realize that the possible combinations grow exponentially if you don't use a smart gridsearch technique.

My initial hypothesis for the hyperparameter interactions was that a wider and deeper neural network would always produces better results for the task. After experimentating a bit, I have come to the conclusion that setting the right amount of epochs, optimizer settings, trainstep sizes and grid search strategy are very important. When this is set correctly only then you can worry about setting the right amount of units and layers. What is the right amount of units and layers? This depends on the complexity of the data, but also on the amount of compute and time you have for training a model. I have experienced for example that with every epoch a slight improvement of the model was seen, but this takes time. 

I could not yet visualise my findings unfortunately but I did wrote down some hypothesis and experiments.

Hypothesis 1
Increasing the units means that more patterns can be learned per layer in the data and thus result in a model that fits better for a complex data pattern. (higher accuracy)  But can also cause overfitting so a high score on the train set and low on the test set.

Experiment

more units 1024,512,256

less units 64, 32, 16

Findings

Highest accuracy with more units (0.87)

Highest accuracy with less units (0.85)

Conclusion

This is not a complex data pattern because the difference is very small in accuracy

Hypothesis 2
A high epoch number means the model has seen the whole dataset more often and thus have a higher accuracy. With too much epochs there is a risk of overfitting.

Experiment

Epochs  5

Findings

More epochs gives higher accuracy

Conclusion

It learns the data better

Hypothesis 3
A high batchsize lets the model train faster but also gives the model less opportunities to tune its weights resulting in less performance

Experiment

batchsize 128

batchsize 4

Findings

batchsize 4 gives highest accuracy 0.51

batchsize 128 gives highest accuracy  0.78

Conclusion

Setting the batch size (how often the model can update its weights) is very important, and the higher probably the better for a robust model.

Hypothesis 4
A low batchsize lets the model train faster but also gives the model less opportunities to tune its weights resulting in less performance

Experiment

batchsize 128

batchsize 4

Findings

batchsize 4 gives highest accuracy 0.51

batchsize 128 gives highest accuracy  0.78

Conclusion

Setting the batch size/train steps (how often the model can update its weights) is very important, and the higher probably the better for a robust model.

Hypothesis 5
Adding depth to the model helps the model capture more complex patterns in the data and i think this results into a high accuracy

Experiment

Adding 1 extra layer

Findings

Highest accuracy was 0.77

Conclusion

Adding extra layers can help the model find complex patterns, but only if we are dealing with complex data. In this experiment we can see the accuracy being worse then with less layers

Find the [notebook](./notebook.ipynb) and the [instructions](./instructions.md)

[Go back to Homepage](../README.md)
