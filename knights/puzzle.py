from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

universal_knowledge = And(
    # A symbol can noly be a knight or a knave
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),
    Or(And(CKnight, Not(CKnave)), And(Not(CKnight), CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    universal_knowledge,
    # A says: And(AKnight, AKnave)
    # if A is a knight what it says it's true
    Implication(AKnight, And(AKnight, AKnave)),
    # if A is a knave then what it says is a lie
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    universal_knowledge,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    universal_knowledge,
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(BKnight, And(BKnight, AKnave)),
    Implication(AKnave, And(AKnave, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
ASaidImKnave = Symbol("A said 'I am a knave'")
ASaidImKnight = Symbol("A said 'I am a knight'")

knowledge3 = And(
    universal_knowledge,
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # If A is a Knave then he would say "I am a Knight" because he has to lie
    Implication(AKnave, And(ASaidImKnight, Not(ASaidImKnave))),
    # If A is a Knight then he would say "I am a Knight" beauce he has to tell the truth
    Implication(AKnight, And(ASaidImKnight, Not(ASaidImKnave))),
    
    # B says "A said 'I am a knave'."
    # If B is a knight A said "I am a Knave"
    Implication(BKnight, ASaidImKnave),
    # If B is a knave A said "I am a Knight"
    Implication(BKnave, ASaidImKnight),
    
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    
    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),  # A is a Knave because it cannot be both a Knave and a Knight at the same time, therefore it is telling a lie 
        ("Puzzle 1", knowledge1),  # A is a Knave and B is a Knight. "We are both Knaves" cannot be true because if it was true that would mean that A is a Knight, since it's telling the truth, therefore A is a knave. Since A is a Knave and the sentence it says is a lie, B has to be a Knight since if it was a Knave the sentence would be true
        ("Puzzle 2", knowledge2),  # A is a Knave and B is a Knight. If what A says ("We are the same kind") is true, then what B says would also have to be true. Since what B is saying ("we are of different kinds") cannot be true if A is telling the truth, B would have to be lying. Therefore B would be a knave. But if B is a knave then they would be of different kinds. Therefore B is telling the truth and A is lying 
        ("Puzzle 3", knowledge3)  # A and C are knights and B is a Knave. If C is lying, then A is a Knave. If C is lying then it is a Knave, if both C and A are knaves, what B is saying cannot be both true or both false. That's a contradiction. So C is a knight, and therefore A is a knight, and B is lying. 
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
