#Canan Kılıç 220201037
import pandas as pd  # to read .csv files
import time  # to measure the time taken for the process

def read_csv_files(dataset):
    return pd.read_csv(dataset)

def bubble_sort_algorithm(array):
    array_length = len(array)
    for i in range(array_length):
        for k in range(0, array_length - i - 1):
            if (array[k]['Urgency Level'] > array[k + 1]['Urgency Level'] or
                (array[k]['Urgency Level'] == array[k + 1]['Urgency Level'] and
                 array[k]['Test Date'] > array[k + 1]['Test Date'])):  # if urgency level is the same, check test date
                array[k], array[k + 1] = array[k + 1], array[k]
    return array

def merge_sort_algorithm(array):
    if len(array) > 1:
        middle_point = len(array) // 2
        left_half = array[:middle_point]
        right_half = array[middle_point:]

        merge_sort_algorithm(left_half)  # sort them recursively
        merge_sort_algorithm(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (left_half[i]['Urgency Level'] < right_half[j]['Urgency Level'] or
                (left_half[i]['Urgency Level'] == right_half[j]['Urgency Level'] and
                 left_half[i]['Test Date'] <= right_half[j]['Test Date'])):  # if urgency level is the same, check test date
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):  # if anything left copy them to the array
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

def save_sorted_results_to_csv(sorted_data, filename):
    # save sorted data as CSV
    df = pd.DataFrame(sorted_data)
    df.to_csv(filename, index=False)

def measure_time(sorted_algorithm, value):
    starting = time.time()
    sorted_values = sorted_algorithm(value)
    ending = time.time()
    return sorted_values, ending - starting

def main():
    # read datasets and convert them to dictionaries
    dataset_small = read_csv_files('medical_tests.csv').to_dict('records')
    dataset_mid = read_csv_files('medical_tests1.csv').to_dict('records')
    dataset_large = read_csv_files('medical_tests2.csv').to_dict('records')
    dataset_xlarge = read_csv_files('medical_tests3.csv').to_dict('records')

    print("Testing on Small Dataset:")
    sorted_small_data_bubble, bubble_time_small = measure_time(bubble_sort_algorithm, dataset_small.copy())
    print(f"Bubble Sort Time: {bubble_time_small:.8f} seconds")
    save_sorted_results_to_csv(sorted_small_data_bubble, 'medical_test_res_small_bubble.csv')

    sorted_small_data_merge, merge_time_small = measure_time(merge_sort_algorithm, dataset_small.copy())
    print(f"Merge Sort Time: {merge_time_small:.8f} seconds")
    save_sorted_results_to_csv(sorted_small_data_merge, 'medical_test_res_small_merge.csv')
    speed = "Bubble Sort is faster for small dataset" if bubble_time_small < merge_time_small else "Merge Sort is faster for small dataset"
    print(f"{speed}")

    print("\nTesting on Mid Dataset:")
    sorted_mid_data_bubble, bubble_time_mid = measure_time(bubble_sort_algorithm, dataset_mid.copy())
    print(f"Bubble Sort Time: {bubble_time_mid:.8f} seconds")
    save_sorted_results_to_csv(sorted_mid_data_bubble, 'medical_test_res_mid_bubble.csv')

    sorted_mid_data_merge, merge_time_mid = measure_time(merge_sort_algorithm, dataset_mid.copy())
    print(f"Merge Sort Time: {merge_time_mid:.8f} seconds")
    save_sorted_results_to_csv(sorted_mid_data_merge, 'medical_test_res_mid_merge.csv')
    speed = "Bubble Sort is faster for mid dataset" if bubble_time_mid < merge_time_mid else "Merge Sort is faster for mid dataset"
    print(f"{speed}")

    print("\nTesting on Large Dataset:")
    sorted_large_data_bubble, bubble_time_large = measure_time(bubble_sort_algorithm, dataset_large.copy())
    print(f"Bubble Sort Time: {bubble_time_large:.8f} seconds")
    save_sorted_results_to_csv(sorted_large_data_bubble, 'medical_test_res_large_bubble.csv')

    sorted_large_data_merge, merge_time_large = measure_time(merge_sort_algorithm, dataset_large.copy())
    print(f"Merge Sort Time: {merge_time_large:.8f} seconds")
    save_sorted_results_to_csv(sorted_large_data_merge, 'medical_test_res_large_merge.csv')
    speed = "Bubble Sort is faster for large dataset" if bubble_time_large < merge_time_large else "Merge Sort is faster for large dataset"
    print(f"{speed}")

    print("\nTesting on Very Large Dataset:")
    sorted_very_large_data_bubble, bubble_time_very_large = measure_time(bubble_sort_algorithm, dataset_xlarge.copy())
    print(f"Bubble Sort Time: {bubble_time_very_large:.8f} seconds")
    save_sorted_results_to_csv(sorted_very_large_data_bubble, 'medical_test_res_very_large_bubble.csv')

    sorted_very_large_data_merge, merge_time_very_large = measure_time(merge_sort_algorithm, dataset_xlarge.copy())
    print(f"Merge Sort Time: {merge_time_very_large:.8f} seconds")
    save_sorted_results_to_csv(sorted_very_large_data_merge, 'medical_test_res_very_large_merge.csv')
    speed = "Bubble Sort is faster for very large dataset" if bubble_time_very_large < merge_time_very_large else "Merge Sort is faster for very large dataset"
    print(f"{speed}")

if __name__ == "__main__":
    main()
