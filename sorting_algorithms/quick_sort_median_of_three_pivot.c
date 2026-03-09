/*
 * Quick Sort Implementation with Median-of-Three Pivot Selection
 * This implementation uses the median-of-three strategy to select a good pivot,
 * which helps avoid worst-case performance on already sorted or reverse-sorted data.
 * The median of the first, middle, and last elements is chosen as the pivot.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

// Performance tracking variables
static long long total_comparisons = 0;
static struct timespec performance_start, performance_end;

// Calculate elapsed time between two timestamps
double compute_time_elapsed(struct timespec start_timestamp, struct timespec end_timestamp) {
    return (end_timestamp.tv_sec - start_timestamp.tv_sec) + 
           (end_timestamp.tv_nsec - start_timestamp.tv_nsec) / 1e9;
}

// Exchange values between two integer pointers
inline void exchange_values(int* first_pointer, int* second_pointer) {
    int temporary_storage = *first_pointer;
    *first_pointer = *second_pointer;
    *second_pointer = temporary_storage;
}

// Determine the median element among three positions in the array
int find_median_of_three(int data_array[], int left_bound, int right_bound) {
    int middle_position = left_bound + (right_bound - left_bound) / 2;
    
    // Order the three elements to identify the median
    total_comparisons++;
    if (data_array[left_bound] > data_array[middle_position]) 
        exchange_values(&data_array[left_bound], &data_array[middle_position]);
    
    total_comparisons++;
    if (data_array[left_bound] > data_array[right_bound]) 
        exchange_values(&data_array[left_bound], &data_array[right_bound]);
    
    total_comparisons++;
    if (data_array[middle_position] > data_array[right_bound]) 
        exchange_values(&data_array[middle_position], &data_array[right_bound]);
    
    // The middle element now contains the median value
    return middle_position;
}

// Partition the array around the pivot element
int array_partition(int data_array[], int left_index, int right_index) {
    int pivot_value = data_array[right_index];
    int partition_boundary = (left_index - 1);
    int current_index;
    
    // Rearrange elements based on comparison with pivot
    for (current_index = left_index; current_index <= right_index - 1; current_index++) {
        total_comparisons++;
        if (data_array[current_index] < pivot_value) {
            partition_boundary++;
            exchange_values(&data_array[partition_boundary], &data_array[current_index]);
        }
    }
    
    // Position pivot in its final location
    exchange_values(&data_array[partition_boundary + 1], &data_array[right_index]);
    return (partition_boundary + 1);
}

// Recursive quicksort implementation with median-of-three pivot selection
void quicksort_median_three(int data_array[], int left_bound, int right_bound) {
    if (left_bound < right_bound) {
        // Select optimal pivot using median-of-three strategy
        int pivot_position = find_median_of_three(data_array, left_bound, right_bound);
        
        // Move selected pivot to end for partitioning
        exchange_values(&data_array[pivot_position], &data_array[right_bound]);
        
        // Partition array around the pivot
        int partition_index = array_partition(data_array, left_bound, right_bound);
        
        // Recursively sort subarrays
        quicksort_median_three(data_array, left_bound, partition_index - 1);
        quicksort_median_three(data_array, partition_index + 1, right_bound);
    }
}

// Display array contents (primarily for debugging purposes)
void output_array_contents(int data_array[], int array_length) {
    int position_index;
    for (position_index = 0; position_index < array_length; position_index++) {
        printf("%d ", data_array[position_index]);
    }
    printf("\n");
}

// Main program entry point
int main(void) {
    int elements_count;
    
    // Input: number of elements to sort
    scanf("%d", &elements_count);
    
    // Allocate memory for input data
    int *sorting_array = (int *)malloc(elements_count * sizeof(int));
    if (sorting_array == NULL) {
        return 1; // Memory allocation failure
    }

    // Input: array elements
    for (int element_index = 0; element_index < elements_count; element_index++) {
        scanf("%d", &sorting_array[element_index]);
    }
    
    // Execute sorting algorithm with performance measurement
    clock_gettime(CLOCK_MONOTONIC, &performance_start);
    quicksort_median_three(sorting_array, 0, elements_count - 1);
    clock_gettime(CLOCK_MONOTONIC, &performance_end);
    
    // Calculate and report performance metrics
    double sorting_duration = compute_time_elapsed(performance_start, performance_end);
    
    // Output results to stderr for benchmarking framework
    fprintf(stderr, "TIME: %.9f\n", sorting_duration);
    fprintf(stderr, "COMPARISONS: %lld\n", total_comparisons);
    
    // Sorted array output suppressed for benchmarking efficiency
    // output_array_contents(sorting_array, elements_count);
    
    // Release allocated memory
    free(sorting_array);
    return 0;
}