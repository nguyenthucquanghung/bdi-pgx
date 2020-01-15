import pickle


x_train = pickle.load(open('simulated_data.pkl', 'rb'))
y_train = pickle.load(open('simulated_data_label.pkl', 'rb'))

print(x_train.shape)
print(y_train.shape)