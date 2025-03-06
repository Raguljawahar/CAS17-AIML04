 CAS17-AIML04
TANZANITE-MITHUN-CYBERBULLYING

PROBLEM STATEMENT CLARITY:
              
SHORT DESCRIPTION:
Detect and flag harmful social media comments using NLP.

TECHNICAL STACK:

1)Data Collection & Storage:
  *Python with libraries like Tweepy (Twitter), PRAW (Reddit) for collecting social media data
  *MongoDB or PostgreSQL for storing collected comments and metadata
  *Pandas for data manipulation and preprocessing

2)Text Processing & Feature Engineering:
  *NLTK for basic text preprocessing (tokenization, stemming)
  *spaCy for advanced NLP tasks (entity recognition, dependency parsing)
  *scikit-learn for feature extraction with TF-IDF and other vectorization techniques
  *HuggingFace Datasets for working with existing cyberbullying datasets

3)Model Development:
  *PyTorch or TensorFlow/Keras as the deep learning framework
  *HuggingFace Transformers for implementing pre-trained language models
  *BERT/RoBERTa/DistilBERT as the base transformer model
  *scikit-learn for traditional ML algorithms (comparison baseline)
  *Optuna or Ray Tune for hyperparameter optimization

4)Cloud Infrastructure:

  *AWS, GCP, or Azure for cloud hosting
  *AWS SageMaker or Google Vertex AI for model training and deployment

INNOVATION AND UNIQUENESS:


SCALABILITY:

Streaming Architecture:

Implement Apache Kafka or AWS Kinesis for real-time comment ingestion
Design for parallel processing of incoming data streams
Use consumer groups to distribute processing load across multiple instances

Batch Processing:

Leverage Apache Spark for distributed processing of historical data
Implement incremental processing patterns to avoid full reprocessing
Schedule regular model retraining on accumulated data

FEASILIBILITY AND PRACTICALITY:

Natural Language Processing (NLP):

  Feasible: NLP models like BERT, RoBERTa, GPT, and LSTMs are well-suited for text classification tasks.
  Challenge: Understanding sarcasm, code words, and evolving slang requires continuous fine-tuning.
  Solution: Use context-aware models and train on real-world social media datasets.

Real-Time Detection:

  Feasible: Deploying models via FastAPI, Flask, or TensorFlow Serving enables real-time detection.
  Challenge: Latency issues for high-volume platforms like Twitter or Instagram.
  Solution: Optimize models via distillation (TinyBERT, DistilBERT) and use edge computing for efficiency.
  

  
  
