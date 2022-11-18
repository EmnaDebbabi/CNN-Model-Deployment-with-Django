import string
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
from tensorflow.python.keras.models import load_model
import os
import gzip
import pickle as pkl
from .utils import *

# Create your views here.
def predict(request):
    return render(request,'predict.html')
def predict_chances(request):
    if request.POST.get("action")=='post':
        # Receive data from client
        sentence = str(request.POST.get('s_l'))
        position1 = int(request.POST.get('s_w'))
        position2 = int(request.POST.get('p_l'))
        #save to file
        print('*****',os.getcwd())
        folder='/home/sesamm/emna/pfe1/pfe/extra/deploy test/mlops/CNN deploy/CNN/predict/data/'
        files = [folder+'dep_test.txt']   

        df=pd.DataFrame([position1,position2,sentence]).T
        df.to_csv(files[0],header=False, index=False,sep="\t")
        # Unpickle model
        model = load_model("/home/sesamm/emna/pfe1/pfe/extra/deploy test/mlops/CNN deploy/CNN/predict/cnn_model_1.h5")
        f = gzip.open(folder + 'causal-relations.pkl.gz', 'rb')
        data = pkl.load(f)
        f.close()
        maxSentenceLen = data['max_sentence_length']
        word2Idx = data['word2Idx']
        labelsMapping = data['labels_mapping']
        minDistance = data['min_distance']
        maxDistance = data['max_distance']
        vectorizer = Vectorizer(word2Idx, labelsMapping, minDistance, maxDistance, maxSentenceLen)
        yTest, sentenceTest, positionTest1, positionTest2 = vectorizer.vectorizeInput1(files[0])
        # Make prediction
        result = model.predict([sentenceTest, positionTest1, positionTest2], verbose=False).argmax(axis=-1)
        print("*******",result[0])
        classi=result[0]
        if classi==1:
            classification = "Cause"
        elif classi==2:
            classification = "Effect" 
        else:       
            classification = "Other"
        print('*********here',sentence)
        PredResults.objects.create(sentence= sentence, position1=position1, position2=position2, classification=classification)

        return JsonResponse({'result': classification, 'sentence': sentence,
                             'position1': position1, 'position2': position2},
                            safe=False)
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)        
        