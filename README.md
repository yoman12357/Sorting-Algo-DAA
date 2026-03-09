# Sorting Algorithm Performance Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/your-repo/your-project/actions) <!-- Placeholder: Replace with actual build status if using CI/CD -->

## Overview

This comprehensive analysis tool evaluates and compares the performance characteristics of multiple sorting algorithms across different data sizes and distributions. The system generates detailed performance metrics in CSV format, creates visual representations through graphs, and provides an extensive analytical report.

## Table of Contents

1.  [Project Structure](#1-project-structure)
2.  [Algorithms Benchmarked](#2-algorithms-benchmarked)
3.  [Benchmarking Methodology](#3-benchmarking-methodology)
    *   [Machine Specifications](#31-machine-specifications)
    *   [Timing Mechanism](#32-timing-mechanism)
    *   [Number of Experiment Repetitions](#33-number-of-experiment-repetitions)
    *   [Reported Times](#34-reported-times)
    *   [Input Selection](#35-input-selection)
    *   [Consistency of Inputs](#36-consistency-of-inputs)
4.  [Sorting Algorithms Details](#4-sorting-algorithms-details)
    *   [Bubble Sort](#bubble-sort)
    *   [Selection Sort](#selection-sort)
    *   [Insertion Sort](#insertion-sort)
    *   [Merge Sort](#merge-sort)
    *   [Quicksort](#quicksort)
    *   [Radix Sort](#radix-sort)
5.  [Launch and Usage](#5-launch-and-usage)
6.  [License](#6-license)
7.  [Contact Information](#7-contact-information)

## Directory Structure

The project repository is organized with the following structure:

*   `sorting_algorithms/`: Contains C source code implementations of all sorting algorithms.
*   `test_data/`: Pre-generated data files used for performance testing and evaluation.
*   `executables/`: (Created during execution) Compiled binary files from C source code.
*   `graphs/`: (Generated during runtime) Performance data in CSV format and visualization plots.
*   `benchmark.py`: Main Python script for orchestrating the benchmarking process.
*   `generate_test_data.py`: Utility script for creating test datasets.

## Algorithms Under Analysis

The performance evaluation encompasses the following sorting algorithms, selected to provide comprehensive coverage of different algorithmic paradigms:

1.  **Fundamental Comparison Sort:** Bubble Sort
2.  **Advanced Divide-and-Conquer:** Quicksort (median-of-three pivot strategy)
3.  **Linear-Time Non-Comparison:** Radix Sort
4.  **Simple Selection-Based:** Selection Sort
5.  **Incremental Building:** Insertion Sort
6.  **Heap-Based:** Heap Sort
7.  **Stable Divide-and-Conquer:** Merge Sort

## Experimental Methodology

The testing framework is designed to ensure reproducible and comparable performance measurements across all evaluated sorting algorithms.

### System Configuration

*   **Operating System:** Windows
*   **Device Model:** ASUS Vivobook 16X
*   **CPU:** Intel Core i7 Processor
*   **Graphics:** NVIDIA RTX 4050 Studio
*   **Device ID:** R6N0CX02K537230

### Timing Measurement Approach

Execution timing is captured using **Python's `time.perf_counter()`** function, which provides high-precision temporal measurements suitable for performance analysis. The C sorting programs are executed as subprocesses, with their complete execution duration (including input processing, sorting operations, and internal overhead) measured by the orchestrating Python script.

### Experimental Repetition Strategy

Each individual test case (specific algorithm operating on particular input size and data distribution) is executed **7 times**. This multiple repetition approach mitigates the impact of system variability, background processes, and other environmental factors that could introduce measurement noise in single-run scenarios.

### Performance Metrics Reporting

For each experimental configuration, the **mean execution time** across all 7 repetitions is reported. All timing measurements are presented in **seconds (s)** with precision to six decimal places. In scenarios where algorithm execution fails (e.g., stack overflow in certain Quick Sort implementations with pathological inputs), the result is marked as "Crashed/Timeout".

### Test Dataset Generation

The evaluation data is systematically generated using the `generate_test_data.py` utility. The test inputs are designed to span various sizes and initial ordering patterns to assess algorithmic behavior across best-case, worst-case, and average-case scenarios:

*   **Dataset Sizes (N):** The evaluation includes the following input magnitudes: 100, 500, 1,000, 5,000, 10,000, 25,000, 50,000, 75,000, and 100,000 elements.
*   **Data Distribution Types:** For each input size, three distinct data arrangements are generated:
    *   **Random Distribution:** Unordered integer arrays representing **average-case** performance scenarios.
    *   **Ascending Order:** Pre-sorted integer arrays for evaluating **best-case** performance (advantageous for algorithms like Insertion Sort and Merge Sort) and **worst-case** scenarios for others (such as Quick Sort with suboptimal pivot selection).
    *   **Descending Order:** Reverse-sorted arrays typically representing **worst-case** conditions for most comparison-based sorting approaches.

### Dataset Consistency Protocol

All sorting algorithms are evaluated using identical input datasets to ensure fair and direct performance comparisons under uniform conditions. Each C sorting implementation is configured to read input from standard input (stdin), enabling the Python benchmarking framework to provide consistent data streams to all algorithms.

## Algorithmic Analysis

### Bubble Sort Algorithm

Bubble Sort represents one of the most fundamental comparison-based sorting approaches. The algorithm operates by iteratively traversing the list, comparing neighboring elements, and performing swaps when elements are out of order. This traversal process continues until a complete pass occurs without any swaps, indicating successful sorting.

#### Algorithm Characteristics

**Data Structure:** Array-based implementation

| Performance Metric         | Computational Complexity                     |
| :------------------------- | :------------------------------------------ |
| Worst-Case Time Complexity | O(n²) comparisons, O(n²) swaps               |
| Best-Case Time Complexity  | O(n) comparisons, O(1) swaps (sorted input) |
| Average-Case Complexity    | O(n²) comparisons, O(n²) swaps               |
| Space Complexity           | O(1) auxiliary memory                        |

### Selection Sort Algorithm

Selection Sort operates by partitioning the input array into two distinct regions: a progressively growing sorted subarray at the beginning and a remaining unsorted region. Initially, the sorted region is empty while the unsorted region encompasses the entire array. The algorithm systematically identifies the minimum element from the unsorted region and exchanges it with the first unsorted element, effectively expanding the sorted boundary by one position.

![selection sort Gif](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

#### Algorithm Characteristics

**Data Structure:** Array-based implementation

| Performance Metric         | Computational Complexity                    |
| :------------------------- | :----------------------------------------- |
| Worst-Case Time Complexity | O(n²) comparisons, O(n) swaps              |
| Best-Case Time Complexity  | O(n²) comparisons, O(n) swaps               |
| Average-Case Complexity    | O(n²) comparisons, O(n) swaps              |
| Space Complexity           | O(1) auxiliary memory                       |

### Insertion Sort Algorithm

Insertion Sort constructs the final sorted array incrementally by inserting elements one at a time. While this approach exhibits inferior performance characteristics on large datasets compared to advanced algorithms like Quicksort or Merge Sort, it offers several practical advantages including implementation simplicity, efficiency with small datasets, and optimal performance for nearly sorted input data.

#### Algorithm Characteristics

**Data Structure:** Array-based implementation

| Performance Metric         | Computational Complexity                      |
| :------------------------- | :------------------------------------------- |
| Worst-Case Time Complexity | O(n²) comparisons, O(n²) element shifts      |
| Best-Case Time Complexity  | O(n) comparisons, O(1) shifts (sorted input) |
| Average-Case Complexity    | O(n²) comparisons, O(n²) shifts              |
| Space Complexity           | O(1) auxiliary memory                         |

### Merge Sort Algorithm

Merge Sort represents an efficient, comparison-based, divide-and-conquer sorting paradigm. The algorithm operates by recursively partitioning an unsorted list into n sublists, each containing a single element (considered inherently sorted). These sublists are then systematically merged to produce progressively larger sorted sublists until only one completely sorted list remains.

#### Algorithm Characteristics

**Data Structure:** Array-based implementation (adaptable to linked lists)

| Performance Metric         | Computational Complexity |
| :------------------------- | :---------------------- |
| Worst-Case Time Complexity | O(n log n)              |
| Best-Case Time Complexity  | O(n log n)              |
| Average-Case Complexity    | O(n log n)              |
| Space Complexity           | O(n) auxiliary (array) |

### Quicksort Algorithm

Quicksort implements a divide-and-conquer strategy by selecting a 'pivot' element from the array and partitioning the remaining elements into two subarrays based on their comparison to the pivot. These subarrays are then recursively sorted. This specific implementation employs a **median-of-three pivot selection strategy**. The algorithm can be performed in-place, requiring minimal additional memory beyond the recursion stack.

![quicksort sort Gif](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

#### Algorithm Characteristics

**Data Structure:** Array-based implementation

| Performance Metric         | Computational Complexity                                     |
| :------------------------- | :----------------------------------------------------------- |
| Worst-Case Time Complexity | O(n²) (degenerate cases with poor pivot selection)            |
| Best-Case Time Complexity  | O(n log n)                                                   |
| Average-Case Complexity    | O(n log n)                                                   |
| Space Complexity           | O(log n) auxiliary (recursion stack)                         |

### Radix Sort Algorithm

Radix Sort represents a non-comparative sorting approach that eliminates the need for element-to-element comparisons. Instead, the algorithm distributes elements into buckets based on their digit values (radix). For multi-digit numbers, this bucketing process is repeated for each digit position while maintaining the ordering established in previous passes. This methodology results in a time complexity of O(nk), where n represents the number of elements and k denotes the number of digit positions required.

#### Algorithm Characteristics

**Data Structure:** Array-based implementation

| Performance Metric         | Computational Complexity                           |
| :------------------------- | :------------------------------------------------ |
| Worst-Case Time Complexity | O(nk)                                              |
| Best-Case Time Complexity  | O(nk)                                              |
| Average-Case Complexity    | O(nk)                                              |
| Space Complexity           | O(n + k) auxiliary (bucket-dependent implementation) |

## Execution Guide

### Prerequisites

*   **Python 3.x** (version 3.9 or newer recommended)
*   **`matplotlib`** visualization library (`pip install matplotlib`)
*   **`pandas`** data analysis library (`pip install pandas`)
*   **`scipy`** scientific computing library (`pip install scipy`)
*   **GCC Compiler** (or compatible C compiler) for building sorting algorithm executables

### Running the Performance Analysis

1.  **Repository Setup:**
    ```bash
    git clone https://github.com/your-repo/Sorting-algorithms-benchmark.git # Replace with actual repository URL
    cd Sorting-algorithms-benchmark
    ```
2.  **Dependency Installation:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Test Dataset Generation (if needed):**
    ```bash
    python generate_test_data.py
    ```
    This process creates the `test_data/` directory and populates it with evaluation datasets.
4.  **Execute Performance Analysis:**
    ```bash
    python benchmark.py
    ```
    The analysis script will:
    *   Compile all C sorting algorithm implementations into executables in the `executables/` directory.
    *   Execute comprehensive performance testing against all generated datasets with multiple repetitions.
    *   Display real-time progress and results to the console.
    *   Generate performance visualization plots in the `graphs/` directory.
    *   Create detailed results tables (CSV format) in the `graphs/csv_data/` directory.

## Licensing Information

This project is distributed under the MIT License - please refer to the [LICENSE](LICENSE) file for complete licensing terms.

## Contact Details

For project-related inquiries and correspondence, please contact: aryan.bokolia@example.com
#   S o r t i n g - A l g o - D A A  
 