import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8), PIL.Image.Resampling.LANCZOS)

    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    numImage = numImage.flatten()

    print(numImage)
    return numImage

#数字を予測する
def predictDigits(data):
    #学習データを読み込む
    digits = sklearn.datasets.load_digits()
    #機械学習をする
    clf = sklearn.svm.SVC(gamma = 0.001)
    #予測結果を表示する
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("予測=", n)

data = imageToData("tmp/5.png")
predictDigits(data)
