## This program converts a folder of PDF documents into a dictionary of 100-element arrays containing binary strings, which can be fed into a neural network.


## DEPENDENCIES (Make sure these are installed from your terminal. You will need the package managers Brew and Pip. Brew installation instruction can be found here: https://brew.sh/ and pip3 will be bundled with the Homebrew python installation.)
# brew install python
# brew install pkg-config poppler
# pip3 install glob2
# pip3 install pdftotext
# pip3 install numpy

# Run in Atom using the Script plugin.

import glob, pdftotext, re, numpy as np

def readpdf(path): ##  TEXT ENGINE  ## Takes a file address, returns string.
    f = open(path,"rb")
    pdf = pdftotext.PDF(f, raw=False)
    return " ".join(pdf)

def dictify(text,dic): ## Takes any input and dictionary object. Returns Panda series.
    X = {i:np.binary_repr(''.join(set(text)).index(i),width=10) for i in ''.join(set(text)) } # Assigns unique binary array of ten digits to each unique character.
    [dic.update({i:np.ravel([X[j] for j in i])}) for i in re.split("[\]\[ *)(:;,'±\\\]",re.sub(' +', ' ',text).rstrip()) if i not in dic] # Recursively unravels the dictionary into a single array and removes unwanted characters.
    [dic.update({i:np.pad(dic[i],(0,max(0,100-len(dic[i]))),'constant') for i in dic})] #Max word length = 10 chars.
    return dic,X

folderList = glob.glob("/Users/libertant/Google Drive/ADMIN/BIZ/ACUIQ/ScienceDirectArticles/temp/*.pdf") ## Creates a list of PDF documents from a folder on your harddrive (Change the folder path to suit.)

TEXT = str([readpdf(i) for i in folderList]) ## Converts PDF documents from folderList into a text string.

A,B = dictify(TEXT,{})
print(TEXT)
print(A)
