def pad_with_indels(sequence,num):
    #returns sequence with specified number of '-' trailing 
    return sequence+('-'*num)

#converts both sequences into lists with all capital letters
# loops through both sequences and lowercases the matching elements
def find_matches(sequence1,sequence2):
    list1 = list(sequence1.upper())
    list2 = list(sequence2.upper())
    for c in range(len(list1)):
        if list1[c] == list2[c]:
            list1[c] = list1[c].lower()
    return "".join(list1)
                
def insert_indel(sequence,index):
    #returns copy of sequence with inserted indel in specified index - 1
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

if __name__ == "__main__":
    sequence1 = input('Please enter DNA Sequence 1: ')
    sequence2 = input('Please enter DNA Sequence 2: ')
#determines which sequence is longer, and passes the shorter sequence with the number of short characters
    if len(sequence1) > len(sequence2):
        sequence2 = pad_with_indels(sequence2,len(sequence1)-len(sequence2))
    elif len(sequence2) > len(sequence1):
        sequence1 = pad_with_indels(sequence1, len(sequence2)-len(sequence1)) 
    print()
    sequence1 = find_matches(sequence1,sequence2)
    print('Sequence 1: ',sequence1)
    sequence2 = find_matches(sequence2,sequence1)
    print("\n"'Sequence 2: ',sequence2)
    matches = count_matches(sequence1,sequence2)
    #calculating the match rate; number of matches / total characters * 100
    match_rate = (matches / len(sequence1) )* 100
    print('Similarity: ',matches,'matches,',(len(sequence1)-matches),'mismatches.',"{:.1f}".format(match_rate)+"% match rate.")
    print()
    #creating a new sequence with indel inserted at the specified location
    indel_sequence = insert_indel(sequence1,int(input('Please enter an indel location for Sequence 1: '))-1)
    print("\n"'Sequence 1: ',find_matches(indel_sequence,sequence2+'-'))
    print("\n"'Sequence 2: ',find_matches(sequence2+'-',indel_sequence))
    print()
    matches = count_matches(indel_sequence,sequence2+'-')
    match_rate = (matches/ len(indel_sequence) ) *100
    print('Similarity: ',matches,'matches,',(len(indel_sequence)-matches),'mismatches.',"{:.1f}".format(match_rate)+"% match rate.")