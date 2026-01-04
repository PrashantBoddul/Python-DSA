Cards = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

CheckCard = int(input("Enter Card Which You Want To Test :-\t"))

NoOfCards = len(Cards)
CheckedCardList = []
PositionOfTheCard = -1

for cardno in range(NoOfCards):
    CheckedCardList.append(Cards[cardno])
    print(Cards[cardno], CheckCard)

    if Cards[cardno] == CheckCard:
        PositionOfTheCard = cardno
        print("\n Number of Cards Turned By Using Linear Rotated Search Algorithm :-", len(CheckedCardList))
        print(" Position of Card", CheckCard, "By Using Linear Rotated Search Algorithm :-", PositionOfTheCard)
        break

if PositionOfTheCard == -1:
    print("\n You Entered an Invalid Card. Please Check.")
