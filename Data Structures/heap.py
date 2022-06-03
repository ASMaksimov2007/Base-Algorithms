def get_from_set(s):
    element = s.pop()
    s.add(element)
    return element


class Heap:
    def __init__(self, start, heap_type):
        if heap_type in ("min", "max"):
            self._type = heap_type
        else:
            raise ValueError(f"unknown heap type: {heap_type}")
        self._indices = dict()
        self._heapify(start)

    def _get_parent_index(self, i):
        if i == 0:
            return -1
        if i % 2 == 0:
            return (i - 2) // 2
        else:
            return (i - 1) // 2

    def _heapify(self, initial):
        self._heap = []

        for i in range(len(initial)):
            child_index = i
            parent_index = self._get_parent_index(child_index)
            self._heap.append(initial[i])
            if self._type == "min":
                while parent_index != -1:
                    if self._heap[child_index] < self._heap[parent_index]:
                        self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
                    child_index = parent_index
                    parent_index = self._get_parent_index(parent_index)
            else:
                while parent_index != -1:
                    if self._heap[child_index] > self._heap[parent_index]:
                        self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
                    child_index = parent_index
                    parent_index = self._get_parent_index(parent_index)

        for index, element in enumerate(self._heap):
            self._indices[element] = self._indices.get(
                element, set()) | set((index,))

    def __repr__(self):
        return f"{self._heap}"

    def __len__(self):
        return len(self._heap)

    def __getitem__(self, index):
        return self._heap[index]

    def __setitem__(self, index):
        raise TypeError("heap does not support item assignment")

    def add(self, item):
        self._heap.append(item)
        self._indices[item] = self._indices.get(
            item, set()) | set((len(self._heap) - 1,))
        child_index = len(self._heap) - 1

        if self._type == "min":
            parent_index = self._get_parent_index(child_index)
            while parent_index != -1:
                if self._heap[child_index] < self._heap[parent_index]:
                    self._indices[self._heap[child_index]].remove(child_index)
                    self._indices[self._heap[parent_index]].remove(
                        parent_index)
                    self._indices[self._heap[parent_index]].add(child_index)
                    self._indices[self._heap[child_index]].add(parent_index)
                    self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
                child_index = parent_index
                parent_index = self._get_parent_index(parent_index)
        else:
            parent_index = self._get_parent_index(child_index)
            while parent_index != -1:
                if self._heap[child_index] > self._heap[parent_index]:
                    self._indices[self._heap[child_index]].remove(child_index)
                    self._indices[self._heap[parent_index]].remove(
                        parent_index)
                    self._indices[self._heap[parent_index]].add(child_index)
                    self._indices[self._heap[child_index]].add(parent_index)
                    self._heap[child_index], self._heap[parent_index] = self._heap[parent_index], self._heap[child_index]
                child_index = parent_index
                parent_index = self._get_parent_index(parent_index)

    def __min__(self):
        if self._type == "min":
            return self._heap[0]
        else:
            return min(self._heap)

    def __max__(self):
        if self._type == "max":
            return self._heap[0]
        else:
            return max(self._heap)

    def _remove_index(self, index):
        if index >= len(self._heap):
            raise IndexError("heap index out of range")

        li_index = len(self._heap) - 1

        self._indices[self._heap[li_index]].remove(li_index)
        if index != li_index:
            self._indices[self._heap[index]].remove(index)
            self._indices[self._heap[li_index]].add(index)

        self._heap[-1], self._heap[index] = self._heap[index], self._heap[-1]

        if self._indices[self._heap[li_index]] == set():
            del self._indices[self._heap[li_index]]

        self._heap.pop()
        cur_index = 0
        if self._type == "min":
            while cur_index * 2 + 1 < len(self._heap):
                if cur_index * 2 + 2 < len(self._heap):
                    index_to_swap = min(
                        cur_index * 2 + 1, cur_index * 2 + 2, key=lambda x: self._heap[x])
                else:
                    index_to_swap = cur_index * 2 + 1
                if self._heap[cur_index] > self._heap[index_to_swap]:
                    self._indices[self._heap[cur_index]].remove(cur_index)
                    self._indices[self._heap[index_to_swap]].remove(
                        index_to_swap)
                    self._indices[self._heap[index_to_swap]].add(cur_index)
                    self._indices[self._heap[cur_index]].add(index_to_swap)
                    self._heap[cur_index], self._heap[index_to_swap] = self._heap[index_to_swap], self._heap[cur_index]
                cur_index = index_to_swap
        else:
            while cur_index * 2 + 1 < len(self._heap):
                if cur_index * 2 + 2 < len(self._heap):
                    index_to_swap = max(
                        cur_index * 2 + 1, cur_index * 2 + 2, key=lambda x: self._heap[x])
                else:
                    index_to_swap = cur_index * 2 + 1
                if self._heap[cur_index] < self._heap[index_to_swap]:
                    self._indices[self._heap[cur_index]].remove(cur_index)
                    self._indices[self._heap[index_to_swap]].remove(
                        index_to_swap)
                    self._indices[self._heap[index_to_swap]].add(cur_index)
                    self._indices[self._heap[cur_index]].add(index_to_swap)
                    self._heap[cur_index], self._heap[index_to_swap] = self._heap[index_to_swap], self._heap[cur_index]
                cur_index = index_to_swap

    def remove(self, item):
        if item in self._indices and self._indices[item]:
            self._remove_index(get_from_set(self._indices[item]))

    def pop(self):
        element = self._heap[0]
        self._remove_index(0)
        return element
