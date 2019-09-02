from corpora import CharEncoder, extract_shakespeare_data
from random import seed, shuffle
from model import CharRNN
from train import train
import argparse
import pdb

def main():
    parser = argparse.ArgumentParser("Char-RNN on the complete works of Shakespeare")
    parser.add_argument("--test", type=bool, default=False,
            help = "if true, keep only a thousand lines from the Shakespeare corpus")

    args = parser.parse_args()

    seed(1616)
    
    text, corpus, lines = extract_shakespeare_data("data/t8.shakespeare.txt")
    if args.test:
        print("Downsizing training data...")
        lines = lines[:1000]
    char_encoder = CharEncoder(corpus)
    sequences = char_encoder.encode_sequences(lines, 70)

    shuffle(sequences)
    n_training_sequences = int(.9 * len(sequences))
    training = sequences[:n_training_sequences]
    validation = sequences[n_training_sequences:]

    hidden_size = 100
    rnn = CharRNN(char_encoder.n_chars, hidden_size)
    train(rnn, training, validation, epochs = 3, lr = 0.01, evaluate_per = 1, batch_size = 20) 
    pdb.set_trace()

if __name__ == "__main__":
    main()
