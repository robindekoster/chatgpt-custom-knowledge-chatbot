from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader


def load_knowledge():
    # Load data from directory
    documents = SimpleDirectoryReader('knowledge').load_data()
    return documents


def create_index():
    print('Creating new index')
    # Load data
    documents = load_knowledge()
    # Create index from documents
    index = GPTSimpleVectorIndex.from_documents(documents)
    save_index(index)
    return index


def save_index(index):
    # Save index to file
    index.save_to_disk('knowledge/index.json')


def load_index():
    # Load index from file
    try:
        index = GPTSimpleVectorIndex.load_from_disk('knowledge/index.json')
    except FileNotFoundError:
        index = create_index()
    return index


def query_index(index):
    # Query index
    while True:
        prompt = input("Type prompt...")
        response = index.query(prompt)
        print(response)


def main():
    # Ask user if they want to refresh the index
    refresh_index = input("Do you want to refresh the index? (y/n) [n]: ")
    refresh_index = refresh_index.lower() == 'y'

    # If refreshing the index, create new index and save to file
    if refresh_index:
        index = create_index()
    # Otherwise, load index from file
    else:
        index = load_index()

    # Query index
    query_index(index)


if __name__ == '__main__':
    main()
