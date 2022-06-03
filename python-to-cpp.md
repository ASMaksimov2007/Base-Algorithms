# Списки

### Массивная реализация

##### Инициализация

```python
s = list()
s = []
s = [69, 228, 1000, 7, 42]
```

```cpp
int s[10];
```

##### Добавление элемента

```python
s.append(element)
```

```cpp
s[i] = element;
```

##### Удаление элемента

```python
s.remove(element)
```

```cpp
// Только костыльная реализация
```

##### Вставка элемента

```python
s.insert(element)
```

```cpp
// Только костыльная реализация
```

##### Обращение по индексу

```python
s[i]
```

```cpp
s[i];
```

##### Получение элемента с удалением

```python
s.pop(i)
s.pop()
```

```cpp
// Только костыльная реализация (см. удаление и обращение по индексу)
```

##### Очистка

```python
s.clear()
s = []
s = list()
```

```cpp
int s[1];
```

##### Сортировка

```python
s.sort()
s = sorted(s)
```

```cpp
#include <algorithm>
std::sort(std::begin(s), std::end(s));

// или

#include <algorithm>
std::sort(s.begin(), s.end());
```

##### Поиск индекса по значению

```python
s.index(element)
```

```cpp
std::distance(arr, std::find(arr, arr + arr_size, element));
```

##### Переворот

```python
s.reverse()
```

```cpp
// Нет стандартной функции или метода
```

### Векторы

##### Инициализация

```python
s = list()
s = []
s = [69, 228, 1000, 7, 42]
```

```cpp
#include <vector>

vector<int> s;
vector<int> s(10);
vector<int> s = {69, 228, 1000, 7, 42};
```

##### Добавление элемента

```python
s.append(element)
```

```cpp
s.push_back(element);
```

##### Удаление элемента

```python
s.remove(element)
```

```cpp
remove(left, right, element)

// используется как

remove(s.begin(), s.end(), element)
```

##### Вставка элемента

```python
s.insert(element)
```

```cpp
// Только костыльная реализация
```

##### Обращение по индексу

```python
s[i]
```

```cpp
s[i];
```

##### Очистка

```python
s.clear()
s = []
s = list()
```

```cpp
int s[1];
```

##### Сортировка

```python
s.sort()
s = sorted(s)
```

```cpp
#include <algorithm>
std::sort(std::begin(s), std::end(s));

// или

#include <algorithm>
std::sort(s.begin(), s.end());
```

##### Поиск индекса по значению

```python
s.index(element)
```

```cpp
std::distance(arr, std::find(arr, arr + arr_size, element));
```

##### Переворот

```python
s.reverse()
```

```cpp
// нет стандартной функции или метода
```
