Cards=["A","K","Q","J",2,3,4,5,6,7,8,9,10]

print('Cards:-', Cards)

print('\nSolve The DSA : - We have 13 card at which position card is 5 you have to check by turing minimum cards\n')

CheckCard=int(input("Enter Card Which You Want To Test :-\t"))
#We have 13 card at which position card is 5 you have to check by turing minimum cards

NoOfCard=len(Cards)
CheckedCardList=[]
PostionOfTheCard=''
NoOfCardTurned=''

for cardno in range(0,NoOfCard,1):
    #print(Cards[cardno])
    CheckedCardList.append(cardno)
    if Cards[cardno]==CheckCard:
        NoOfCardTurned=len(CheckedCardList)
        PostionOfTheCard=cardno
        print('\nNo OF Cards Turned By Using Linear Search Algorithm :-' ,NoOfCardTurned)
        print('\nPosition OF Card 5 By Using Linear Search Algorithm :-' ,PostionOfTheCard)
        break
    if CheckCard not in Cards:
        print('You Entered The Invalid Card Please Check')
        break

