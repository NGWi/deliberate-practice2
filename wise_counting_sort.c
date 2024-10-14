#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <khash.h>

// Function to perform wise counting sort
void wise_counting_sort(int* arr, int n) {
    // Create a hash table to store the count of each integer
    KHASH_MAP_INIT_INT(count_map, int);
    khint_t k;
    int i, min_val, max_val;

    // Initialize the hash table
    khash_t(count_map) *hash = kh_init(count_map);

    // Find the minimum and maximum values in the array
    min_val = max_val = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] < min_val) {
            min_val = arr[i];
        }
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }

    // Count the occurrences of each integer
    for (i = 0; i < n; i++) {
        k = kh_put(count_map, hash, arr[i], &ret_val);
        if (k == kh_end(hash)) {
            // If the key is not present, add it to the hash table
            kh_value(hash, k) = 1;
        } else {
            // If the key is already present, increment its count
            kh_value(hash, k)++;
        }
    }

    // Create a new array to store the sorted elements
    int* sorted_arr = (int*) malloc(n * sizeof(int));

    // Initialize an index to keep track of the current position in the sorted array
    int idx = 0;

    // Populate the sorted array using the counts from the hash table
    for (k = kh_begin(hash); k != kh_end(hash); k++) {
        if (kh_exist(hash, k)) {
            int key = kh_key(hash, k);
            int count = kh_value(hash, k);
            for (i = 0; i < count; i++) {
                sorted_arr[idx++] = key;
            }
        }
    }

    // Print the sorted array
    for (i = 0; i < n; i++) {
        printf("%d ", sorted_arr[i]);
    }
    printf("\n");

    // Free the memory allocated for the hash table and the sorted array
    kh_destroy(count_map, hash);
    free(sorted_arr);
}

int main() {
    int arr[] = {4, 2, 2, -8, 3, 3, -1};
    int n = sizeof(arr) / sizeof(arr[0]);
    wise_counting_sort(arr, n);
    return 0;
}