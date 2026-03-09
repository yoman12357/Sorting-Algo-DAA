/*
 * Bubble Sort Implementation
 * This sorting algorithm repeatedly steps through the list,
 * compares adjacent elements and swaps them if they are in the wrong order.
 * The pass through the list is repeated until no swaps are needed.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

// Global variables for performance tracking
static long long element_comparisons = 0;
static struct timespec timing_start, timing_end;

// Function to calculate elapsed time in seconds
double calculate_execution_duration(struct timespec begin, struct timespec finish) {
    return (finish.tv_sec - begin.tv_sec) + (finish.tv_nsec - begin.tv_nsec) / 1e9;
}

// Optimized bubble sort with early termination
void bubble_sort_algorithm(int array[], int array_size) {
    int outer_index, inner_index, temporary_value;
    int swap_occurred;
    
    // Main sorting loop
    for (outer_index = 0; outer_index < array_size - 1; outer_index++) {
        swap_occurred = 0;
        
        // Compare adjacent elements
        for (inner_index = 0; inner_index < array_size - outer_index - 1; inner_index++) {
            element_comparisons++;
            
            // Swap if elements are in wrong order
            if (array[inner_index] > array[inner_index + 1]) {
                temporary_value = array[inner_index];
                array[inner_index] = array[inner_index + 1];
                array[inner_index + 1] = temporary_value;
                swap_occurred = 1;
            }
        }
        
        // Early exit if no swaps occurred
        if (swap_occurred == 0) {
            break;
        }
    }
}

// Utility function to display array contents (for debugging)
void display_array(int array[], int size) {
    int index;
    for (index = 0; index < size; index++) {
        printf("%d ", array[index]);
    }
    printf("\n");
}

// Main execution function
int main(void) {
    int number_of_elements;
    
    // Read array size from input
    scanf("%d", &number_of_elements);
    
    // Allocate memory for the array
    int *input_array = (int *)malloc(number_of_elements * sizeof(int));
    if (input_array == NULL) {
        return 1; // Memory allocation failed
    }

    // Read array elements from input
    for (int element_index = 0; element_index < number_of_elements; element_index++) {
        scanf("%d", &input_array[element_index]);
    }
    
    // Perform timing measurement
    clock_gettime(CLOCK_MONOTONIC, &timing_start);
    bubble_sort_algorithm(input_array, number_of_elements);
    clock_gettime(CLOCK_MONOTONIC, &timing_end);
    
    // Calculate execution duration
    double execution_time = calculate_execution_duration(timing_start, timing_end);
    
    // Output performance metrics to stderr for benchmarking
    fprintf(stderr, "TIME: %.9f\n", execution_time);
    fprintf(stderr, "COMPARISONS: %lld\n", element_comparisons);
    
    // Array output disabled for performance benchmarking
    // display_array(input_array, number_of_elements);
    
    // Clean up allocated memory
    free(input_array);
    return 0;
}
