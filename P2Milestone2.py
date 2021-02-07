#displays the main menu choices
def print_menu():
    print('Main Menu')
    print('1. Insert an indel\n2. Remove an indel\n3. Score similarity\n4. Suggest indel\n5. Quit')

#asks the user which menu choice they would like to execute
#if the input is not in the range of menu choices (1-5 inclusive) it will ask again until the user enters the correct value
def get_menu_choice():
    user_option = int(input('Please choose an option: '))
    while user_option not in range(1,6):
        user_option = int(input('Please choose an option: '))
    return user_option

#asks the user which sequence they would like to use
#if the number is not valid (not 1 or 2) it will continue to ask the user until it recieves correct input
def get_sequence_number():
    sequence_choice = int(input('Sequence 1 or 2? '))
    while sequence_choice not in range(1,3):
        sequence_choice = int(input('Sequence 1 or 2? '))
    return sequence_choice

#asks the user to chose a position to insert an indel
#if the position is not in the range of numbers between 1 and the length of the string (inclusive) the function will continue to ask the user
def get_insert_position(sequence):
    position = int(input('Please choose a position: '))
    while position not in range(1,len(sequence)):
        position = int(input('Please choose a position: '))
    return position

#displays sequences as they are passed into the function
def print_new_sequences(sequence1,sequence2):
    print('Sequence 1: ',sequence1)
    print('Sequence 2: ',sequence2)

#validates the remove position based on the sequence length and whether the position represents an inserted indel
#if the remove position is not valid(it is not an existing index or the index does not represent an indel), the function 
# will continue to ask the user for a position until it is valid
def get_remove_position(sequence):
    remove_position = int(input('Please choose a position: '))
    while remove_position not in range(1,len(sequence)+1):
        remove_position = int(input("\n"'Please choose a position: '))
    while sequence[remove_position-1] != '-':
        remove_position = int(input("\n"'Please choose a position: '))
    return remove_position

#removes the indel from the passed sequence at a specified index
#converts sequence to a list to make it mutable, returns the joined list
#we use the list method .pop() here because this method uses indexing; we dont know what we are removing but we do know where we want to remove
def remove_indel(sequence,index):
    new_sequence = list(sequence)
    new_sequence.pop(index)
    return "".join(new_sequence)

#only called with menu choice 2, which returns a copy of the sequence with the padded indel
#since both sequences need to remain the same lenth, this function removes the padding given when adding an indel
def remove_last_character(sequence):
    return sequence[:-1]

#calculating the indel position that will result in the most matches between the two sequences
#the parameter sequence is the sequence chosen by the user
def find_optimal_indel_position(sequence, other_sequence):
    count = []
    #loops through the length of the sequence inserting an indel and removing it after the number of matches has been counted
    #it then joins the sequence with the inserted indel and calls the count_matches function 
    #the returned count from that function gets stored into a list
    #the indexes of the counts list represent the indexes of the indel insertion into the sequence
    #finally, the function returns the index of the maximum in the counts list and adds 1 (positions start from 1 and indexes start from 0)
    for i in range(len(sequence)+1):
        sequence=list(sequence)
        sequence.insert(i,'-')
        sequence = "".join(sequence)
        count.append(count_matches(sequence,other_sequence+'-'))
        sequence = remove_indel(sequence,i)
    return (count.index(max(count)) +1)

#lets the user know which position is optimal for the chosen sequence
def print_optimal_indel_position(sequence,position):
    print('Insert an indel into Sequence',sequence,'at position',position,end=".""\n")

#returns sequence with specified number of '-' trailing
def pad_with_indels(sequence,num): 
    return sequence+('-'*num)

#converts both sequences into lists with all capital letters
# loops through both sequences and lowercases the matching elements
#returns a sequence with lower and uppercase letters based on its similarity to the second sequence passed
def find_matches(sequence1,sequence2):
    list1 = list(sequence1.upper())
    list2 = list(sequence2.upper())
    for c in range(len(list1)):
        if list1[c] == list2[c]:
            list1[c] = list1[c].lower()
    return "".join(list1)

#returns copy of sequence with inserted indel in specified index - 1            
def insert_indel(sequence,index):
    sequence = list(sequence)
    sequence.insert(index,'-')
    return "".join(sequence)

#makes a copy of two sequences in all uppercase - A != a, even though they are a match
def count_matches(sequence1,sequence2):
    count = 0
    sequence1=sequence1.upper()
    sequence2=sequence2.upper()
    for c in range(len(sequence1)):
    #if there is a match (not including indels), the count goes up by 1, if there are no matches, the function will return 0
        if sequence1[c] == sequence2[c] and sequence1[c] != "-":
            count+=1
    return count

#function that prints similarity score when called (when the user chooses 3 on main menu)
def print_matches(matches,mismatches,match_rate):
    print('Similarity: ',matches,'matches,',mismatches,'mismatches.',"{:.1f}".format(match_rate)+"% match rate.")

if __name__ == "__main__":
    #this piece of code before the while loop will only happen once, therefore it is not included
    sequence1 = input('Please enter DNA Sequence 1: ')
    sequence2 = input('Please enter DNA Sequence 2: ')
    #determines which sequence is longer, and passes the shorter sequence with the number of short characters
    if len(sequence1) > len(sequence2):
        sequence2 = pad_with_indels(sequence2,len(sequence1)-len(sequence2))
    elif len(sequence2) > len(sequence1):
        sequence1 = pad_with_indels(sequence1, len(sequence2)-len(sequence1)) 
    sequence1 = find_matches(sequence1,sequence2)
    sequence2 = find_matches(sequence2,sequence1)
    print()
    print_new_sequences(sequence1,sequence2)
    #setting user choice equal to a number that will always enter the while loop
    user_choice = 1
    #this loop will always execute first, but if the user enters 5 as their choice, it will exit the loop
    while user_choice != 5:
        print()
        print_menu()
        print()
        user_choice = get_menu_choice()
        print()
        if user_choice == 1:
            sequence_number = get_sequence_number()
            if sequence_number == 1:
                position = get_insert_position(sequence1)
                #creating a new sequence 1 with indel inserted at the specified position
                #in order for the sequences to maintain the same length, sequence 2 must have a - placed at the end of it
                sequence1 = insert_indel(sequence1,position-1)
                sequence2 = sequence2+'-'
            #if the sequence_number function did not return 1, it must have returned a validated 2, so sequence 2 would have the inserted indel
            else:
                position = get_insert_position(sequence2)
                sequence2 = insert_indel(sequence2,position-1)
                sequence1 = sequence1+'-'
            print()
            sequence1 = find_matches(sequence1,sequence2)
            sequence2 = find_matches(sequence2,sequence1)
            print_new_sequences(sequence1,sequence2)
        if user_choice == 2:
            #the remove position needs to be validated with a sequence chosen by the user
            sequence_number = get_sequence_number()
            if sequence_number == 1:
                remove_position = get_remove_position(sequence1)
                sequence1 = remove_indel(sequence1,remove_position-1)
                sequence2 = remove_last_character(sequence2)
            else:
                remove_position = get_remove_position(sequence2)
                sequence2 = remove_indel(sequence2,remove_position-1)
                sequence1 = remove_last_character(sequence1)
            print()
            sequence1 = find_matches(sequence1,sequence2)
            sequence2 = find_matches(sequence2,sequence1)
            print_new_sequences(sequence1,sequence2)
        if user_choice == 3:
            matches = count_matches(sequence1,sequence2)
            mismatches = len(sequence1)-matches
        #calculating the match rate; number of matches / total characters * 100
            match_rate = (matches / len(sequence1) )* 100
            print_matches(matches,mismatches,match_rate)
            print()
            print_new_sequences(sequence1,sequence2)
        if user_choice == 4:
            sequence_choice = get_sequence_number()
            if sequence_choice == 1:
                position = find_optimal_indel_position(sequence1,sequence2)
                print_optimal_indel_position(sequence_choice,position)
                optimal_sequence = insert_indel(sequence1,position-1)
                other_sequence = sequence2
            else:
                position = find_optimal_indel_position(sequence2,sequence1)
                print_optimal_indel_position(sequence_choice,position)
                optimal_sequence = insert_indel(sequence2,position-1)
                other_sequence = sequence1
            matches = count_matches(optimal_sequence,other_sequence+'-')
            match_rate = (matches / len(optimal_sequence) )* 100
            print_matches(matches,(len(optimal_sequence)-matches),match_rate)
            print()
            print_new_sequences(sequence1,sequence2)




            







