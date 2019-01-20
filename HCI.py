import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import aseegg as ag
import numpy as np
import csv


plt.rcParams.update({"font.size":15})
dane = pd.read_csv(r"sub-01_trial-10.csv", delimiter=',', engine='python')

t = np.linspace (0, 37.92, 200*37.92)

sygnal1=dane['sygnał1']
# liczby=dane["liczby"]
# przefiltrowany = ag.pasmowoprzepustowy(sygnal1, 200, 1,50)
# przefiltrowany2 = ag.pasmowozaporowy(przefiltrowany, 200, 49,50)


# st.io.wavfile.read(r"sub-01_trial-10.csv", mmap=False)
plt.plot(t, sygnal1)
# plt.plot(t, liczby)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [µmV]")
plt.title("pierwsze dane pobrane i nieprzefiltrowane")
plt.show()


# if przefiltrowany2 ==1:
#     print(dane["liczba"])

###

wynik = 2*abs(np.fft.fft(przefiltrowany2))/len(przefiltrowany2)
wynik=np.conjugate(wynik)*wynik
if len(przefiltrowany2) % 256 == 0:
    f = np.linspace(0, 256, len(przefiltrowany2))
else:
    f = np.linspace(0, 200, len(przefiltrowany2))
plt.figure()
plt.plot(f, wynik)
plt.xlim([0, 50])
plt.xlabel("czestotliwosc [Hz]")
plt.ylabel(r'PSD [$\mu V^2$/Hz]')

plt.show()
