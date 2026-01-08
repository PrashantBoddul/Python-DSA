Cards=[8,9,10,1,2,3,4,5,6,7]
######[0,1,2 ,3,4,5,6,7,8,9]
NoOfCards=len(Cards)
Low=0
High=NoOfCards-1

CheckMin=10
#print(Low,High,Mid)
#print(Cards[Low],Cards[High],Cards[Mid])

for eachcheck in range(NoOfCards):
    Mid=(Low+High)//2
    if Cards[Mid]==CheckMin:
        print('Found At Iteration',eachcheck)
        break
    if Cards[Mid]<=Cards[High]:
        if Cards[Mid]<CheckMin<=Cards[High]:
            Low=Mid+1
        else:
            High=Mid-1
    if Cards[Low]<=Cards[Mid]:
        if Cards[Low]<=CheckMin<Cards[Mid]:
            High=Mid-1
        else:
            Low=Mid+1
