import pandas as pd
import pickle


cnt = [0] * 5
labels = pickle.load(open('simulated_data_label.pkl', 'rb'))
for label in labels:
    cnt[label] += 1

for i in range(5):
    print('Label {label} percentage:{percentage:8.2f}%'.format(label=i, percentage=cnt[i]/1200))
