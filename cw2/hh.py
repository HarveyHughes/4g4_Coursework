from numpy import exp as exp

def  alpha_m(V):
    an =(2.5-0.1*(V+65)) / (exp(2.5-0.1*(V+65)) -1)
    return an

def beta_m(V):
    bm = 4*exp(-(V+65)/18)
    return bm

def alpha_h(V):
    ah = 0.07*exp(-(V+65)/20)
    return ah

def beta_h(V):
    bh = 1./(exp(3.0-0.1*(V+65))+1)
    return bh

def alpha_n(V):
    an = (0.1-0.01*(V+65)) / (exp(1-0.1*(V+65)) -1)
    return an

def beta_n(V):
    bn = 0.125*exp(-(V+65)/80)
    return bn
