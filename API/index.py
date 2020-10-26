import executionary
from datetime import datetime, timedelta
import json

# detractors : 0-6
# passives : 7-8
# promoters : 9-10

class Api_Requests:
    def __init__(self):
        self.executioner=executionary.Executionary()

    def get_NPS_Scores(self):
        Score_Data=self.executioner.getAllData()[0]
        output=dict()
        output=dict()
        mean_score=0.0

        for key, val in Score_Data.items():
            if val["Date"] in output:
                mean_score=(mean_score+val["Score"])/2.0
            else:
                mean_score=val["Score"]
            output[val["Date"]]=mean_score

        output=sorted(output.items(), key = lambda k: k[0])
        new_output={}
        for ele in output:
            new_output[ele[0]]=ele[1]
        return (new_output)