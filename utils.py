import json
import pandas as pd
import random
import os
import urllib.request

from PIL import Image
import requests
from io import BytesIO
from base64 import b64encode

with open('mapping.json', 'r') as mymapfile:
    map_data=mymapfile.read()
map_dict = json.loads(map_data)



class AnnotDf:
    def __init__(self, df_path):
    
        self.path = df_path

    def load_df(self):
        df = pd.read_csv(self.path)
        return df
    
    def save_df(self, df): 
        df.to_csv(self.path, index=False)
    
    def get_options(self, name):
        random.seed(int(name.split('.')[0]))
        try:

            df = self.load_df()
            options = df.loc[df.image_path==name, ['ar', 'distractor_1', 'distractor_2']].values[0]
            ordered_options = random.sample(list(options), 3)
            self.save_df(df)

            return tuple(ordered_options)
        except:
            return "No AR statement available for the image"

    def get_statement(self, index):

        try:

            df = self.load_df()
            statement = df.loc[index, 'statement']
            self.save_df(df)

            return statement
        
        except:
            return "No AR statement available for the image"


    def annotate_ans(self, annot, image):
        df = self.load_df()
        df.loc[df.image_path==image, 'answer'] = annot
        self.save_df(df)

    def annotate_ans_ranking(self, annot, index):
        df = self.load_df()
        df.loc[index, 'answer'] = annot
        self.save_df(df)
    
    
    def clean_dataset(self):
         df = self.load_df()
         df.distractor_1 = [None] * 150
         df.distractor_2 = [None] * 150
         df.flag = [None] * 150
         self.save_df(df)
    
    def resume(self):
         df = self.load_df()
         idx = df[(~df.answer.isnull())].shape[0]
         return idx
         

        
    def count_annotations(self):
        df = self.load_df()
        return df[(~df.distractor_1.isnull()) & (~df.distractor_2.isnull())].shape[0]
    

class AnnotationManager:
    def __init__(self, annot_df):
        self.annot_df = annot_df
        self.current_index = 0
        self.global_path = 'https://people.cs.pitt.edu/~mzhang/image_ads'
        self.image_paths = list(annot_df.load_df().image_path)

        

    def get_image_path(self):
        
        req_path = os.path.join(self.global_path, map_dict[self.image_paths[self.current_index]])

        response = requests.get(req_path)

# Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Read the image data from the response
            image_data = BytesIO(response.content)
            dataurl = 'data:image/png;base64,' + b64encode(image_data.getvalue()).decode('ascii')
            return dataurl

        else:
             return None
    
    def get_image_url(self):
         im_url = os.path.join(self.global_path, map_dict[self.image_paths[self.current_index]])
         return im_url

    def get_image_name(self):
         name = self.image_paths[self.current_index]
         return name
    




         
     
