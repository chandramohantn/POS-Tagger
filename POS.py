"""
Author: CHANDRAMOHAN T N
File: POS.py 
"""

import Utilities
import HMM

def main():
    folder = 'C:\Users\Chandramohan\Desktop\@IIT\POS Tagger\Data'
    data_file = folder + '\Data.txt'
    inp_file = folder + '\Train.txt'
    out_file = folder + '\Test.txt'

    # Creating vocabulary
    data, tags = Utilities.Get_data(data_file)
    d_vocab, t_vocab = Utilities.Get_vocabulary(data, tags)

    # Get train data
    data, tags = Utilities.Get_data(inp_file)
    train_d, train_t = Utilities.Convert_data(data, tags, d_vocab, t_vocab)

    # Get test data
    data, tags = Utilities.Get_data(out_file)
    test_d, test_t = Utilities.Convert_data(data, tags, d_vocab, t_vocab)

    # Training    
    hmm = HMM.HMM(train_d, train_t, d_vocab, t_vocab)
    p_t = []
    for i in range(len(test_d)):
        seq = hmm.Viterbi(test_d[i])
        p_t.append(seq)
        Utilities.Accuracy_item(seq, test_t[i])
    Utilities.Accuracy_model(p_t, test_t)

if __name__ == "__main__":
    main()


