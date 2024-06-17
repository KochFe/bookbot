def main():
    path="books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    unique_chars_dict = get_unique_characters(text)
    dict_list = sort_dict(unique_chars_dict)

    #return every unique char in a nice way:
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words were found in the document")
    print("")
    for i in range(len(dict_list)):
        if dict_list[i]["char"].isalpha():
            print(f"The'{dict_list[i]["char"]}‘ character was found {dict_list[i]["count"]} times")
    print("--- End report ---")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return(f.read())

def get_word_count(text: str):
    word_list = text.split()
    return(len(word_list))

def get_unique_characters(text):
    count_dict = {}
    no_space_string = "".join(text.lower().split())
    unique_list = list(set(no_space_string))
    for c in unique_list:
        count_dict[c] = no_space_string.count(c)
    return(count_dict)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    dict_list = []
    for pair in dict:
        temp_dict = {"char":pair, "count":dict[pair]}
        dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


main()