# Day One

#Part 1

column1 = []
column2 = []

# Open the file and process each line
with open('dayone.txt', 'r') as f:
    for line in f:
        # Split the line into two values
        values = line.split()
        # Append the values to the respective lists
        column1.append(int(values[0]))
        column2.append(int(values[1]))

# Print the lists to verify
column1.sort()
column2.sort()

sums = 0
# for i, number in enumerate(column1):
#     sums += abs(number - column2[i])

# print(sums)

#Part 2

counter = 0
sum = 0
for col1Value in column1:
    numberofTimes = 0
    if counter > len(column2):
        break

    while ((col1Value > column2[counter]) and (counter < len(column2))):
        counter += 1
        if counter == len(column2):
            break
    
    if counter == len(column2):
        break
    while ((col1Value == column2[counter]) and (counter < len(column2))):
        numberofTimes += 1
        counter += 1
    
    sum += numberofTimes * col1Value

print(sum)
    
#Time: 32:38
