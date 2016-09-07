"""
Author: CHANDRAMOHAN T N
File: HMM.py 
"""

import numpy

class HMM:
    def __init__(self, d, t, d_v, t_v):
        self.i_prob = []                         # initial state probability
        self.t_prob = []                         # transition probability
        self.e_prob = []                         # emmision probability

        N = len(t_v)
        M = len(d_v)
        self.i_prob = [0.001] * N
        tot = 0
        
        for i in range(N):
            self.i_prob[t[i][0]] += 1
        self.i_prob = numpy.array(self.i_prob)
        self.i_prob = self.i_prob / N
        self.i_prob = self.i_prob.tolist()
        
        for i in range(N):
            self.t_prob.append([])
            for j in range(N):
                self.t_prob[i].append(tot)

        for i in range(N):
            self.e_prob.append([])
            for j in range(M):
                self.e_prob[i].append(tot)

        for i in t:
            for j in range(len(i) - 1):
                self.t_prob[i[j]][i[j+1]] += 1

        for i in range(len(d)):
            for j in range(len(d[i])):
                if len(d[i]) == len(t[i]):
                    self.e_prob[t[i][j]][d[i][j]] += 1

        self.t_prob = numpy.array(self.t_prob)
        self.e_prob = numpy.array(self.e_prob)
        for i in range(len(self.t_prob)):
            tot = self.t_prob[i]
            self.t_prob[i] = (self.t_prob[i] + 1) / (tot + N)
        for i in range(len(self.e_prob)):
            tot = self.e_prob[i]
            self.e_prob[i] = (self.e_prob[i] + 1)/ (tot + M)
        self.t_prob = self.t_prob.tolist()
        self.e_prob = self.e_prob.tolist()
        print('Parameters estimated ......')

    def Forward(i_p, t_p, e_p, d, t):
        alfa = [[]]
        N = len(i_p)

        for i in range(N):
            alfa[0].append(i_p[i] * e_p[i][d[0]])

        t = 1
        while t < len(d):
            alfa.append([])
            for i in range(N):
                tot = 0.0
                for j in range(N):
                    tot = tot + alfa[t-1][j] * t_p[i][j]
                alfa[t].append(tot * e_p[i][d[t]])
            t = t + 1
            
        return alfa

    def Backward(i_p, t_p, e_p, d, t):
        beta = []
        N = len(i_p)

        for i in range(len(d)):
            beta.append([])
        for i in range(N):
            beta[len(d) - 1].append(1.0)

        t = len(d) - 2
        while t >= 0:
            for i in range(N):
                tot = 0.0
                for j in range(N):
                    tot  = tot + t_p[i][j] * e_p[j][d[t]] * beta[t+1][j]
                beta[t].append(tot)
            t = t - 1

        return beta

    def Viterbi(self, d):
        delta = [[]]
        seq = [[]]
        N = len(self.i_prob)
        tags = []

        for i in range(N):
            delta[0].append(self.i_prob[i] * self.e_prob[i][d[0]])
            seq[0].append(i)                            

        t = 1
        while t < len(d):
            delta.append([])
            seq.append([])
            for i in range(N):
                a = 0.0
                k = 0
                for j in range(N):
                    b = delta[t-1][j] * self.t_prob[i][j]
                    if b > a:
                        a = b
                        k = j
                delta[t].append(a * self.e_prob[i][d[t]])
                seq[t].append(k)
            t = t + 1
        idx = (delta[t-1]).index(max(delta[t-1]))
        for i in seq:
            tags.append(i[idx])
        return tags

    def Baum_welch(alfa, beta, i_p, t_p, e_p, d, t):
        efsi = []
        N = len(i_p)
        M = len(e_p[0])

        deno1 = []
        for t in range(len(o) - 1):
            efsi.append([])
            tot = 0.0
            for i in range(N):
                efsi[t].append([])
                for j in range(N):
                    efsi[t][i].append(alfa[t][i] * t_p[i][j] * e_p[j][w.index(o[t+1])] * beta[t+1][j])
                    tot = tot + efsi[t][i][j]
            if tot == 0.0:
                tot = deno1[t-1]
            deno1.append(tot)

        deno2 = []
        for t in range(len(o)):
            tot = 0.0
            for i in range(N):
                tot = tot + alf[t][i] * beta[t][i]
            if tot == 0.0:
                tot = deno2[t-1]
            deno2.append(tot)

        for t in range(len(o)-1):
            j = []
            for i in efsi[t]:
                k = [float(float(a) / deno1[t]) for a in i]
                j.append(k)
            efsi[t] = j

        gamma = []
        for t in range(len(d)):
            gamma.append([])
            for i in range(N):
                tot = float((alfa[t][i] * beta[t][i]) / deno2[t])
                gamma[t].append(tot)

        for i in range(N):
            i_p[i] = gamma[0][i]

        for i in range(N):
            for j in range(N):
                tot1 = 0.0
                tot2 = 0.0
                for t in range(len(o) - 1):
                    tot1 = tot1 + efsi[t][i][j]
                    tot2 = tot2 + gamma[t][i]
                t_p[i][j] = float(tot1 / tot2)

        for i in range(N):
            for j in range(M):
                tot1 = 0.0
                tot2 = 0.0
                for t in range(len(o)):
                    if o[t] == w[j]:
                        tot1 = tot1 + gamma[t][i]
                    tot2 = tot2 + gamma[t][i]
            e_p[i][j] = float(tot1 / tot2)
                            
        return i_p, t_p, e_p



