import pandas as pd
import csv
import plotly.express as px

data = pd.read_csv("data.csv")

# print(data.groupby( [ "student_id" , "level" ] , as_index = False )["attempt"].mean() )

mean = data.groupby( [ "student_id" , "level" ] , as_index = False )["attempt"].mean()

graph = px.scatter( mean , x = "student_id", y = "level" , color = "attempt" )

graph.show()