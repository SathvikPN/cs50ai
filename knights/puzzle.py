from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Hints from CS50AI lecture --------------------
# For each knowledge base, you’ll likely want to encode two different types of information:
# (1) information about the structure of the problem itself (i.e., information given in the definition of a Knight and Knave puzzle),
# (2) information about what the characters actually said.

# Translation to current contexts -----------------
# 1.1 Each character is either a knight or a knave.
# 1.2.1 Every sentence spoken by a knight is true,
# 1.2.2 Every sentence spoken by a knave is false.
# 2. statements given in each puzzle

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # 1.1 A either knight or knave but not both (aka XOR)
    Or(AKnight, AKnave),
    Biconditional(AKnight, Not(AKnave)),

    # 1.2.1 A is knight if statement is true.
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO

    # 1.1 person is either knight or knave but(and) not both (aka XOR)
    And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave))
    ),
    And(
        Or(BKnight, BKnave),
        Not(And(BKnight, BKnave))
    ),

    # 1.2.1
    Biconditional(AKnight, And(AKnave, BKnave)), # IFF A is knight if his statement true (A is knave and B is Knave)

    # if A is Knight, A cannot be Knave (1.1)
    # but if A is not Knave, A's statement is false (1.2)
    # so A is not a Knight
    # Hence A is a Knave (1.3) ==> statement is false ==> Not(And(AKnave, BKnave))
    # Not(And(AKnave, BKnave)) == Or(Not(AKnave), Not(BKnave))
    # from 1.3 Not(AKnave) is false ==> Or(Not(AKnave), Not(BKnave)) = Not(BKnave)
    # hence B is Knight


)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO

    # 1.1 person is either knight or knave but(and) not both (aka XOR)
    # And(
    #     Or(AKnight, AKnave),
    #     Not(And(AKnight, AKnave))
    # ),
    # And(
    #     Or(BKnight, BKnave),
    #     Not(And(BKnight, BKnave))
    # ),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),     


    # 1.2.1
    Biconditional(
        AKnight, 
        Or(
            And(AKnight, BKnight),
            And(AKnave, BKnave),
        )
    ),

    Biconditional(
        BKnight,
        Or(
            And(AKnight, Not(BKnight)),
            And(AKnave, Not(BKnave)),
        )
    ),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO

    # 1.1 Each character is either a knight or a knave.
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),     
    Biconditional(CKnight, Not(CKnave)),     

    # 1.2.1 Every sentence spoken by a knight is true,
    Biconditional(AKnight, Or(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight),

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
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
