import pandas

pimasdata = pandas.read_csv("diabetes.csv")

traincsv = pimasdata.sample(frac=0.8)
testcsv = pimasdata.drop(traincsv.index)

traincsv.to_csv("training_data.csv")
testcsv.to_csv("test_data.csv")