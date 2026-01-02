Cards=[1,2,3,4,5,6,7,8,9,10]
#Index positions: [0,1,2 ,3,4,5,6,7,8,9]
NoOfCards=len(Cards)
Low=0
High=NoOfCards-1

CheckMin=int(input("Enter Card Which You Want To Test :-\t"))
#print(Low,High,Mid)
#print(Cards[Low],Cards[High],Cards[Mid])

for each_check in range(NoOfCards):
    Mid=(Low+High)//2
    if Cards[Mid]==CheckMin:
        print('Found at Iteration :- ',each_check+1)
        print('Position of Card :-', Mid)
        break
    elif Cards[Mid]>CheckMin:
        High=Mid-1
    elif Cards[Mid]<CheckMin:
        Low=Mid+1
else:
    print("Card not found in the list.")
