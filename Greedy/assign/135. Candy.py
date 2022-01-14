'''
    TOPIC:minimum candies to assign. higher rating have more candies than neighbors.if equal nothing to do
    STEP:
    1.CREATE array size islen(ratings) default 1 since each child have at least one candy
    12two TRAVERSALS from front and back because check both sides' neighbors.from front, if right > left,candy[right]++(mean res++). from back if left > right and candy[left]<= candy[right] candy[left]++(mean res ++)
    
'''
def candy(ratings):
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if (ratings[i-1] > ratings[i]) and (candies[i-1] <= candies[i]):
                candies[i-1] = candies[i] + 1
        return sum(candies)
            
print(candy([1,2,87,87,87,2,1])) #13