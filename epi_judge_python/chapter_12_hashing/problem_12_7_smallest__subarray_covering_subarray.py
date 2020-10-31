import collections

def smallest_sequentially_covering_subset(paragraph, keywords):

    # Map each keyword to its index in the keywords array.
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}

    # The ith entry contains the index into paragraph of
    # the latest occurrence of the ith keyword
    latest_occurrence = [-1] * len(keywords)

    # The ith entry contains the length of the shortest subarray
    # that ends with the ith keyword and that contains the 1st to (i-1)th previous keywords.
    shortest_subarray_lengths = [float("inf")] * len(keywords)

    answer = (-1, -1)
    shortest_subarray_length = float("inf")

    for i, word in enumerate(paragraph):
        if word in keyword_to_idx:
            keyword_idx = keyword_to_idx[word]

            # If the keyword is the first keyword:
            if keyword_idx == 0:
                shortest_subarray_lengths[0] = 1

            # If the keywords is not the first keyword and the previous keyword subarray lengths are known
            elif shortest_subarray_lengths[keyword_idx - 1] != float("inf"):
                distance_from_previous_keyword = i - latest_occurrence[keyword_idx - 1]

                shortest_subarray_lengths[keyword_idx] = shortest_subarray_lengths[keyword_idx - 1] + \
                                                         distance_from_previous_keyword

            # Update the latest occurrence of the keyword
            latest_occurrence[keyword_idx] = i

            # If an occurrence of the last keyword has been found and the previous keywords have also all been
            # found in correct sequence, check if a new shortest subarray has been found:
            if keyword_idx == len(keywords) - 1 and shortest_subarray_lengths[-1] < shortest_subarray_length:
                shortest_subarray_length = shortest_subarray_lengths[-1]
                answer = (i - shortest_subarray_length + 1, i)

    return answer



def main():
    paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
    keywords = {"b", "c"}




if __name__ == "__main__":
    main()
