#!/usr/local/bin/python3
#coding: utf-8
#VARIABLES

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: Harry Potter
#     Repositorio: DinamoDB
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
#imports
import json
import csv
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from faker import Faker
import faker_commerce
import faker_microservice
from faker_vehicle import VehicleProvider
from faker_music import MusicProvider
import random
from datetime import date, datetime
import numpy as np



#setup
faker = Faker()


def harry(dynamodb=None):
    nome = [faker.name() for i in range(100)]
    sexo = [np.random.choice(["M", "F"], p=[0.5, 0.5]) for i in range(100)]
    endereco = [faker.address() for i in range(100)]
    casa = [random.choice(['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']) for i in range(100)]
    varinha  = [random.choice(['Acacia', 'Elder', 'Chestnut', 'Spruce ']) for i in range(100)]
    patronus = [random.choice(['Otter', 'Dog', 'Fox', 'Dumb', 'Elephant', 'Deer','Mouse', 'Bird', 'Frog', 'Fish', 'Mosquito', 'Bunny'])]
    nascimento = [faker.date_of_birth() for i in range(100)]
    profissao = [faker.job() for i in range(100)]
    dt_update = [datetime.now() for i in range(100)]
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        table = dynamodb.Table('Harry Potter')
              

        response = table.put_item(
        Item={
            "name": nome,
            "gender": sexo,
            "adress": endereco,
            "houses": casa,
            "wand": varinha,
            "patronus": patronus,
            "birth": nascimento,
            "occupation": profissao,
            "dt_update": dt_update
        }
    )
    return response


if __name__ == '__main__':
    data_resp = harry()
    print("Put data succeeded:")
    pprint(data_resp, sort_dicts=False)