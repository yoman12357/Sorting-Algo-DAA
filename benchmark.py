import os
import subprocess
import time
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# --- Configuration Parameters ---
ALGORITHM_FILES = [
    "bubble_sort.c",
    "heap_sort.c",
    "insertion_sort.c",
    "merge_sort.c",
    "quick_sort_median_of_three_pivot.c",
    "radix_sort.c",
    "selection_sort.c",
]

# Quick Sort implementation variants for comparative analysis
QUICKSORT_IMPLEMENTATIONS = [
    "quick_sort_first_pivot.c",
    "quick_sort_median_of_three_pivot.c",
    "quick_sort_random_pivot.c",
]

ALGORITHM_FILE_PATHS = [os.path.join("sorting_algorithms", f) for f in ALGORITHM_FILES]
QUICKSORT_FILE_PATHS = [os.path.join("sorting_algorithms", f) for f in QUICKSORT_IMPLEMENTATIONS]
BINARY_OUTPUT_DIR = "executables"
DATASET_DIRECTORY = "test_data"
VISUALIZATION_OUTPUT_DIR = "graphs"
COMPARISON_CHARTS_DIR = os.path.join(VISUALIZATION_OUTPUT_DIR, "7_sorting_algo_comparisons")
QUICKSORT_ANALYSIS_DIR = os.path.join(VISUALIZATION_OUTPUT_DIR, "quick_sort_analysis")
CSV_EXPORT_DIR = os.path.join(VISUALIZATION_OUTPUT_DIR, "csv_data")
EXPERIMENT_REPETITIONS = 7
# Maximum dataset size for visualization plots
VISUALIZATION_MAX_SIZE = 100000 

# --- Utility Functions ---

def build_executable(source_file_path, binary_output_path):
    """Compiles C source code into executable binary."""
    print(f"Building executable from {source_file_path}...")
    try:
        # Use different compilation flags for Windows compatibility
        gcc_cmd = ["gcc", source_file_path, "-o", binary_output_path, 
                   "-Wl,--stack=268435456", "-std=c99", "-DNULL=0",
                   "-U__STRICT_ANSI__", "-D_CRT_SECURE_NO_WARNINGS"]
        subprocess.run(gcc_cmd, check=True, capture_output=True, text=True)
        print(f"Successfully compiled {source_file_path} -> {binary_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed for {source_file_path}:")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        exit(1)

def load_dataset(file_path):
    """Loads integer dataset from specified file, one integer per line."""
    with open(file_path, 'r') as f:
        dataset = [int(line.strip()) for line in f if line.strip()]
    return dataset

def execute_performance_test(executable_path, test_dataset):
    """
    Executes compiled sorting program with provided dataset and captures performance metrics.
    Input is delivered via stdin. Returns tuple of (execution_time, comparison_count).
    Timing measurements are performed within C code using clock_gettime().
    """
    input_data = f"{len(test_dataset)}\n" + " ".join(map(str, test_dataset))
    
    try:
        process_result = subprocess.run(
            [executable_path],
            input=input_data,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse performance metrics from stderr output
        execution_time = float('inf')
        comparison_operations = 0
        stderr_output = process_result.stderr.strip().split('\n')
        for output_line in stderr_output:
            if output_line.startswith("TIME:"):
                execution_time = float(output_line.split(":")[1].strip())
            elif output_line.startswith("COMPARISONS:"):
                comparison_operations = int(output_line.split(":")[1].strip())
        
        return execution_time, comparison_operations
    except subprocess.CalledProcessError as e:
        print(f"Execution failed for {executable_path} with dataset size {len(test_dataset)}:")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return float('inf'), 0

def parse_dataset_metadata(filename):
    """Extracts dataset size and type information from filename pattern."""
    pattern_match = re.match(r"n_(\d+)_(\w+)\.txt", filename)
    if pattern_match:
        return int(pattern_match.group(1)), pattern_match.group(2)
    return None, None

def create_performance_visualizations(results_data, case_description, output_directory, measurement_type="time"):
    """Generates and saves performance visualization plots for specific test cases."""
    # Linear scale visualization
    plt.figure(figsize=(12, 7))
    
    for algorithm_name, performance_points in results_data.items():
        # Sort data points for proper plotting
        performance_points.sort(key=lambda x: x[0])
        dataset_sizes = [dp[0] for dp in performance_points if dp[0] <= VISUALIZATION_MAX_SIZE]
        performance_values = [dp[1] for dp in performance_points if dp[0] <= VISUALIZATION_MAX_SIZE]
        plt.plot(dataset_sizes, performance_values, marker='o', linestyle='-', 
                label=algorithm_name, linewidth=2, markersize=6)

    plt.xlabel("Dataset Size (n)", fontsize=11)
    if measurement_type == "time":
        plt.ylabel("Mean Execution Time (s)", fontsize=11)
        plt.title(f"Algorithm Performance Analysis (Time): {case_description}", fontsize=12, fontweight='bold')
    else:
        plt.ylabel("Comparison Operations Count", fontsize=11)
        plt.title(f"Algorithm Performance Analysis (Comparisons): {case_description}", fontsize=12, fontweight='bold')
    
    plt.legend(fontsize=10, loc='best')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.tight_layout()
    
    metric_suffix = "_time" if measurement_type == "time" else "_comparisons"
    output_filepath = os.path.join(output_directory, f"algorithm_performance_{case_description.lower().replace(' ', '_')}{metric_suffix}.png")
    plt.savefig(output_filepath, dpi=150)
    print(f"Generated visualization: {output_filepath}")
    plt.close()
    
    # Logarithmic Scale Plot (Y-axis) - For better visibility
    plt.figure(figsize=(12, 7))
    
    for algorithm_name, performance_points in results_data.items():
        # Sort data points for proper plotting
        performance_points.sort(key=lambda x: x[0])
        dataset_sizes = [dp[0] for dp in performance_points if dp[0] <= VISUALIZATION_MAX_SIZE]
        performance_values = [dp[1] for dp in performance_points if dp[0] <= VISUALIZATION_MAX_SIZE]
        # Filter out zero or negative values for log scale
        filtered_sizes = [n for n, v in zip(dataset_sizes, performance_values) if v > 0]
        filtered_values = [v for v in performance_values if v > 0]
        if filtered_values:
            plt.plot(filtered_sizes, filtered_values, marker='o', linestyle='-', 
                    label=algorithm_name, linewidth=2, markersize=6)

    plt.xlabel("Dataset Size (n)", fontsize=11)
    if measurement_type == "time":
        plt.ylabel("Mean Execution Time (s) - Log Scale", fontsize=11)
        plt.title(f"Algorithm Performance Analysis (Time) - Log Scale: {case_description}", fontsize=12, fontweight='bold')
    else:
        plt.ylabel("Comparison Operations Count - Log Scale", fontsize=11)
        plt.title(f"Algorithm Performance Analysis (Comparisons) - Log Scale: {case_description}", fontsize=12, fontweight='bold')
    
    plt.legend(fontsize=10, loc='best')
    plt.grid(True, alpha=0.3, which='both')
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    
    # Save with _log_scale suffix
    log_output_filepath = os.path.join(output_directory, f"algorithm_performance_{case_description.lower().replace(' ', '_')}{metric_suffix}_log_scale.png")
    plt.savefig(log_output_filepath, dpi=150)
    print(f"Generated logarithmic visualization: {log_output_filepath}")
    plt.close()

def generate_correlation_analysis(performance_data, output_directory):
    """Creates correlation analysis plots between execution time and comparison operations."""
    plt.figure(figsize=(14, 10))
    
    algorithm_count = len(performance_data)
    subplot_rows = (algorithm_count + 1) // 2
    subplot_cols = 2
    
    for subplot_index, (algorithm_name, data_points) in enumerate(performance_data.items(), 1):
        plt.subplot(subplot_rows, subplot_cols, subplot_index)
        
        # Extract timing and comparison metrics
        execution_times = [dp[1] for dp in data_points if dp[1] != float('inf')]
        comparison_counts = [dp[2] for dp in data_points if dp[1] != float('inf')]
        
        if len(execution_times) > 1 and len(comparison_counts) > 1:
            # Calculate statistical correlation
            correlation_coeff, p_value = pearsonr(comparison_counts, execution_times)
            
            # Create scatter plot with regression line
            plt.scatter(comparison_counts, execution_times, alpha=0.6, s=100, 
                       color='steelblue', edgecolors='black', linewidth=0.5)
            
            # Add linear regression trend line
            regression_params = np.polyfit(comparison_counts, execution_times, 1)
            regression_function = np.poly1d(regression_params)
            x_range = np.linspace(min(comparison_counts), max(comparison_counts), 100)
            plt.plot(x_range, regression_function(x_range), "r--", alpha=0.8, 
                    linewidth=2, label='Regression Line')
            
            plt.xlabel("Comparison Operations Count", fontsize=10)
            plt.ylabel("Execution Time (s)", fontsize=10)
            subplot_title = f"{algorithm_name}\nCorrelation: {correlation_coeff:.4f} (p={p_value:.4e})"
            plt.title(subplot_title, fontsize=10, fontweight='bold')
            plt.grid(True, alpha=0.3)
            plt.legend(fontsize=9, loc='best')
    
    plt.tight_layout()
    correlation_output_path = os.path.join(output_directory, "time_vs_comparisons_correlation.png")
    plt.savefig(correlation_output_path, dpi=150)
    print(f"Generated correlation analysis: {correlation_output_path}")
    plt.close()

# --- Main Execution ---
if __name__ == "__main__":
    # Create necessary directories
    os.makedirs(BINARY_OUTPUT_DIR, exist_ok=True)
    os.makedirs(VISUALIZATION_OUTPUT_DIR, exist_ok=True)
    os.makedirs(COMPARISON_CHARTS_DIR, exist_ok=True)
    os.makedirs(QUICKSORT_ANALYSIS_DIR, exist_ok=True)
    os.makedirs(CSV_EXPORT_DIR, exist_ok=True)

    algorithm_executables = {}
    for source_file in ALGORITHM_FILES:
        algorithm_name = os.path.splitext(source_file)[0]
        executable_path = os.path.join(BINARY_OUTPUT_DIR, algorithm_name)
        build_executable(os.path.join("sorting_algorithms", source_file), executable_path)
        algorithm_executables[algorithm_name] = executable_path
    
    # Build quick sort variant executables
    quicksort_executables = {}
    for quicksort_file in QUICKSORT_IMPLEMENTATIONS:
        algorithm_name = os.path.splitext(quicksort_file)[0]
        executable_path = os.path.join(BINARY_OUTPUT_DIR, algorithm_name)
        build_executable(os.path.join("sorting_algorithms", quicksort_file), executable_path)
        quicksort_executables[algorithm_name] = executable_path

    # Performance data structure: {algorithm: {data_type: [(size, time, comparisons), ...]}}
    algorithm_performance_data = {
        "bubble_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "heap_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "insertion_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "merge_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "quick_sort_median_of_three_pivot": {"random": [], "sorted": [], "reverse_sorted": []},
        "radix_sort": {"random": [], "sorted": [], "reverse_sorted": []},
        "selection_sort": {"random": [], "sorted": [], "reverse_sorted": []},
    }
    
    # Quick sort variant performance data
    quicksort_performance_data = {
        "quick_sort_first_pivot": {"random": [], "sorted": [], "reverse_sorted": []},
        "quick_sort_median_of_three_pivot": {"random": [], "sorted": [], "reverse_sorted": []},
        "quick_sort_random_pivot": {"random": [], "sorted": [], "reverse_sorted": []},
    }

    # Retrieve all dataset files
    dataset_files = [f for f in os.listdir(DATASET_DIRECTORY) if f.endswith(".txt")]
    dataset_files.sort(key=lambda x: (parse_dataset_metadata(x)[0], parse_dataset_metadata(x)[1]))

    print("\nInitiating performance evaluation...")
    for dataset_file in dataset_files:
        dataset_size, data_category = parse_dataset_metadata(dataset_file)
        if dataset_size is None:
            continue
        
        dataset_path = os.path.join(DATASET_DIRECTORY, dataset_file)
        source_data = load_dataset(dataset_path)
        
        print(f"Evaluating dataset size={dataset_size}, category={data_category}...")

        for algorithm_identifier, executable_path in algorithm_executables.items():
            cumulative_time = 0
            cumulative_comparisons = 0
            for iteration in range(EXPERIMENT_REPETITIONS):
                # Provide data copy to prevent modification by C program
                execution_time, comparison_count = execute_performance_test(executable_path, list(source_data))
                cumulative_time += execution_time
                cumulative_comparisons += comparison_count
            
            mean_time = cumulative_time / EXPERIMENT_REPETITIONS
            mean_comparisons = cumulative_comparisons / EXPERIMENT_REPETITIONS
            print(f"  {algorithm_identifier}: Time = {mean_time:.6f} s, Comparisons = {mean_comparisons:.0f}")
            
            # Store performance data as (size, time, comparisons)
            algorithm_performance_data[algorithm_identifier][data_category].append((dataset_size, mean_time, mean_comparisons))
        
        # Evaluate quick sort variants separately
        for quicksort_variant, quicksort_executable_path in quicksort_executables.items():
            cumulative_time = 0
            cumulative_comparisons = 0
            for iteration in range(EXPERIMENT_REPETITIONS):
                execution_time, comparison_count = execute_performance_test(quicksort_executable_path, list(source_data))
                cumulative_time += execution_time
                cumulative_comparisons += comparison_count
            
            mean_time = cumulative_time / EXPERIMENT_REPETITIONS
            mean_comparisons = cumulative_comparisons / EXPERIMENT_REPETITIONS
            print(f"  {quicksort_variant}: Time = {mean_time:.6f} s, Comparisons = {mean_comparisons:.0f}")
            
            quicksort_performance_data[quicksort_variant][data_category].append((dataset_size, mean_time, mean_comparisons))

    print("\nPerformance evaluation completed. Generating visualizations...")

    # --- Visualization Generation ---
    # Prepare time-based visualization data
    average_case_time = {}
    worst_case_time = {}
    best_case_time = {}
    
    # Prepare comparison-based visualization data
    average_case_comparisons = {}
    worst_case_comparisons = {}
    best_case_comparisons = {}
    
    # Prepare data for correlation analysis
    correlation_analysis_data = {}
    
    for algorithm_key, data_categories in algorithm_performance_data.items():
        # Format algorithm name for display
        display_name = algorithm_key.replace('_', ' ').title()
        if "Quick Sort Median Of Three Pivot" in display_name:
            display_name = "Quick Sort (Median of Three)"
        
        # Time-based plots - extract (size, time)
        average_case_time[display_name] = [(size, time_val) for size, time_val, comp_count in data_categories["random"]]
        worst_case_time[display_name] = [(size, time_val) for size, time_val, comp_count in data_categories["reverse_sorted"]]
        best_case_time[display_name] = [(size, time_val) for size, time_val, comp_count in data_categories["sorted"]]
        
        # Comparison-based plots - extract (size, comparisons)
        average_case_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in data_categories["random"]]
        worst_case_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in data_categories["reverse_sorted"]]
        best_case_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in data_categories["sorted"]]
        
        # Correlation data - combine all categories, extract (size, time, comparisons)
        all_categories_combined = data_categories["random"] + data_categories["sorted"] + data_categories["reverse_sorted"]
        correlation_analysis_data[display_name] = all_categories_combined
    
    # Generate Time vs Size plots in comparison charts directory
    create_performance_visualizations(average_case_time, "Average Case (Random Input)", COMPARISON_CHARTS_DIR, measurement_type="time")
    create_performance_visualizations(worst_case_time, "Worst Case (Reverse Sorted Input)", COMPARISON_CHARTS_DIR, measurement_type="time")
    create_performance_visualizations(best_case_time, "Best Case (Sorted Input)", COMPARISON_CHARTS_DIR, measurement_type="time")
    
    # Generate Comparisons vs Size plots in comparison charts directory
    create_performance_visualizations(average_case_comparisons, "Average Case (Random Input)", COMPARISON_CHARTS_DIR, measurement_type="comparisons")
    create_performance_visualizations(worst_case_comparisons, "Worst Case (Reverse Sorted Input)", COMPARISON_CHARTS_DIR, measurement_type="comparisons")
    create_performance_visualizations(best_case_comparisons, "Best Case (Sorted Input)", COMPARISON_CHARTS_DIR, measurement_type="comparisons")
    
    # Generate correlation analysis for main algorithms
    generate_correlation_analysis(correlation_analysis_data, COMPARISON_CHARTS_DIR)
    
    # --- Quick Sort Variants Analysis ---
    print("\nGenerating QuickSort variant analysis...")
    
    # Prepare quick sort variant visualization data
    qs_average_time = {}
    qs_worst_time = {}
    qs_best_time = {}
    
    qs_average_comparisons = {}
    qs_worst_comparisons = {}
    qs_best_comparisons = {}
    
    for quicksort_algorithm, quicksort_categories in quicksort_performance_data.items():
        # Format algorithm name for display
        display_name = quicksort_algorithm.replace('_', ' ').title()
        if "Median Of Three" in display_name:
            display_name = "Quick Sort (Median of Three)"
        elif quicksort_algorithm == "quick_sort_first_pivot":
            display_name = "Quick Sort (First Element Pivot)"
        elif "Random" in display_name:
            display_name = "Quick Sort (Random Pivot)"
        
        # Time-based visualizations
        qs_average_time[display_name] = [(size, time_val) for size, time_val, comp_count in quicksort_categories["random"]]
        qs_worst_time[display_name] = [(size, time_val) for size, time_val, comp_count in quicksort_categories["reverse_sorted"]]
        qs_best_time[display_name] = [(size, time_val) for size, time_val, comp_count in quicksort_categories["sorted"]]
        
        # Comparison-based visualizations
        qs_average_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in quicksort_categories["random"]]
        qs_worst_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in quicksort_categories["reverse_sorted"]]
        qs_best_comparisons[display_name] = [(size, comp_count) for size, time_val, comp_count in quicksort_categories["sorted"]]
    
    # Generate Quick Sort Time vs Size visualizations
    create_performance_visualizations(qs_average_time, "Average Case (Random Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="time")
    create_performance_visualizations(qs_worst_time, "Worst Case (Reverse Sorted Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="time")
    create_performance_visualizations(qs_best_time, "Best Case (Sorted Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="time")
    
    # Generate Quick Sort Comparisons vs Size visualizations
    create_performance_visualizations(qs_average_comparisons, "Average Case (Random Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="comparisons")
    create_performance_visualizations(qs_worst_comparisons, "Worst Case (Reverse Sorted Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="comparisons")
    create_performance_visualizations(qs_best_comparisons, "Best Case (Sorted Input)", QUICKSORT_ANALYSIS_DIR, measurement_type="comparisons")
    
    # Prepare correlation data for quick sort variants
    quicksort_correlation_data = {}
    for quicksort_algorithm, quicksort_categories in quicksort_performance_data.items():
        display_name = quicksort_algorithm.replace('_', ' ').title()
        if "Median Of Three" in display_name:
            display_name = "Quick Sort (Median of Three)"
        elif quicksort_algorithm == "quick_sort_first_pivot":
            display_name = "Quick Sort (First Element Pivot)"
        elif "Random" in display_name:
            display_name = "Quick Sort (Random Pivot)"
        
        # Correlation data - combine all categories
        all_categories_combined = quicksort_categories["random"] + quicksort_categories["sorted"] + quicksort_categories["reverse_sorted"]
        quicksort_correlation_data[display_name] = all_categories_combined
    
    # Generate correlation analysis for quick sort variants
    generate_correlation_analysis(quicksort_correlation_data, QUICKSORT_ANALYSIS_DIR)

    print("\nAll visualizations generated successfully.")
    print(f"Results available in '{VISUALIZATION_OUTPUT_DIR}' directory.")
    print(f"  - Algorithm comparisons: '{COMPARISON_CHARTS_DIR}'")
    print(f"  - Quick sort analysis: '{QUICKSORT_ANALYSIS_DIR}'")
    print(f"  - CSV data exports: '{CSV_EXPORT_DIR}'")
    
    print("\n--- Experimental Methodology ---")
    print(f"Each test configuration executed {EXPERIMENT_REPETITIONS} times, reporting mean execution time.")
    print("Timing mechanism: High-resolution Python `time.perf_counter()` measurements.")
    print("Comparison tracking: Instrumented C code monitors all element comparisons.")
    print("Dataset selection: Pre-generated evaluation data from '{DATASET_DIRECTORY}/' utilized.")
    print("Consistent inputs applied across all algorithms for equitable performance comparison.")
    print("\nBest/Worst Case Classification:")
    print("  - Average Case: Represented by randomized input distributions.")
    print("  - Worst Case: Represented by reverse-sorted input sequences.")
    print("  - Best Case: Represented by pre-sorted input sequences.")
    print("\nCorrelation Analysis Interpretation:")
    print("  Correlation visualizations illustrate the relationship between comparison operations")
    print("  and execution duration. High correlation (approaching 1.0) indicates comparison count")
    print("  strongly predicts execution time for the respective algorithm.")
    
    # --- Performance Results Table ---
    print("\n--- Performance Evaluation Results ---")
    results_table_data = []
    for algorithm_key, category_data in algorithm_performance_data.items():
        # Format algorithm name for display
        formatted_algorithm_name = algorithm_key.replace('_', ' ').title()
        if "Quick Sort Median Of Three Pivot" in formatted_algorithm_name:
            formatted_algorithm_name = "Quick Sort (Median of Three)"
        
        for data_category, performance_results in category_data.items():
            for dataset_size, mean_time, mean_comparisons in performance_results:
                results_table_data.append({
                    "Algorithm": formatted_algorithm_name,
                    "Input Type": data_category.replace('_', ' ').title(),
                    "Dataset Size (N)": dataset_size,
                    "Mean Execution Time (s)": f"{mean_time:.6f}" if mean_time != float('inf') else "Crashed/Timeout",
                    "Mean Comparisons": f"{mean_comparisons:.0f}" if mean_time != float('inf') else "N/A"
                })
    
    performance_dataframe = pd.DataFrame(results_table_data)
    sorted_dataframe = performance_dataframe.sort_values(by=["Dataset Size (N)", "Input Type", "Algorithm"])
    print(sorted_dataframe.to_string(index=False))

    # Export results to CSV
    csv_export_path = os.path.join(CSV_EXPORT_DIR, "comprehensive_sorting_performance_results.csv")
    sorted_dataframe.to_csv(csv_export_path, index=False)
    print(f"\nComplete results table exported to {csv_export_path}")
    
    # --- Statistical Correlation Summary ---
    print("\n--- Statistical Correlation Analysis ---")
    print("Algorithm                           | Correlation (r) | P-value")
    print("-" * 70)
    for algorithm_name, performance_points in correlation_analysis_data.items():
        execution_times = [dp[1] for dp in performance_points if dp[1] != float('inf')]
        comparison_operations = [dp[2] for dp in performance_points if dp[1] != float('inf')]
        
        if len(execution_times) > 1 and len(comparison_operations) > 1:
            correlation_coefficient, statistical_p_value = pearsonr(comparison_operations, execution_times)
            print(f"{algorithm_name:<35} | {correlation_coefficient:>15.4f} | {statistical_p_value:.4e}")
    
    print("\nStatistical Interpretation:")
    print("  r ≈ 1.0: Strong positive correlation (increased comparisons → increased time)")
    print("  r ≈ 0.0: Weak or negligible correlation")
    print("  p-value < 0.05: Statistically significant correlation")
    
    # --- Critical Performance Notes ---
    print("\n" + "="*80)
    print("CRITICAL PERFORMANCE EVALUATION NOTES")
    print("="*80)
    
    print("\n⚠️  TIMING MEASUREMENT PROTOCOL:")
    print("  - Execution timing measured within C code using clock_gettime(CLOCK_MONOTONIC)")
    print("  - This approach eliminates Python subprocess overhead from measurements")
    print("  - Results accurately reflect actual algorithmic performance characteristics")
    
    print("\n⚠️  RADIX SORT COMPARISON METRIC NOTE:")
    print("  - Radix sort implements a NON-COMPARATIVE sorting paradigm")
    print("  - Algorithm does not perform element-to-element comparisons (unlike other methods)")
    print("  - 'Comparisons' metric represents getMax() function operations (~n)")
    print("  - This value is NOT directly comparable to other algorithms' comparison counts")
    print("  - Utilize TIME metric rather than COMPARISONS for radix sort performance evaluation")
    
    print("\n✓ EXPECTED ALGORITHMIC BEHAVIOR:")
    print("  - O(n²) complexity: Bubble, Insertion, Selection Sort algorithms")
    print("  - O(n log n) complexity: Heap, Merge, Quick Sort algorithms")
    print("  - O(n+k) complexity: Radix Sort (where k represents key range)")
    print("  - Optimized best-case: Bubble & Insertion sort demonstrate O(n) for sorted inputs")
    print("="*80)