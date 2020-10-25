function bubbleSort(list: number[]): void {
    let listLength = list.length;

    function swap(indexA: number, indexB: number): void {
        let temp = list[indexA];
        list[indexA] = list[indexB];
        list[indexB] = temp;
    }

    let swapped;
    do {
        swapped = false;
        for (let i = 1; i <= listLength - 1; i++) {
            if (list[i - 1] > list[i]) {
                swap(i - 1, i);
                swapped = true;
            }
        }
    } while(swapped);
}

const list = [10, -11, 31, 15, -3, 3, 0, 1];
console.log('list pre-sort:', list);
bubbleSort(list);
console.log('after sort:', list);