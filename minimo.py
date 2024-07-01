for m in range(0, 57):
	archivos=[]
	for j in range(0, 5):
	    archivos.append("distaN14/dist-"+str(j+5*m)+".xvg")

	import numpy as np

	a=np.zeros((21, 8))

	for i in range(len(archivos)):
	    t, r = np.loadtxt(archivos[i], comments=("@", "#"), unpack=True)
	    a[:, 0]=t
	    a[:, i+1]=r

	for l in range(0, 21):
	    a[l, len(archivos)+1]=np.min(a[l, 1:len(archivos)+1])
	    a[l, len(archivos)+2]=np.mean(a[l, 1:len(archivos)+1])

	np.savetxt("lista-Na_"+str(8908+m)+".xvg", np.c_[a], fmt='%1.4f')
	    
