Надежные сведения можно украсть с сайта 179 школы:

https://server.179.ru/tasks/cpp/total/

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
s.insert(index, element)
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
s.insert(index, element)
```

```cpp
s.insert(index, element);

// index - указатель на элемент, в который нужно произвести вставку

s.insert(s.begin() + index, element)
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
s = {};
s.clear();
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
s.find(s.begin(), s.end(), element) - s.begin();
```

##### Переворот

```python
s.reverse()
```

```cpp
std::reverse(s.begin(), s.end());
```


# Множества за O(log n) с упорядоченными элементами

*Заметка: в Python множества работают на хеш-таблицах и за O(1).*

##### Инициализация

```python
s = set()
```

```cpp
#include <set>
set<int> s;
```

##### Добавление элемента

```python
s.add(element)
```

```cpp
s.insert(element);
```

##### Удаление элемента

```python
s.remove(element)
```

```cpp
s.erase(element);

// либо по индексу через итератор

s.erase(s.begin() + index);
```

##### Проверка нахождения элемента

```python
element in s
```

```cpp
s.count(element) == 1;

// или через find();

s.find(element) != s.end();
```

##### Операции на множествах

```python
a | b

a & b

a - b
```

```cpp
set<int> intersect;
set_intersection(a.begin(), a.end(), b.begin(), b.end(), intersect.begin());

set<int> union_set;
set_union(a.begin(), a.end(), b.begin(), b.end(), union_set.begin());

set<int> difference;
set_difference(a.begin(), a.end(), b.begin(), b.end(), difference.begin());
```

##### Очистка

```python
s.clear()
s = set()
```

```cpp
s.clear();
```



# Множества за O(1) с неупорядоченными элементами

##### Инициализация

```python
s = set()
```

```cpp
#include <set>
unordered_set<int> s;
```

##### Добавление элемента

```python
s.add(element)
```

```cpp
s.insert(element);
```

##### Удаление элемента

```python
s.remove(element)
```

```cpp
s.erase(element);
```

##### Проверка нахождения элемента

```python
element in s
```

```cpp
s.count(element) == 1;

// или через find();

s.find(element) != s.end();
```

##### Операции на множествах

```python
a | b

a & b

a - b
```

```cpp
unordered_set<int> intersect;
set_intersection(a.begin(), a.end(), b.begin(), b.end(), intersect.begin());

unordered_set<int> union_set;
set_union(a.begin(), a.end(), b.begin(), b.end(), union_set.begin());

unordered_set<int> difference;
set_difference(a.begin(), a.end(), b.begin(), b.end(), difference.begin());
```

##### Очистка

```python
s.clear()
s = set()
```

```cpp
s.clear();
```


# Словарь (хеш-таблица) за O(1) c неупорядоченными элементами

### Инициализация

```python
s = {}
s = dict()
```

```cpp
#include <unordered_map>
unordered_map<string, int> s;
```

### Вставка элементов

```python
s[key] = value
```

```cpp
s.insert(make_pair(key, value))

// но можно просто присвоить значение
```

### Удаление элементов

```python
del s[key]
```

```cpp
s.erase(s.find(key));
```

### Присвоение элементов

```python
s[key] = value
```

```cpp
s[key] = value;
```

### Обращение к элементам

```python
a = s[key]
```

```cpp
a = s[key];
```

### Проверка на принадлежность элемента

```python
key in s
```

```cpp
s.find(key) != s.end();
```

### Итерирование

```python
for key, value in s.items():
    pass
```

```cpp
unordered_map<string, int>::iterator it;
for (it = s.begin(); it != s.end(); it++) {
  key = *it.first;
  value = *it.second;
}

// или

for (auto p: s) {
  key = p.first;
  value = p.second;
}

// p - pair на key и value, it - указатель на них
```

### Очистка

```python
s = {}
s = dict()
```

```cpp
s.clear();
```

# Словарь (дерево) за O(log n) c упорядоченными элементами

*Код на Python приведен для справки, так как работает с другой асимптотикой*

### Инициализация

```python
s = {}
s = dict()
```

```cpp
#include <map>
map<string, int> s;
```

### Вставка элементов

```python
s[key] = value
```

```cpp
s.insert(make_pair(key, value))

// но можно просто присвоить значение
```

### Удаление элементов

```python
del s[key]
```

```cpp
s.erase(s.find(key));
```

### Присвоение элементов

```python
s[key] = value
```

```cpp
s[key] = value;
```

### Обращение к элементам

```python
a = s[key]
```

```cpp
a = s[key];
```

### Проверка на принадлежность элемента

```python
key in s
```

```cpp
s.find(key) != s.end();
```

### Итерирование

```python
for key, value in s.items():
    pass
```

```cpp
map<string, int>::iterator it;
for (it = s.begin(); it != s.end(); it++) {
  key = *it.first;
  value = *it.second;
}

// или

for (auto p: s) {
  key = p.first;
  value = p.second;
}

// p - pair на key и value, it - указатель на них
```

### Очистка

```python
s = {}
s = dict()
```

```cpp
s.clear();
```

# Строки

### Инициализация

```python
s = ""
```

```cpp
#include <string>

string s;
```

### Конкатенация

```python
s = a + b
```

```cpp
s = a + b;
```

### Строка в вектор char

```python
s = list(s)
```

```cpp
vector<char> v(s.begin(), s.end());
```

### Вектор char в строку

```python
s = "".join(v)
```

```cpp
string s(v.begin(), v.end());
```

### Обращение к элементам

```python
s[index]
```

```cpp
s[index];
```

### Добавление в конец

```python
s += element
```

```cpp
s.push_back(element);
```

### Подстрока

```python
s[start:start + length]
```

```cpp
s.substr(start, length);
```

### Длина

```python
len(s)
```

```cpp
s.size();
```

### Очистка

```python
s = ""
s = str()
```

```cpp
s.clear();
```

Подробнее о строках: https://server.179.ru/tasks/cpp/total/161.html
