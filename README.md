# Ответ заданий для получения сертификата [SQL Academy](https://sql-academy.org/ru)

### 1. Вывести имена всех людей, которые есть в базе данных авиакомпаний 
<details>
  <summary>Ответ</summary>

```mysql
select name from Passenger
```

</details>

### 2. Вывести названия всеx авиакомпаний 

<details>
  <summary>Ответ</summary>

```mysql
select name from Company
```

</details>

### 3. Вывести все рейсы, совершенные из Москвы  

<details>
  <summary>Ответ</summary>

```mysql
select * from Trip
where town_from = 'Moscow'
```

</details>

### 4. Вывести имена людей, которые заканчиваются на "man"  

<details>
  <summary>Ответ</summary>

```mysql
select name from passenger
where name like '%man'
```

</details>

### 5. Вывести количество рейсов, совершенных на TU-134

<details>
  <summary>Ответ</summary>

```mysql
select COUNT(*) as count from trip
where plane = 'TU-134'
```

</details>

### 6. Какие компании совершали перелеты на Boeing

<details>
  <summary>Ответ</summary>

```mysql
select DISTINCT name from Company
join Trip ON Company.id = Trip.company
where plane = 'Boeing'
```

</details>

### 7. Вывести все названия самолётов, на которых можно улететь в Москву (Moscow)
  

<details>
  <summary>Ответ</summary>

```mysql
select DISTINCT plane from trip
where town_to = 'Moscow';
```

</details>

