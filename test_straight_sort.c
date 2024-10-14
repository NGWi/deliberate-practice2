#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../Documents/klib-master/khash.h"

// Declare the hash table at the top-level of the file
KHASH_MAP_INIT_INT(count_map, int);

// Function to perform wise counting sort
void wise_counting_sort(int* arr, int n) {
    // ... (same implementation as before)
}

int main() {
    int n = 1000000;
    int* arr = (int*) malloc(n * sizeof(int));

    FILE* file = fopen("random_array.txt", "r");
    for (int i = 0; i < n; i++) {
        fscanf(file, "%d", &arr[i]);
    }
    fclose(file);

    wise_counting_sort(arr, n);

    free(arr);
    return 0;
}