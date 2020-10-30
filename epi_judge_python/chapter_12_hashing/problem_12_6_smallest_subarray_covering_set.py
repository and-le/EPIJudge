import collections

def smallest_subarray_covering_set(paragraph, keywords):

    set_to_cover = collections.Counter(keywords)

    # If there is no such subarray that covers the set, return this interval to indicate
    # no solution.
    interval = (-1, -1)

    # The remaining number of keywords to cover each time we look for a shortest subarray
    num_keywords_to_cover = len(keywords)

    left_idx = 0

    for right_idx, word in enumerate(paragraph):
        if word in keywords:
            set_to_cover[word] -= 1

            # Ensure that we only decrement the number of keywords we need to cover if
            # we have found a new keyword in the set. We don't want to decrement if we found
            # the same keyword 2+ times.
            if set_to_cover[word] >= 0:
                num_keywords_to_cover -= 1

        # This loop runs each time a candidate for shortest subarray is found.
        # num_keywords_to_cover will be 0 because a subarray that covers the set has been identified.
        while num_keywords_to_cover == 0:
            # If the first valid interval has been found OR a shorter subarray has been found
            if interval == (-1, -1) or right_idx - left_idx < interval[1] - interval[0]:
                interval = (left_idx, right_idx)

            # Advance the left_idx until the subarray with indexes (left_idx, right_idx) no longer covers the set
            if paragraph[left_idx] in keywords:
                # Since we are leaving out this keyword now, we need to add 1 back to the number of keywords
                # remaining to cover for subsequent iterations.
                set_to_cover[paragraph[left_idx]] += 1

                # Only increment this for non-repeated keywords in the set.
                if set_to_cover[paragraph[left_idx]] > 0:
                    num_keywords_to_cover += 1

            # Advances the left index
            left_idx += 1


    return interval


def main():
    paragraph = ["a", "b", "a", "a", "d", "c", "a", "d", "b", "a", "c", "d"]
    keywords = {"b", "c"}
    print(smallest_subarray_covering_set(paragraph, keywords))
    assert(smallest_subarray_covering_set(paragraph, keywords) == (8, 10))



if __name__ == "__main__":
    main()
