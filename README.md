A continuous change between two or more languages in a single utterance is known as code-switching. In this work, we develop a novel model to predict whether given audio is monolingual or contains code-switching.
We propose to use a convolutional encoder in combination with transformer architecture for utterance-level code-switching detection. The convolution encoder processes the spectral features from audio with the help of 1D convolutional layers. 
The convolutional layer output features are processed by the Transformer network, consisting of a sequence of multi-head self-attention layers. The multi-head self-attention layers use attention mechanisms and help in selecting relevant information for better code-switching detection. 
Finally, our model aggregates frame-level features from the transformer network to create an utterance-level feature vector to predict the class label. We train and evaluate our model using the dataset provided by the Microsoft codeswitching challenge. 
The training data contains three different languages, and each language contains both mono-lingual and code-switched utterances. Our model achieves significantly better accuracy compared to the baseline model. 
Our experiments show that, compared to the baseline, we obtain approximately 8%, 7%, and 3% improvement in accuracy for Telugu, Gujarati, and Tamil language, respectively.
**Presentation** - [[https://docs.google.com/presentation/d/1JNAQpwOOpqQtIEAtPh7k9K9ugn-Un0J2/edit#slide=id.p2](https://docs.google.com/presentation/d/1JNAQpwOOpqQtIEAtPh7k9K9ugn-Un0J2/edit?usp=sharing&ouid=110080193885383515171&rtpof=true&sd=true)](url)
