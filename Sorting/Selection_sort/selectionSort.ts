function partition(arr: number[], low: number, high: number): number {
    let pivot = arr[high];
    let i = low - 1;

    for (let j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            
            // swap here
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    // swap here
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];

    return (i + 1);
}

function quickSort(arr: number[], low, high): void {
    if (low < high) {
        let pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

let arr = [-1238, 0, -123, 1293, 555, -999, 10];
console.log('before:', arr.join(' '));
quickSort(arr, 0, arr.length - 1);
console.log('after:', arr.join(' '));