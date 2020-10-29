import typing

def distance_of_nearest_repeated_entry(s):

    # Maps each word to the latest index it has appeared at
    word_to_latest_index = {}

    # Initially, the distance would be infinity
    nearest_repeated_distance = float("inf")

    for i, word in enumerate(s):

        # If the current word has been seen before
        if word in word_to_latest_index:
            # If a new closest distance between pairs of words is found, update the distance
            nearest_repeated_distance = min(nearest_repeated_distance, i - word_to_latest_index[word])

        # Update the latest index of the word
        word_to_latest_index[word] = i

    # Return -1 if no pairs of words repeated.
    return typing.cast(int, nearest_repeated_distance) if nearest_repeated_distance != float("inf") else -1



def main():
   s = ["class", "object", "method", "variable", "method", "method", "object"]
   assert(distance_of_nearest_repeated_entry(s) == 1)

   s = ["object", "class", "file"]
   assert(distance_of_nearest_repeated_entry(s) == -1)



if __name__ == "__main__":
    main()
