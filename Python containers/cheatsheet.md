### List

###### Initialisation

`a = list()` same as `a = []`


###### Appending/inserting

`a.insert(index, value)` same as `a[index:index] = value`

`a.append(value)` same as `a += [value]`

`a.extend(list)` same as `a += list`

`a *= n`

###### Deletion

`a.remove(value)`

`a.pop(index)`

`a.pop()`

`del a[start:end:step]`

`a.clear()`

###### Changing

`a[index] = value`

`a[start:end:step] = value`


###### Getting

`value = a[index]`

`value = a.pop()`

`value = a.pop(index)`


###### Miscellaneous

`a.sort()` same as `a = sorted(a)`

`a.copy()` same as `a[:]`

`a.reverse()` same as `a = a[::-1]`

`len(a)`


### Set

###### Initialisation

`a = set()`

###### Adding

`a.add(value)`

###### Deletion

`a.remove(value)` - raises `KeyError` if the item is not present

`a.discard(value)` - deletes the item if it is present

`a.pop()`

`a.clear()`

###### Changing

Sets do not support indexing and assignment.

###### Getting

`value = a.pop()`

###### Miscellaneous



`a.copy()`






### Dict




### Tuple





### Frozenset





### Deque
