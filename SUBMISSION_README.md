# Sorting Algorithms Benchmarking - Submission Guide

This package contains the source code and benchmarking tools used for the CS-253 Practical Assignment.

## Project Structure
- `sorting_algorithms/`: C implementations of all 7 sorting algorithms and Quick Sort variants.
- `benchmark.py`: The main Python script that automates compilation, execution, and data analysis.
- `generate_test_data.py`: Script used to generate the random, sorted, and reverse-sorted datasets.
- `test_data/`: Directory containing the pre-generated input files.
- `graphs/`: (Generated after running) Contains the CSV results and visualization plots.

## Prerequisites
- **C Compiler**: `gcc` (MinGW for Windows or standard GCC for Linux/macOS).
- **Python 3.x**: With the following libraries installed:
  ```bash
  pip install matplotlib pandas numpy scipy
  ```

## How to Run the Benchmarks
1. **Navigate to the project directory**:
   ```bash
   cd Sorting-algorithms-benchmark
   ```
2. **Generate Test Data** (Optional, if not already present):
   ```bash
   python generate_test_data.py
   ```
3. **Run the Benchmark**:
   ```bash
   python benchmark.py
   ```
   *Note: The script will automatically compile the C files into an `executables/` folder and run them against the data in `test_data/`.*

4. **View Results**:
   - Numerical data will be saved in `graphs/csv_data/`.
   - Visualization plots will be available in `graphs/7_sorting_algo_comparisons/` and `graphs/quick_sort_analysis/`.

## Authors
- Aryan Bokolia (241CS111)
- Rishinandan D R (241CS145)

---

### Terminal Output

```
──(kali㉿kali)-[~/Documents/Sorting-Algo-DAA]
└─$ python benchmark.py         
Building executable from sorting_algorithms/bubble_sort.c...
Successfully compiled sorting_algorithms/bubble_sort.c -> executables/bubble_sort
Building executable from sorting_algorithms/heap_sort.c...
Successfully compiled sorting_algorithms/heap_sort.c -> executables/heap_sort
Building executable from sorting_algorithms/insertion_sort.c...
Successfully compiled sorting_algorithms/insertion_sort.c -> executables/insertion_sort
Building executable from sorting_algorithms/merge_sort.c...
Successfully compiled sorting_algorithms/merge_sort.c -> executables/merge_sort
Building executable from sorting_algorithms/quick_sort_median_of_three_pivot.c...
Successfully compiled sorting_algorithms/quick_sort_median_of_three_pivot.c -> executables/quick_sort_median_of_three_pivot
Building executable from sorting_algorithms/radix_sort.c...
Successfully compiled sorting_algorithms/radix_sort.c -> executables/radix_sort
Building executable from sorting_algorithms/selection_sort.c...
Successfully compiled sorting_algorithms/selection_sort.c -> executables/selection_sort
Building executable from sorting_algorithms/quick_sort_first_pivot.c...
Successfully compiled sorting_algorithms/quick_sort_first_pivot.c -> executables/quick_sort_first_pivot
Building executable from sorting_algorithms/quick_sort_median_of_three_pivot.c...
Successfully compiled sorting_algorithms/quick_sort_median_of_three_pivot.c -> executables/quick_sort_median_of_three_pivot
Building executable from sorting_algorithms/quick_sort_random_pivot.c...
Successfully compiled sorting_algorithms/quick_sort_random_pivot.c -> executables/quick_sort_random_pivot

Initiating performance evaluation...
Evaluating dataset size=100, category=random...
  bubble_sort: Time = 0.000035 s, Comparisons = 4895
  heap_sort: Time = 0.000012 s, Comparisons = 1028
  insertion_sort: Time = 0.000013 s, Comparisons = 2636
  merge_sort: Time = 0.000015 s, Comparisons = 542
  quick_sort_median_of_three_pivot: Time = 0.000009 s, Comparisons = 785
  radix_sort: Time = 0.000007 s, Comparisons = 99
  selection_sort: Time = 0.000020 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000008 s, Comparisons = 594
  quick_sort_median_of_three_pivot: Time = 0.000010 s, Comparisons = 785
  quick_sort_random_pivot: Time = 0.000113 s, Comparisons = 644
Evaluating dataset size=100, category=reverse_sorted...
  bubble_sort: Time = 0.000030 s, Comparisons = 4950
  heap_sort: Time = 0.000011 s, Comparisons = 944
  insertion_sort: Time = 0.000019 s, Comparisons = 4950
  merge_sort: Time = 0.000010 s, Comparisons = 316
  quick_sort_median_of_three_pivot: Time = 0.000006 s, Comparisons = 868
  radix_sort: Time = 0.000004 s, Comparisons = 99
  selection_sort: Time = 0.000014 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000021 s, Comparisons = 4950
  quick_sort_median_of_three_pivot: Time = 0.000008 s, Comparisons = 868
  quick_sort_random_pivot: Time = 0.000069 s, Comparisons = 669
Evaluating dataset size=100, category=sorted...
  bubble_sort: Time = 0.000000 s, Comparisons = 99
  heap_sort: Time = 0.000012 s, Comparisons = 1081
  insertion_sort: Time = 0.000001 s, Comparisons = 99
  merge_sort: Time = 0.000012 s, Comparisons = 356
  quick_sort_median_of_three_pivot: Time = 0.000004 s, Comparisons = 669
  radix_sort: Time = 0.000005 s, Comparisons = 99
  selection_sort: Time = 0.000015 s, Comparisons = 4950
  quick_sort_first_pivot: Time = 0.000015 s, Comparisons = 4950
  quick_sort_median_of_three_pivot: Time = 0.000005 s, Comparisons = 669
  quick_sort_random_pivot: Time = 0.000092 s, Comparisons = 621
Evaluating dataset size=500, category=random...
  bubble_sort: Time = 0.000798 s, Comparisons = 124372
  heap_sort: Time = 0.000097 s, Comparisons = 7443
  insertion_sort: Time = 0.000228 s, Comparisons = 63070
  merge_sort: Time = 0.000086 s, Comparisons = 3859
  quick_sort_median_of_three_pivot: Time = 0.000051 s, Comparisons = 5199
  radix_sort: Time = 0.000029 s, Comparisons = 499
  selection_sort: Time = 0.001513 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000046 s, Comparisons = 4695
  quick_sort_median_of_three_pivot: Time = 0.000055 s, Comparisons = 5199
  quick_sort_random_pivot: Time = 0.001275 s, Comparisons = 4793
Evaluating dataset size=500, category=reverse_sorted...
  bubble_sort: Time = 0.000523 s, Comparisons = 124750
  heap_sort: Time = 0.000080 s, Comparisons = 7010
  insertion_sort: Time = 0.000457 s, Comparisons = 124750
  merge_sort: Time = 0.000053 s, Comparisons = 2216
  quick_sort_median_of_three_pivot: Time = 0.000038 s, Comparisons = 6790
  radix_sort: Time = 0.000022 s, Comparisons = 499
  selection_sort: Time = 0.000604 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000551 s, Comparisons = 124750
  quick_sort_median_of_three_pivot: Time = 0.000037 s, Comparisons = 6790
  quick_sort_random_pivot: Time = 0.000507 s, Comparisons = 4499
Evaluating dataset size=500, category=sorted...
  bubble_sort: Time = 0.000002 s, Comparisons = 499
  heap_sort: Time = 0.000089 s, Comparisons = 7756
  insertion_sort: Time = 0.000002 s, Comparisons = 499
  merge_sort: Time = 0.000044 s, Comparisons = 2272
  quick_sort_median_of_three_pivot: Time = 0.000017 s, Comparisons = 4263
  radix_sort: Time = 0.000028 s, Comparisons = 499
  selection_sort: Time = 0.000328 s, Comparisons = 124750
  quick_sort_first_pivot: Time = 0.000379 s, Comparisons = 124750
  quick_sort_median_of_three_pivot: Time = 0.000017 s, Comparisons = 4263
  quick_sort_random_pivot: Time = 0.000456 s, Comparisons = 5329
Evaluating dataset size=1000, category=random...
  bubble_sort: Time = 0.002094 s, Comparisons = 496725
  heap_sort: Time = 0.000219 s, Comparisons = 16909
  insertion_sort: Time = 0.000972 s, Comparisons = 253779
  merge_sort: Time = 0.000187 s, Comparisons = 8740
  quick_sort_median_of_three_pivot: Time = 0.000120 s, Comparisons = 11104
  radix_sort: Time = 0.000068 s, Comparisons = 999
  selection_sort: Time = 0.001748 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.000124 s, Comparisons = 11762
  quick_sort_median_of_three_pivot: Time = 0.000135 s, Comparisons = 11104
  quick_sort_random_pivot: Time = 0.000818 s, Comparisons = 10014
Evaluating dataset size=1000, category=reverse_sorted...
  bubble_sort: Time = 0.003585 s, Comparisons = 499500
  heap_sort: Time = 0.000172 s, Comparisons = 15965
  insertion_sort: Time = 0.001641 s, Comparisons = 499500
  merge_sort: Time = 0.000096 s, Comparisons = 4932
  quick_sort_median_of_three_pivot: Time = 0.000091 s, Comparisons = 15849
  radix_sort: Time = 0.000050 s, Comparisons = 999
  selection_sort: Time = 0.001484 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.002199 s, Comparisons = 499500
  quick_sort_median_of_three_pivot: Time = 0.000077 s, Comparisons = 15849
  quick_sort_random_pivot: Time = 0.001044 s, Comparisons = 10133
Evaluating dataset size=1000, category=sorted...
  bubble_sort: Time = 0.000004 s, Comparisons = 999
  heap_sort: Time = 0.000187 s, Comparisons = 17583
  insertion_sort: Time = 0.000003 s, Comparisons = 999
  merge_sort: Time = 0.000101 s, Comparisons = 5044
  quick_sort_median_of_three_pivot: Time = 0.000039 s, Comparisons = 9520
  radix_sort: Time = 0.000089 s, Comparisons = 999
  selection_sort: Time = 0.001747 s, Comparisons = 499500
  quick_sort_first_pivot: Time = 0.002041 s, Comparisons = 499500
  quick_sort_median_of_three_pivot: Time = 0.000038 s, Comparisons = 9520
  quick_sort_random_pivot: Time = 0.000801 s, Comparisons = 10792
Evaluating dataset size=5000, category=random...
  bubble_sort: Time = 0.062006 s, Comparisons = 12484620
  heap_sort: Time = 0.001315 s, Comparisons = 107650
  insertion_sort: Time = 0.022418 s, Comparisons = 6127844
  merge_sort: Time = 0.001164 s, Comparisons = 55115
  quick_sort_median_of_three_pivot: Time = 0.000645 s, Comparisons = 69487
  radix_sort: Time = 0.000428 s, Comparisons = 4999
  selection_sort: Time = 0.039483 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.000622 s, Comparisons = 68231
  quick_sort_median_of_three_pivot: Time = 0.000604 s, Comparisons = 69487
  quick_sort_random_pivot: Time = 0.005633 s, Comparisons = 72950
Evaluating dataset size=5000, category=reverse_sorted...
  bubble_sort: Time = 0.054603 s, Comparisons = 12497500
  heap_sort: Time = 0.001743 s, Comparisons = 103227
  insertion_sort: Time = 0.044004 s, Comparisons = 12497500
  merge_sort: Time = 0.000893 s, Comparisons = 29804
  quick_sort_median_of_three_pivot: Time = 0.000528 s, Comparisons = 106182
  radix_sort: Time = 0.000358 s, Comparisons = 4999
  selection_sort: Time = 0.039266 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.048810 s, Comparisons = 12497500
  quick_sort_median_of_three_pivot: Time = 0.000429 s, Comparisons = 106182
  quick_sort_random_pivot: Time = 0.004127 s, Comparisons = 75497
Evaluating dataset size=5000, category=sorted...
  bubble_sort: Time = 0.000015 s, Comparisons = 4999
  heap_sort: Time = 0.001136 s, Comparisons = 112126
  insertion_sort: Time = 0.000016 s, Comparisons = 4999
  merge_sort: Time = 0.001225 s, Comparisons = 32004
  quick_sort_median_of_three_pivot: Time = 0.000273 s, Comparisons = 60678
  radix_sort: Time = 0.000301 s, Comparisons = 4999
  selection_sort: Time = 0.041061 s, Comparisons = 12497500
  quick_sort_first_pivot: Time = 0.038803 s, Comparisons = 12497500
  quick_sort_median_of_three_pivot: Time = 0.000306 s, Comparisons = 60678
  quick_sort_random_pivot: Time = 0.004239 s, Comparisons = 73381
Evaluating dataset size=10000, category=random...
  bubble_sort: Time = 0.198312 s, Comparisons = 49969575
  heap_sort: Time = 0.003475 s, Comparisons = 235194
  insertion_sort: Time = 0.086758 s, Comparisons = 25111913
  merge_sort: Time = 0.002616 s, Comparisons = 120439
  quick_sort_median_of_three_pivot: Time = 0.001414 s, Comparisons = 146509
  radix_sort: Time = 0.000783 s, Comparisons = 9999
  selection_sort: Time = 0.155764 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.001386 s, Comparisons = 151047
  quick_sort_median_of_three_pivot: Time = 0.001825 s, Comparisons = 146509
  quick_sort_random_pivot: Time = 0.011616 s, Comparisons = 148453
Evaluating dataset size=10000, category=reverse_sorted...
  bubble_sort: Time = 0.208647 s, Comparisons = 49995000
  heap_sort: Time = 0.002604 s, Comparisons = 226682
  insertion_sort: Time = 0.171012 s, Comparisons = 49995000
  merge_sort: Time = 0.004921 s, Comparisons = 64608
  quick_sort_median_of_three_pivot: Time = 0.000836 s, Comparisons = 234923
  radix_sort: Time = 0.000576 s, Comparisons = 9999
  selection_sort: Time = 0.155836 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.173341 s, Comparisons = 49995000
  quick_sort_median_of_three_pivot: Time = 0.001263 s, Comparisons = 234923
  quick_sort_random_pivot: Time = 0.011664 s, Comparisons = 164858
Evaluating dataset size=10000, category=sorted...
  bubble_sort: Time = 0.000029 s, Comparisons = 9999
  heap_sort: Time = 0.002191 s, Comparisons = 244460
  insertion_sort: Time = 0.000028 s, Comparisons = 9999
  merge_sort: Time = 0.001229 s, Comparisons = 69008
  quick_sort_median_of_three_pivot: Time = 0.000570 s, Comparisons = 131343
  radix_sort: Time = 0.000586 s, Comparisons = 9999
  selection_sort: Time = 0.154614 s, Comparisons = 49995000
  quick_sort_first_pivot: Time = 0.155301 s, Comparisons = 49995000
  quick_sort_median_of_three_pivot: Time = 0.000663 s, Comparisons = 131343
  quick_sort_random_pivot: Time = 0.009389 s, Comparisons = 158908
Evaluating dataset size=25000, category=random...
  bubble_sort: Time = 1.738591 s, Comparisons = 312483672
  heap_sort: Time = 0.007906 s, Comparisons = 654959
  insertion_sort: Time = 0.509035 s, Comparisons = 155819568
  merge_sort: Time = 0.007990 s, Comparisons = 334198
  quick_sort_median_of_three_pivot: Time = 0.003924 s, Comparisons = 406541
  radix_sort: Time = 0.001990 s, Comparisons = 24999
  selection_sort: Time = 0.971079 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 0.003503 s, Comparisons = 453877
  quick_sort_median_of_three_pivot: Time = 0.005976 s, Comparisons = 406541
  quick_sort_random_pivot: Time = 0.023968 s, Comparisons = 429402
Evaluating dataset size=25000, category=reverse_sorted...
  bubble_sort: Time = 1.286002 s, Comparisons = 312487500
  heap_sort: Time = 0.006169 s, Comparisons = 633719
  insertion_sort: Time = 0.984622 s, Comparisons = 312487500
  merge_sort: Time = 0.005030 s, Comparisons = 178756
  quick_sort_median_of_three_pivot: Time = 0.003781 s, Comparisons = 660758
  radix_sort: Time = 0.002304 s, Comparisons = 24999
  selection_sort: Time = 0.966563 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 1.102579 s, Comparisons = 312487500
  quick_sort_median_of_three_pivot: Time = 0.004466 s, Comparisons = 660758
  quick_sort_random_pivot: Time = 0.026630 s, Comparisons = 436217
Evaluating dataset size=25000, category=sorted...
  bubble_sort: Time = 0.000255 s, Comparisons = 24999
  heap_sort: Time = 0.005866 s, Comparisons = 677688
  insertion_sort: Time = 0.000077 s, Comparisons = 24999
  merge_sort: Time = 0.002681 s, Comparisons = 188476
  quick_sort_median_of_three_pivot: Time = 0.001524 s, Comparisons = 366397
  radix_sort: Time = 0.002444 s, Comparisons = 24999
  selection_sort: Time = 1.784183 s, Comparisons = 312487500
  quick_sort_first_pivot: Time = 1.378714 s, Comparisons = 312487500
  quick_sort_median_of_three_pivot: Time = 0.001002 s, Comparisons = 366397
  quick_sort_random_pivot: Time = 0.015006 s, Comparisons = 411432
Evaluating dataset size=50000, category=random...
  bubble_sort: Time = 5.025651 s, Comparisons = 1249805929
  heap_sort: Time = 0.014543 s, Comparisons = 1409865
  insertion_sort: Time = 1.381375 s, Comparisons = 625874287
  merge_sort: Time = 0.011187 s, Comparisons = 718192
  quick_sort_median_of_three_pivot: Time = 0.006198 s, Comparisons = 874800
  radix_sort: Time = 0.003069 s, Comparisons = 49999
  selection_sort: Time = 2.650236 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 0.005319 s, Comparisons = 918948
  quick_sort_median_of_three_pivot: Time = 0.007935 s, Comparisons = 874800
  quick_sort_random_pivot: Time = 0.029975 s, Comparisons = 999406
Evaluating dataset size=50000, category=reverse_sorted...
  bubble_sort: Time = 3.520148 s, Comparisons = 1249975000
  heap_sort: Time = 0.008775 s, Comparisons = 1366047
  insertion_sort: Time = 2.760166 s, Comparisons = 1249975000
  merge_sort: Time = 0.003677 s, Comparisons = 382512
  quick_sort_median_of_three_pivot: Time = 0.005474 s, Comparisons = 1433133
  radix_sort: Time = 0.002338 s, Comparisons = 49999
  selection_sort: Time = 2.626613 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 3.075647 s, Comparisons = 1249975000
  quick_sort_median_of_three_pivot: Time = 0.004060 s, Comparisons = 1433133
  quick_sort_random_pivot: Time = 0.035788 s, Comparisons = 939863
Evaluating dataset size=50000, category=sorted...
  bubble_sort: Time = 0.000093 s, Comparisons = 49999
  heap_sort: Time = 0.012655 s, Comparisons = 1455438
  insertion_sort: Time = 0.000128 s, Comparisons = 49999
  merge_sort: Time = 0.004302 s, Comparisons = 401952
  quick_sort_median_of_three_pivot: Time = 0.002815 s, Comparisons = 782782
  radix_sort: Time = 0.002775 s, Comparisons = 49999
  selection_sort: Time = 2.736064 s, Comparisons = 1249975000
  quick_sort_first_pivot: Time = 2.631822 s, Comparisons = 1249975000
  quick_sort_median_of_three_pivot: Time = 0.002674 s, Comparisons = 782782
  quick_sort_random_pivot: Time = 0.032046 s, Comparisons = 936262
Evaluating dataset size=75000, category=random...
  bubble_sort: Time = 13.015469 s, Comparisons = 2812406889
  heap_sort: Time = 0.016775 s, Comparisons = 2200213
  insertion_sort: Time = 3.153109 s, Comparisons = 1407462177
  merge_sort: Time = 0.012212 s, Comparisons = 1121123
  quick_sort_median_of_three_pivot: Time = 0.009933 s, Comparisons = 1378985
  radix_sort: Time = 0.004007 s, Comparisons = 74999
  selection_sort: Time = 6.038297 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 0.011031 s, Comparisons = 1576706
  quick_sort_median_of_three_pivot: Time = 0.008343 s, Comparisons = 1378985
  quick_sort_random_pivot: Time = 0.052997 s, Comparisons = 1531478
Evaluating dataset size=75000, category=reverse_sorted...
  bubble_sort: Time = 7.927747 s, Comparisons = 2812462500
  heap_sort: Time = 0.013935 s, Comparisons = 2138650
  insertion_sort: Time = 6.306414 s, Comparisons = 2812462500
  merge_sort: Time = 0.005946 s, Comparisons = 594612
  quick_sort_median_of_three_pivot: Time = 0.006389 s, Comparisons = 2272487
  radix_sort: Time = 0.003386 s, Comparisons = 74999
  selection_sort: Time = 5.885482 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 6.619053 s, Comparisons = 2812462500
  quick_sort_median_of_three_pivot: Time = 0.008699 s, Comparisons = 2272487
  quick_sort_random_pivot: Time = 0.047170 s, Comparisons = 1496065
Evaluating dataset size=75000, category=sorted...
  bubble_sort: Time = 0.000187 s, Comparisons = 74999
  heap_sort: Time = 0.013620 s, Comparisons = 2268087
  insertion_sort: Time = 0.000156 s, Comparisons = 74999
  merge_sort: Time = 0.005722 s, Comparisons = 624316
  quick_sort_median_of_three_pivot: Time = 0.003228 s, Comparisons = 1195642
  radix_sort: Time = 0.003488 s, Comparisons = 74999
  selection_sort: Time = 6.125949 s, Comparisons = 2812462500
  quick_sort_first_pivot: Time = 5.743560 s, Comparisons = 2812462500
  quick_sort_median_of_three_pivot: Time = 0.003542 s, Comparisons = 1195642
  quick_sort_random_pivot: Time = 0.043377 s, Comparisons = 1526441
Evaluating dataset size=100000, category=random...
  bubble_sort: Time = 22.857072 s, Comparisons = 4999746159
  heap_sort: Time = 0.023261 s, Comparisons = 3019917
  insertion_sort: Time = 5.465526 s, Comparisons = 2508124174
  merge_sort: Time = 0.019851 s, Comparisons = 1536545
  quick_sort_median_of_three_pivot: Time = 0.010984 s, Comparisons = 1904754
  radix_sort: Time = 0.006380 s, Comparisons = 99999
  selection_sort: Time = 10.747956 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 0.013017 s, Comparisons = 2034747
  quick_sort_median_of_three_pivot: Time = 0.011255 s, Comparisons = 1904754
  quick_sort_random_pivot: Time = 0.057731 s, Comparisons = 1939896
Evaluating dataset size=100000, category=reverse_sorted...
  bubble_sort: Time = 14.045717 s, Comparisons = 4999950000
  heap_sort: Time = 0.017061 s, Comparisons = 2926640
  insertion_sort: Time = 10.604652 s, Comparisons = 4999950000
  merge_sort: Time = 0.007389 s, Comparisons = 815024
  quick_sort_median_of_three_pivot: Time = 0.008388 s, Comparisons = 3107283
  radix_sort: Time = 0.004301 s, Comparisons = 99999
  selection_sort: Time = 10.573512 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 9.980484 s, Comparisons = 4999950000
  quick_sort_median_of_three_pivot: Time = 0.006458 s, Comparisons = 3107283
  quick_sort_random_pivot: Time = 0.043393 s, Comparisons = 1966695
Evaluating dataset size=100000, category=sorted...
  bubble_sort: Time = 0.000171 s, Comparisons = 99999
  heap_sort: Time = 0.014340 s, Comparisons = 3112517
  insertion_sort: Time = 0.000180 s, Comparisons = 99999
  merge_sort: Time = 0.006181 s, Comparisons = 853904
  quick_sort_median_of_three_pivot: Time = 0.004786 s, Comparisons = 1665551
  radix_sort: Time = 0.003749 s, Comparisons = 99999
  selection_sort: Time = 8.109508 s, Comparisons = 4999950000
  quick_sort_first_pivot: Time = 8.087411 s, Comparisons = 4999950000
  quick_sort_median_of_three_pivot: Time = 0.005809 s, Comparisons = 1665551
  quick_sort_random_pivot: Time = 0.047182 s, Comparisons = 1997238

Performance evaluation completed. Generating visualizations...
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_average_case_(random_input)_time.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_average_case_(random_input)_time_log_scale.png
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_worst_case_(reverse_sorted_input)_time.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_worst_case_(reverse_sorted_input)_time_log_scale.png
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_best_case_(sorted_input)_time.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_best_case_(sorted_input)_time_log_scale.png
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_average_case_(random_input)_comparisons.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_average_case_(random_input)_comparisons_log_scale.png
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_worst_case_(reverse_sorted_input)_comparisons.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_worst_case_(reverse_sorted_input)_comparisons_log_scale.png
Generated visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_best_case_(sorted_input)_comparisons.png
Generated logarithmic visualization: graphs/7_sorting_algo_comparisons/algorithm_performance_best_case_(sorted_input)_comparisons_log_scale.png
Generated correlation analysis: graphs/7_sorting_algo_comparisons/time_vs_comparisons_correlation.png

Generating QuickSort variant analysis...
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_average_case_(random_input)_time.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_average_case_(random_input)_time_log_scale.png
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_worst_case_(reverse_sorted_input)_time.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_worst_case_(reverse_sorted_input)_time_log_scale.png
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_best_case_(sorted_input)_time.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_best_case_(sorted_input)_time_log_scale.png
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_average_case_(random_input)_comparisons.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_average_case_(random_input)_comparisons_log_scale.png
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_worst_case_(reverse_sorted_input)_comparisons.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_worst_case_(reverse_sorted_input)_comparisons_log_scale.png
Generated visualization: graphs/quick_sort_analysis/algorithm_performance_best_case_(sorted_input)_comparisons.png
Generated logarithmic visualization: graphs/quick_sort_analysis/algorithm_performance_best_case_(sorted_input)_comparisons_log_scale.png
Generated correlation analysis: graphs/quick_sort_analysis/time_vs_comparisons_correlation.png

All visualizations generated successfully.
Results available in 'graphs' directory.
  - Algorithm comparisons: 'graphs/7_sorting_algo_comparisons'
  - Quick sort analysis: 'graphs/quick_sort_analysis'
  - CSV data exports: 'graphs/csv_data'

--- Experimental Methodology ---
Each test configuration executed 7 times, reporting mean execution time.
Timing mechanism: High-resolution Python `time.perf_counter()` measurements.
Comparison tracking: Instrumented C code monitors all element comparisons.
Dataset selection: Pre-generated evaluation data from '{DATASET_DIRECTORY}/' utilized.
Consistent inputs applied across all algorithms for equitable performance comparison.

Best/Worst Case Classification:
  - Average Case: Represented by randomized input distributions.
  - Worst Case: Represented by reverse-sorted input sequences.
  - Best Case: Represented by pre-sorted input sequences.

Correlation Analysis Interpretation:
  Correlation visualizations illustrate the relationship between comparison operations
  and execution duration. High correlation (approaching 1.0) indicates comparison count
  strongly predicts execution time for the respective algorithm.

--- Performance Evaluation Results ---
                   Algorithm     Input Type  Dataset Size (N) Mean Execution Time (s) Mean Comparisons
                 Bubble Sort         Random               100                0.000035             4895
                   Heap Sort         Random               100                0.000012             1028
              Insertion Sort         Random               100                0.000013             2636
                  Merge Sort         Random               100                0.000015              542
Quick Sort (Median of Three)         Random               100                0.000009              785
                  Radix Sort         Random               100                0.000007               99
              Selection Sort         Random               100                0.000020             4950
                 Bubble Sort Reverse Sorted               100                0.000030             4950
                   Heap Sort Reverse Sorted               100                0.000011              944
              Insertion Sort Reverse Sorted               100                0.000019             4950
                  Merge Sort Reverse Sorted               100                0.000010              316
Quick Sort (Median of Three) Reverse Sorted               100                0.000006              868
                  Radix Sort Reverse Sorted               100                0.000004               99
              Selection Sort Reverse Sorted               100                0.000014             4950
                 Bubble Sort         Sorted               100                0.000000               99
                   Heap Sort         Sorted               100                0.000012             1081
              Insertion Sort         Sorted               100                0.000001               99
                  Merge Sort         Sorted               100                0.000012              356
Quick Sort (Median of Three)         Sorted               100                0.000004              669
                  Radix Sort         Sorted               100                0.000005               99
              Selection Sort         Sorted               100                0.000015             4950
                 Bubble Sort         Random               500                0.000798           124372
                   Heap Sort         Random               500                0.000097             7443
              Insertion Sort         Random               500                0.000228            63070
                  Merge Sort         Random               500                0.000086             3859
Quick Sort (Median of Three)         Random               500                0.000051             5199
                  Radix Sort         Random               500                0.000029              499
              Selection Sort         Random               500                0.001513           124750
                 Bubble Sort Reverse Sorted               500                0.000523           124750
                   Heap Sort Reverse Sorted               500                0.000080             7010
              Insertion Sort Reverse Sorted               500                0.000457           124750
                  Merge Sort Reverse Sorted               500                0.000053             2216
Quick Sort (Median of Three) Reverse Sorted               500                0.000038             6790
                  Radix Sort Reverse Sorted               500                0.000022              499
              Selection Sort Reverse Sorted               500                0.000604           124750
                 Bubble Sort         Sorted               500                0.000002              499
                   Heap Sort         Sorted               500                0.000089             7756
              Insertion Sort         Sorted               500                0.000002              499
                  Merge Sort         Sorted               500                0.000044             2272
Quick Sort (Median of Three)         Sorted               500                0.000017             4263
                  Radix Sort         Sorted               500                0.000028              499
              Selection Sort         Sorted               500                0.000328           124750
                 Bubble Sort         Random              1000                0.002094           496725
                   Heap Sort         Random              1000                0.000219            16909
              Insertion Sort         Random              1000                0.000972           253779
                  Merge Sort         Random              1000                0.000187             8740
Quick Sort (Median of Three)         Random              1000                0.000120            11104
                  Radix Sort         Random              1000                0.000068              999
              Selection Sort         Random              1000                0.001748           499500
                 Bubble Sort Reverse Sorted              1000                0.003585           499500
                   Heap Sort Reverse Sorted              1000                0.000172            15965
              Insertion Sort Reverse Sorted              1000                0.001641           499500
                  Merge Sort Reverse Sorted              1000                0.000096             4932
Quick Sort (Median of Three) Reverse Sorted              1000                0.000091            15849
                  Radix Sort Reverse Sorted              1000                0.000050              999
              Selection Sort Reverse Sorted              1000                0.001484           499500
                 Bubble Sort         Sorted              1000                0.000004              999
                   Heap Sort         Sorted              1000                0.000187            17583
              Insertion Sort         Sorted              1000                0.000003              999
                  Merge Sort         Sorted              1000                0.000101             5044
Quick Sort (Median of Three)         Sorted              1000                0.000039             9520
                  Radix Sort         Sorted              1000                0.000089              999
              Selection Sort         Sorted              1000                0.001747           499500
                 Bubble Sort         Random              5000                0.062006         12484620
                   Heap Sort         Random              5000                0.001315           107650
              Insertion Sort         Random              5000                0.022418          6127844
                  Merge Sort         Random              5000                0.001164            55115
Quick Sort (Median of Three)         Random              5000                0.000645            69487
                  Radix Sort         Random              5000                0.000428             4999
              Selection Sort         Random              5000                0.039483         12497500
                 Bubble Sort Reverse Sorted              5000                0.054603         12497500
                   Heap Sort Reverse Sorted              5000                0.001743           103227
              Insertion Sort Reverse Sorted              5000                0.044004         12497500
                  Merge Sort Reverse Sorted              5000                0.000893            29804
Quick Sort (Median of Three) Reverse Sorted              5000                0.000528           106182
                  Radix Sort Reverse Sorted              5000                0.000358             4999
              Selection Sort Reverse Sorted              5000                0.039266         12497500
                 Bubble Sort         Sorted              5000                0.000015             4999
                   Heap Sort         Sorted              5000                0.001136           112126
              Insertion Sort         Sorted              5000                0.000016             4999
                  Merge Sort         Sorted              5000                0.001225            32004
Quick Sort (Median of Three)         Sorted              5000                0.000273            60678
                  Radix Sort         Sorted              5000                0.000301             4999
              Selection Sort         Sorted              5000                0.041061         12497500
                 Bubble Sort         Random             10000                0.198312         49969575
                   Heap Sort         Random             10000                0.003475           235194
              Insertion Sort         Random             10000                0.086758         25111913
                  Merge Sort         Random             10000                0.002616           120439
Quick Sort (Median of Three)         Random             10000                0.001414           146509
                  Radix Sort         Random             10000                0.000783             9999
              Selection Sort         Random             10000                0.155764         49995000
                 Bubble Sort Reverse Sorted             10000                0.208647         49995000
                   Heap Sort Reverse Sorted             10000                0.002604           226682
              Insertion Sort Reverse Sorted             10000                0.171012         49995000
                  Merge Sort Reverse Sorted             10000                0.004921            64608
Quick Sort (Median of Three) Reverse Sorted             10000                0.000836           234923
                  Radix Sort Reverse Sorted             10000                0.000576             9999
              Selection Sort Reverse Sorted             10000                0.155836         49995000
                 Bubble Sort         Sorted             10000                0.000029             9999
                   Heap Sort         Sorted             10000                0.002191           244460
              Insertion Sort         Sorted             10000                0.000028             9999
                  Merge Sort         Sorted             10000                0.001229            69008
Quick Sort (Median of Three)         Sorted             10000                0.000570           131343
                  Radix Sort         Sorted             10000                0.000586             9999
              Selection Sort         Sorted             10000                0.154614         49995000
                 Bubble Sort         Random             25000                1.738591        312483672
                   Heap Sort         Random             25000                0.007906           654959
              Insertion Sort         Random             25000                0.509035        155819568
                  Merge Sort         Random             25000                0.007990           334198
Quick Sort (Median of Three)         Random             25000                0.003924           406541
                  Radix Sort         Random             25000                0.001990            24999
              Selection Sort         Random             25000                0.971079        312487500
                 Bubble Sort Reverse Sorted             25000                1.286002        312487500
                   Heap Sort Reverse Sorted             25000                0.006169           633719
              Insertion Sort Reverse Sorted             25000                0.984622        312487500
                  Merge Sort Reverse Sorted             25000                0.005030           178756
Quick Sort (Median of Three) Reverse Sorted             25000                0.003781           660758
                  Radix Sort Reverse Sorted             25000                0.002304            24999
              Selection Sort Reverse Sorted             25000                0.966563        312487500
                 Bubble Sort         Sorted             25000                0.000255            24999
                   Heap Sort         Sorted             25000                0.005866           677688
              Insertion Sort         Sorted             25000                0.000077            24999
                  Merge Sort         Sorted             25000                0.002681           188476
Quick Sort (Median of Three)         Sorted             25000                0.001524           366397
                  Radix Sort         Sorted             25000                0.002444            24999
              Selection Sort         Sorted             25000                1.784183        312487500
                 Bubble Sort         Random             50000                5.025651       1249805929
                   Heap Sort         Random             50000                0.014543          1409865
              Insertion Sort         Random             50000                1.381375        625874287
                  Merge Sort         Random             50000                0.011187           718192
Quick Sort (Median of Three)         Random             50000                0.006198           874800
                  Radix Sort         Random             50000                0.003069            49999
              Selection Sort         Random             50000                2.650236       1249975000
                 Bubble Sort Reverse Sorted             50000                3.520148       1249975000
                   Heap Sort Reverse Sorted             50000                0.008775          1366047
              Insertion Sort Reverse Sorted             50000                2.760166       1249975000
                  Merge Sort Reverse Sorted             50000                0.003677           382512
Quick Sort (Median of Three) Reverse Sorted             50000                0.005474          1433133
                  Radix Sort Reverse Sorted             50000                0.002338            49999
              Selection Sort Reverse Sorted             50000                2.626613       1249975000
                 Bubble Sort         Sorted             50000                0.000093            49999
                   Heap Sort         Sorted             50000                0.012655          1455438
              Insertion Sort         Sorted             50000                0.000128            49999
                  Merge Sort         Sorted             50000                0.004302           401952
Quick Sort (Median of Three)         Sorted             50000                0.002815           782782
                  Radix Sort         Sorted             50000                0.002775            49999
              Selection Sort         Sorted             50000                2.736064       1249975000
                 Bubble Sort         Random             75000               13.015469       2812406889
                   Heap Sort         Random             75000                0.016775          2200213
              Insertion Sort         Random             75000                3.153109       1407462177
                  Merge Sort         Random             75000                0.012212          1121123
Quick Sort (Median of Three)         Random             75000                0.009933          1378985
                  Radix Sort         Random             75000                0.004007            74999
              Selection Sort         Random             75000                6.038297       2812462500
                 Bubble Sort Reverse Sorted             75000                7.927747       2812462500
                   Heap Sort Reverse Sorted             75000                0.013935          2138650
              Insertion Sort Reverse Sorted             75000                6.306414       2812462500
                  Merge Sort Reverse Sorted             75000                0.005946           594612
Quick Sort (Median of Three) Reverse Sorted             75000                0.006389          2272487
                  Radix Sort Reverse Sorted             75000                0.003386            74999
              Selection Sort Reverse Sorted             75000                5.885482       2812462500
                 Bubble Sort         Sorted             75000                0.000187            74999
                   Heap Sort         Sorted             75000                0.013620          2268087
              Insertion Sort         Sorted             75000                0.000156            74999
                  Merge Sort         Sorted             75000                0.005722           624316
Quick Sort (Median of Three)         Sorted             75000                0.003228          1195642
                  Radix Sort         Sorted             75000                0.003488            74999
              Selection Sort         Sorted             75000                6.125949       2812462500
                 Bubble Sort         Random            100000               22.857072       4999746159
                   Heap Sort         Random            100000                0.023261          3019917
              Insertion Sort         Random            100000                5.465526       2508124174
                  Merge Sort         Random            100000                0.019851          1536545
Quick Sort (Median of Three)         Random            100000                0.010984          1904754
                  Radix Sort         Random            100000                0.006380            99999
              Selection Sort         Random            100000               10.747956       4999950000
                 Bubble Sort Reverse Sorted            100000               14.045717       4999950000
                   Heap Sort Reverse Sorted            100000                0.017061          2926640
              Insertion Sort Reverse Sorted            100000               10.604652       4999950000
                  Merge Sort Reverse Sorted            100000                0.007389           815024
Quick Sort (Median of Three) Reverse Sorted            100000                0.008388          3107283
                  Radix Sort Reverse Sorted            100000                0.004301            99999
              Selection Sort Reverse Sorted            100000               10.573512       4999950000
                 Bubble Sort         Sorted            100000                0.000171            99999
                   Heap Sort         Sorted            100000                0.014340          3112517
              Insertion Sort         Sorted            100000                0.000180            99999
                  Merge Sort         Sorted            100000                0.006181           853904
Quick Sort (Median of Three)         Sorted            100000                0.004786          1665551
                  Radix Sort         Sorted            100000                0.003749            99999
              Selection Sort         Sorted            100000                8.109508       4999950000

Complete results table exported to graphs/csv_data/comprehensive_sorting_performance_results.csv

--- Statistical Correlation Analysis ---
Algorithm                           | Correlation (r) | P-value
----------------------------------------------------------------------
Bubble Sort                         |          0.9665 | 2.7559e-16
Heap Sort                           |          0.9557 | 8.5789e-15
Insertion Sort                      |          0.9994 | 9.6243e-38
Merge Sort                          |          0.9339 | 1.1519e-12
Quick Sort (Median of Three)        |          0.8710 | 3.4554e-09
Radix Sort                          |          0.9550 | 1.0499e-14
Selection Sort                      |          0.9894 | 1.7489e-22

Statistical Interpretation:
  r ≈ 1.0: Strong positive correlation (increased comparisons → increased time)
  r ≈ 0.0: Weak or negligible correlation
  p-value < 0.05: Statistically significant correlation

================================================================================
CRITICAL PERFORMANCE EVALUATION NOTES
================================================================================

⚠️  TIMING MEASUREMENT PROTOCOL:
  - Execution timing measured within C code using clock_gettime(CLOCK_MONOTONIC)
  - This approach eliminates Python subprocess overhead from measurements
  - Results accurately reflect actual algorithmic performance characteristics

⚠️  RADIX SORT COMPARISON METRIC NOTE:
  - Radix sort implements a NON-COMPARATIVE sorting paradigm
  - Algorithm does not perform element-to-element comparisons (unlike other methods)
  - 'Comparisons' metric represents getMax() function operations (~n)
  - This value is NOT directly comparable to other algorithms' comparison counts
  - Utilize TIME metric rather than COMPARISONS for radix sort performance evaluation

✓ EXPECTED ALGORITHMIC BEHAVIOR:
  - O(n²) complexity: Bubble, Insertion, Selection Sort algorithms
  - O(n log n) complexity: Heap, Merge, Quick Sort algorithms
  - O(n+k) complexity: Radix Sort (where k represents key range)
  - Optimized best-case: Bubble & Insertion sort demonstrate O(n) for sorted inputs
================================================================================
                   