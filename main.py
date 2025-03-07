# min = 100
# max = 1000
count = 0
min , max = map (int , input().split())

while min < max :

    #sum = (min%10) + (min//100) + (( ( min - (    min % 10  ) ) % 100 ) // 10)
    #print ( min , sum)
    sum = 0
    min = str(min)
    for char in min :
        sum = sum + int(char)

    min = int(min)
    
    if sum == 2 :
        print ( min , "=" , sum )
        min = min + 1
        count = count + 1
    elif sum == 1 :
        min = min + 1
        #count = count + 1
    
    sum = 0
    min = str(min)
    for char in min :
        sum = sum + int(char)
        
    min = int(min)

    i = 2

    while i <= sum :
        if i == sum :
            print ( min , "=" , sum )
            i = sum + 1
            min = min + 1
            count = count + 1
        elif sum%i == 0 :
            min = min + 1
            i = sum + 1
        else :
            i = i + 1

print ("tedad adad:" , count)

        

   
