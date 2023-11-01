import tkinter as tk
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import random as rand
import time as t 
rand.seed(t.time())

scatterplot = [150,150]
dots = []

def gendots():
    
    global dots
    dots = []
    for i in range(scatterplot[0]):
        for j in range(scatterplot[1]):
                ##gen dots
                dots.append([rand.randint(1,1080),rand.randint(1, 1080)])
    return dots
##kmeans

def alg(dots):
    kmeans =  MiniBatchKMeans(n_clusters = 3, random_state=0, batch_size = 6, max_iter=10, n_init = "auto").fit(dots)
    return kmeans
window_res = "1080x1080"
window_name = "Visual Feedback of Kmeans"
window = tk.Tk()
window.title(window_name)
window.geometry(window_res)

""" def get_shape(shape,x,y,color):
    shape_func_collection = {
         "circle" : canvas.create_oval(x, y, x + 10, y + 10, fill=color),
         "cross" : canvas.create_text(x,y, text= "X", fill=color, font=("Courier", 20)),
         "square" : canvas.create_rectangle(x, y,  x+10, y+10, fill=  color)
    }
    return shape_func_collection[shape]
 """


def get_shape(x, y, color, shape):
    if shape == "circle":
        return canvas.create_oval(x, y, x + 10, y + 10, fill=color)
    elif shape == "cross":
        return canvas.create_text(x, y, text="X", fill=color, font=("Courier", 20))
    elif shape == "square":
        return canvas.create_rectangle(x, y, x + 10, y + 10, fill=color)
    else:
        return None

x = 100
y = 100

canvas = tk.Canvas(window, width =1080, height=1080)
canvas.configure(bg="white")
canvas.pack()

cluster_colors = ["red", "green", "blue"]





while True:
    canvas.delete("all")
    dots = gendots()
    kmeans=alg(dots)
    

    

    cluster_to_shape = {0: "circle", 1: "cross", 2: "square"}

    for i, dot in enumerate(dots):
            cluster_id = kmeans.labels_[i]
            x, y = dot
            color = cluster_colors[cluster_id]
            shape = cluster_to_shape[cluster_id]
            get_shape(x, y, color, shape)

    for i in kmeans.cluster_centers_:
            x,y = i
            canvas.create_oval(x,y,x+30, y+30, fill="black")
    t.sleep(2.5)

        
    
    
    window.update()


