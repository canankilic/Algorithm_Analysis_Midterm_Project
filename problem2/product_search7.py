#Canan Kılıç 220201037
import pandas as pd  # to read .csv files
import time  # to measure the time taken for the process


def read_csv_files(dataset):
    return pd.read_csv(dataset)


def linear_search_algorithm(array, target):  # for partial match search
    results = []
    for element in array:
        if target in element['Product Name']:
            results.append(element)  # collect all matching elements
    return results if results else -1  # return matches or -1 if no match


def binary_search_algorithm(array, target):  # doing binary search to find exact matches
    left = 0
    right = len(array) - 1
    results = []
    while left <= right:
        middle_point = (left + right) // 2  # halved the array
        if array[middle_point]['Product Name'] == target:
            results.append(array[middle_point])  # add exact match
            break  # if found exact match, exit the loop
        elif array[middle_point]['Product Name'] < target:
            left = middle_point + 1
        else:
            right = middle_point - 1
    return results if results else None


def save_results_to_csv(results, filename):
    # save found elements as .csv
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)


def measure_time(search_alg, data, target):
    starting = time.time()
    results = search_alg(data, target)
    ending = time.time()
    return results, ending - starting


def main():
    dataset_small = read_csv_files('product_catalog.csv').to_dict('records')
    dataset_mid = read_csv_files('product_catalog1.csv').to_dict('records')
    dataset_large = read_csv_files('product_catalog2.csv').to_dict('records')
    dataset_xlarge = read_csv_files('product_catalog3.csv').to_dict('records')

    # sort datasets if not sorted
    small_data_sorted = sorted(dataset_small, key=lambda x: x['Product Name'])
    mid_data_sorted = sorted(dataset_mid, key=lambda x: x['Product Name'])
    large_data_sorted = sorted(dataset_large, key=lambda x: x['Product Name'])
    very_large_data_sorted = sorted(dataset_xlarge, key=lambda x: x['Product Name'])

    search_term = "Product 10" # to find different product, change the search term

    print("Testing Exact Match on Small Dataset:")
    exact_results_small, exact_time_small = measure_time(binary_search_algorithm, small_data_sorted.copy(), search_term)
    print(f"Binary Search Time (Exact Match): {exact_time_small:.8f} seconds")

    print("Testing Partial Match on Small Dataset:")
    partial_results_small, partial_time_small = measure_time(linear_search_algorithm, small_data_sorted.copy(),
                                                             search_term)
    print(f"Linear Search Time (Partial Match): {partial_time_small:.8f} seconds")

    # save found results to .csv
    if exact_results_small:
        save_results_to_csv(exact_results_small, 'product_search_small_exact.csv')

    if partial_results_small:
        save_results_to_csv(partial_results_small, 'product_search_small_partial.csv')

    # repeat the same for mid, large, and very large datasets.
    print("\nTesting Exact Match on Mid Dataset:")
    exact_results_mid, exact_time_mid = measure_time(binary_search_algorithm, mid_data_sorted.copy(), search_term)
    print(f"Binary Search Time (Exact Match): {exact_time_mid:.8f} seconds")

    print("Testing Partial Match on Mid Dataset:")
    partial_results_mid, partial_time_mid = measure_time(linear_search_algorithm, mid_data_sorted.copy(), search_term)
    print(f"Linear Search Time (Partial Match): {partial_time_mid:.8f} seconds")

    if exact_results_mid:
        save_results_to_csv(exact_results_mid, 'product_search_mid_exact.csv')

    if partial_results_mid:
        save_results_to_csv(partial_results_mid, 'product_search_mid_partial.csv')

    print("\nTesting Exact Match on Large Dataset:")
    exact_results_large, exact_time_large = measure_time(binary_search_algorithm, large_data_sorted.copy(), search_term)
    print(f"Binary Search Time (Exact Match): {exact_time_large:.8f} seconds")

    print("Testing Partial Match on Large Dataset:")
    partial_results_large, partial_time_large = measure_time(linear_search_algorithm, large_data_sorted.copy(),
                                                             search_term)
    print(f"Linear Search Time (Partial Match): {partial_time_large:.8f} seconds")

    if exact_results_large:
        save_results_to_csv(exact_results_large, 'product_search_large_exact.csv')

    if partial_results_large:
        save_results_to_csv(partial_results_large, 'product_search_large_partial.csv')

    print("\nTesting Exact Match on Very Large Dataset:")
    exact_results_very_large, exact_time_very_large = measure_time(binary_search_algorithm,
                                                                   very_large_data_sorted.copy(), search_term)
    print(f"Binary Search Time (Exact Match): {exact_time_very_large:.8f} seconds")

    print("Testing Partial Match on Very Large Dataset:")
    partial_results_very_large, partial_time_very_large = measure_time(linear_search_algorithm,
                                                                       very_large_data_sorted.copy(), search_term)
    print(f"Linear Search Time (Partial Match): {partial_time_very_large:.8f} seconds")

    if exact_results_very_large:
        save_results_to_csv(exact_results_very_large, 'product_search_very_large_exact.csv')

    if partial_results_very_large:
        save_results_to_csv(partial_results_very_large, 'product_search_very_large_partial.csv')


if __name__ == "__main__":
    main()
