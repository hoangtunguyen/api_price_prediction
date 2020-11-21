from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_predict.service import service
import numpy as np
import pandas as pd

x = pd.read_csv("./api_predict/service/x_test.csv")


class PredictionView(APIView):
    def get(self, request, ):
        result = service.predict_price(x[0:1])[0][0]

        return Response(dict(data=result))
