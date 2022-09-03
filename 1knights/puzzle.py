from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
B = And(Biconditional(BKnave, Not(BKnight)), Biconditional(BKnight, Not(BKnave)), (Or(BKnave, BKnight)))

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
C = And(Biconditional(CKnave, Not(CKnight))).add(Biconditional(CKnight, Not(CKnave))).add(Or(CKnave, CKnight))

knowledgebase = And(  # A
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(AKnight, Not(AKnave)),
    Or(AKnave, AKnight),  # 1 sentence

    # B
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Or(BKnave, BKnight),

    Biconditional(CKnave, Not(CKnight)),
    Biconditional(CKnight, Not(CKnave)),
    Or(CKnave, CKnight))
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledgebase,

    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledgebase,

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledgebase,

    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(BKnight, (Or(And(AKnave, BKnight), And(AKnight, BKnave)))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # 4
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),

    # 3
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # 2
    Or(Implication(BKnight,
                   Or(Implication(AKnight, AKnave),
                      Implication(AKnave, Not(AKnave)))),
       Implication(BKnave,
                   Not(Or(Implication(AKnight, AKnave),
                          Implication(AKnave, Not(AKnave)))))),

    # 1
    Implication(AKnight, Or(AKnave, AKnight)),
    Implication(AKnave, Not(Or(AKnave, AKnight))),

    knowledgebase

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"\t{symbol}")


if __name__ == "__main__":
    main()
