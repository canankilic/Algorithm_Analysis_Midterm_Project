# Canan Kılıç 220201037
import pandas as pd  # to read .csv files
import time  # to measure the time taken for the process

def read_csv_files(dataset):
    return pd.read_csv(dataset)

def binary_search_algorithm(array, target):  # search for an exact document
    left, right = 0, len(array) - 1
    while left <= right:
        middle_point = (left + right) // 2  # find the middle point to halve
        if array[middle_point]['Document ID'] == target:
            return array[middle_point]  # return found document
        elif array[middle_point]['Document ID'] < target:
            left = middle_point + 1
        else:
            right = middle_point - 1
    return None

def linear_search_algorithm(array, target):  # search for a partial match in document titles and author
    found_documents = []
    for govern_doc in array:
        if isinstance(target, str) and isinstance(govern_doc['Document Title'], str) and isinstance(govern_doc['Author'], str):
            if (target.lower() in govern_doc['Document Title'].lower() or
                    target.lower() in govern_doc['Author'].lower()):
                found_documents.append(govern_doc)  # append found documents
    return found_documents

def save_results_to_csv(results, filename):
    # save found documents as .csv
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

def main():
    dataset_small = read_csv_files('document_archive.csv').to_dict('records')
    dataset_mid = read_csv_files('document_archive1.csv').to_dict('records')
    dataset_large = read_csv_files('document_archive2.csv').to_dict('records')
    dataset_xlarge = read_csv_files('document_archive3.csv').to_dict('records')

    # sort datasets if not sorted
    small_data_sorted = sorted(dataset_small, key=lambda x: x['Document ID'])
    mid_data_sorted = sorted(dataset_mid, key=lambda x: x['Document ID'])
    large_data_sorted = sorted(dataset_large, key=lambda x: x['Document ID'])
    very_large_data_sorted = sorted(dataset_xlarge, key=lambda x: x['Document ID'])

    search_num = 10  # target ID for binary search
    search_word = "Author 3"  # keyword for partial match in linear search

    exact_results_small = [] #containers to hold data
    exact_results_mid = []
    exact_results_large = []
    exact_results_very_large = []

    print("Testing Exact Match on Small Dataset:")
    start_time = time.time()
    result_exact_small = binary_search_algorithm(small_data_sorted, search_num)
    binary_time_small = time.time() - start_time
    print(f"Binary Search Time (Exact Match): {binary_time_small:.10f} seconds")

    if result_exact_small:  # only add if a document is found
        exact_results_small.append(result_exact_small)

    # repeat this steps for mid, large, and very large datasets
    print("Testing Exact Match on Mid Dataset:")
    start_time = time.time()
    result_exact_mid = binary_search_algorithm(mid_data_sorted, search_num)
    binary_time_mid = time.time() - start_time
    print(f"Binary Search Time (Exact Match): {binary_time_mid:.10f} seconds")

    if result_exact_mid:
        exact_results_mid.append(result_exact_mid)

    print("Testing Exact Match on Large Dataset:")
    start_time = time.time()
    result_exact_large = binary_search_algorithm(large_data_sorted, search_num)
    binary_time_large = time.time() - start_time
    print(f"Binary Search Time (Exact Match): {binary_time_large:.10f} seconds")

    if result_exact_large:
        exact_results_large.append(result_exact_large)

    print("Testing Exact Match on Very Large Dataset:")
    start_time = time.time()
    result_exact_very_large = binary_search_algorithm(very_large_data_sorted, search_num)
    binary_time_very_large = time.time() - start_time
    print(f"Binary Search Time (Exact Match): {binary_time_very_large:.10f} seconds")

    if result_exact_very_large:
        exact_results_very_large.append(result_exact_very_large)

    partial_results_small = []
    partial_results_mid = []
    partial_results_large = []
    partial_results_very_large = []

    print("\nTesting Partial Match on Small Dataset:")
    start_time = time.time()
    result_partial_small = linear_search_algorithm(small_data_sorted, search_word)
    linear_time_small = time.time() - start_time
    print(f"Linear Search Time (Partial Match): {linear_time_small:.10f} seconds")
    partial_results_small.extend(result_partial_small)

    print("Testing Partial Match on Mid Dataset:")
    start_time = time.time()
    result_partial_mid = linear_search_algorithm(mid_data_sorted, search_word)
    linear_time_mid = time.time() - start_time
    print(f"Linear Search Time (Partial Match): {linear_time_mid:.10f} seconds")
    partial_results_mid.extend(result_partial_mid)

    print("Testing Partial Match on Large Dataset:")
    start_time = time.time()
    result_partial_large = linear_search_algorithm(large_data_sorted, search_word)
    linear_time_large = time.time() - start_time
    print(f"Linear Search Time (Partial Match): {linear_time_large:.10f} seconds")
    partial_results_large.extend(result_partial_large)

    print("Testing Partial Match on Very Large Dataset:")
    start_time = time.time()
    result_partial_very_large = linear_search_algorithm(very_large_data_sorted, search_word)
    linear_time_very_large = time.time() - start_time
    print(f"Linear Search Time (Partial Match): {linear_time_very_large:.10f} seconds")
    partial_results_very_large.extend(result_partial_very_large)

    # save found results to .csv
    if exact_results_small:
        save_results_to_csv(exact_results_small, 'government_archive_small_exact.csv')

    if partial_results_small:
        save_results_to_csv(partial_results_small, 'government_archive_small_partial.csv')

    if exact_results_mid:
        save_results_to_csv(exact_results_mid, 'government_archive_mid_exact.csv')

    if partial_results_mid:
        save_results_to_csv(partial_results_mid, 'government_archive_mid_partial.csv')

    if exact_results_large:
        save_results_to_csv(exact_results_large, 'government_archive_large_exact.csv')

    if partial_results_large:
        save_results_to_csv(partial_results_large, 'government_archive_large_partial.csv')

    if exact_results_very_large:
        save_results_to_csv(exact_results_very_large, 'government_archive_very_large_exact.csv')

    if partial_results_very_large:
        save_results_to_csv(partial_results_very_large, 'government_archive_very_large_partial.csv')


if __name__ == "__main__":
    main()
