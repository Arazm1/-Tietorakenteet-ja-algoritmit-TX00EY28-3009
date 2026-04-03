vowels = ['a', 'e', 'i', 'o', 'u']
count = 0;

user_input = input();

lower_cased = user_input.lower();

for i in lower_cased:
    #print(i);
    for j in vowels:
        #print(j);
        if(i == j):
            count+=1;
    

print(f"Number of vowels: {count}");