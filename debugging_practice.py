



def main():

    def remove_keys_containing_string(dictionary, remove):
            new_dictionary = {}
            for key in dictionary:
                if remove == key:
                    new_dictionary[key] = dictionary[key]

    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    remove_keys_containing_string(dictionary, "coding")
    print(dictionary)




if __name__ == '__main__':
    main()