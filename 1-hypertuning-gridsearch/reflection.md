REFLECTION 

Tuning the hyperparameters was not a straightforward task for me. First I had difficulty understanding the code and then I had difficulty running tensorboard. A lot of new concepts which I have to get familiar with. Second, I refreshed my knowledge about the meaning of an epoch, matrix multiplication and class inheritence. Also looking at the logging around running neural networks and making transparant what it is doing. Finally I tried training the neural network, this went fine until I made some changes to the number of layers and hidden units per layer. This made me realize that the possible combinations grow exponentially if you don't use a smart gridsearch technique.

My initial hypothesis for the hyperparameter interactions was that a wider and deeper neural network would always produces better results for the task. After experimentating a bit, I have come to the conclusion that setting the right amount of epochs, optimizer settings, trainstep sizes and grid search strategy are very important. When this is set correctly only then you can worry about setting the right amount of units and layers. What is the right amount of units and layers? This depends on the complexity of the data, but also on the amount of compute and time you have for training a model. I have experienced for example that with every epoch a slight improvement of the model was seen, but this takes time. 

I tried visualizing some of the findings

Hypothesis 
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