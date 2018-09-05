from allennlp.modules.elmo import Elmo, batch_to_ids

options_file = "/home/tian/Documents/external/allennlp/model_weights/elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "/home/tian/Documents/external/allennlp/model_weights/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

elmo = Elmo(options_file, weight_file, 2, dropout=0)

sentences = [['First', 'sentence', '.'], ['Another', '.']]
character_ids = batch_to_ids(sentences)

embeddings = elmo(character_ids)

print(embeddings)

