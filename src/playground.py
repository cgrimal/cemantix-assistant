# Third party
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    "data/frWac_no_postag_no_phrase_500_cbow_cut100.bin",
    binary=True,
    unicode_errors="ignore",
)

for word, _ in model.most_similar(
    [
        "resserrer",
        # "nouer",
        # "tisser",
        # "renforcer",
        # "maintenir",
        # "consolider",
        # "élargir",
        # "lier",
        # "intensifier",
        # "conforter",
        # "entretenir",
        # "oeuvrer",
        # "accroître",
        # "encourager",
        # "contribuer",
        # "promouvoir",
        # "dynamiser",
        # "soutenir",
        # "favoriser",
        # "développer",
        # "perpétuer",
        # "détacher",
        # "stimuler",
        # "concrétiser",
        # "faciliter",
        # "fédérer",
        # "diversifier",
        # "fixer",
        # "pérenniser",
        # "éloigner",
        # "améliorer",
    ],
    [
        # "fait",
        # "status",
        # "téléphone",
        # "verbe",
        # "affaire",
    ],
    30,
):
    print(word)
