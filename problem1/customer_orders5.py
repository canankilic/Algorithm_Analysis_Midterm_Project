#Canan Kılıç 220201037
import pandas as pd  # to read .csv files
import time  # to measure the time taken

def read_csv_files(dataset):
    return pd.read_csv(dataset)

def bubble_sort_algorithm(array):
    array_length = len(array)

    for i in range(array_length):
        for k in range(0, array_length - i - 1):
            if array[k]['Order Amount'] < array[k + 1]['Order Amount']:
                array[k], array[k + 1] = array[k + 1], array[k]  # switch bigger value to the right and smaller value to the left

    return array

def merge_sort_algorithm(array):
    if len(array) > 1:
        middle_point = len(array) // 2 # find the middle point to halve it
        left_half = array[:middle_point]
        right_half = array[middle_point:]

        left_half = merge_sort_algorithm(left_half)  # sorted left
        right_half = merge_sort_algorithm(right_half)  # sorted right

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['Order Amount'] > right_half[j]['Order Amount']: # switch bigger value to the right and smaller value to the left
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

def save_to_csv(sorted_data, filename):
    # save it as .csv
    df = pd.DataFrame(sorted_data)
    df.to_csv(filename, index=False)

def measure_time(sorted_algorithm, value):
    starting = time.time()
    sorted_values = sorted_algorithm(value)
    ending = time.time()
    return sorted_values, ending - starting

def main():
    # read datasets and convert them to dictionaries
    dataset_small = read_csv_files('customer_orders.csv').to_dict('records')
    dataset_mid = read_csv_files('customer_orders1.csv').to_dict('records')
    dataset_large = read_csv_files('customer_orders2.csv').to_dict('records')
    dataset_xlarge = read_csv_files('customer_orders3.csv').to_dict('records')

    # Process the small dataset
    print("Testing on Small Dataset:")
    sorted_small_data_bubble, bubble_time_small = measure_time(bubble_sort_algorithm, dataset_small.copy())
    sorted_small_data_merge, merge_time_small = measure_time(merge_sort_algorithm, dataset_small.copy())

    print(f"Bubble Sort: {bubble_time_small:.8f} seconds")
    print(f"Merge Sort: {merge_time_small:.8f} seconds")
    speed = "Bubble Sort is faster for small dataset" if bubble_time_small < merge_time_small else "Merge Sort is faster for small dataset"
    print(f"{speed}")

    # save sorted small dataset to .csv
    save_to_csv(sorted_small_data_bubble, 'customer_orders_sorted_bubble.csv')
    save_to_csv(sorted_small_data_merge, 'customer_orders_sorted_merge.csv')

    # repeat this steps for mid, large, and very large datasets.
    print("\nTesting on Mid Dataset:")
    sorted_mid_data_bubble, bubble_time_mid = measure_time(bubble_sort_algorithm, dataset_mid.copy())
    sorted_mid_data_merge, merge_time_mid = measure_time(merge_sort_algorithm, dataset_mid.copy())

    print(f"Bubble Sort: {bubble_time_mid:.8f} seconds")
    print(f"Merge Sort: {merge_time_mid:.8f} seconds")
    speed = "Bubble Sort is faster for mid dataset" if bubble_time_mid < merge_time_mid else "Merge Sort is faster for mid dataset"
    print(f"{speed}")

    save_to_csv(sorted_mid_data_bubble, 'customer_orders_sorted_mid_bubble.csv')
    save_to_csv(sorted_mid_data_merge, 'customer_orders_sorted_mid_merge.csv')

    print("\nTesting on Large Dataset:")
    sorted_large_data_bubble, bubble_time_large = measure_time(bubble_sort_algorithm, dataset_large.copy())
    sorted_large_data_merge, merge_time_large = measure_time(merge_sort_algorithm, dataset_large.copy())

    print(f"Bubble Sort: {bubble_time_large:.8f} seconds")
    print(f"Merge Sort: {merge_time_large:.8f} seconds")
    speed = "Bubble Sort is faster for large dataset" if bubble_time_large < merge_time_large else "Merge Sort is faster for large dataset"
    print(f"{speed}")

    save_to_csv(sorted_large_data_bubble, 'customer_orders_sorted_large_bubble.csv')
    save_to_csv(sorted_large_data_merge, 'customer_orders_sorted_large_merge.csv')

    print("\nTesting on Very Large Dataset:")
    sorted_very_large_data_bubble, bubble_time_very_large = measure_time(bubble_sort_algorithm, dataset_xlarge.copy())
    sorted_very_large_data_merge, merge_time_very_large = measure_time(merge_sort_algorithm, dataset_xlarge.copy())

    print(f"Bubble Sort: {bubble_time_very_large:.8f} seconds")
    print(f"Merge Sort: {merge_time_very_large:.8f} seconds")
    speed = "Bubble Sort is faster for very large dataset" if bubble_time_very_large < merge_time_very_large else "Merge Sort is faster for very large dataset"
    print(f"{speed}")

    save_to_csv(sorted_very_large_data_bubble, 'customer_orders_sorted_very_large_bubble.csv')
    save_to_csv(sorted_very_large_data_merge, 'customer_orders_sorted_very_large_merge.csv')

if __name__ == "__main__":
    main()
