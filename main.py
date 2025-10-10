# Домашнее задание
# 1. Вам представлен код с реализацией алгоритма Нидлмана-Вунша. Функция needleman_wunsch принимает параметры: match=2, mismatch=-1, gap=-1
# поэксперементируйте с параметрами и посморите, как меняется выравнивание и score. Какие выводы можно сделать? 
#!/usr/bin/env python3
"""
Алгоритма Нидлмана-Вунша.
"""

import time
import os


def clear_screen():
    """Очищает экран"""
    os.system('clear' if os.name == 'posix' else 'cls')


def print_matrix(seq1, seq2, dp, current_i=None, current_j=None, step_info=""):
    """
    Печатает матрицу с анимацией текущей ячейки
    """
    clear_screen()
    
    print("=" * 70)
    print("АЛГОРИТМ НИДЛМАНА-ВУНША - ПОШАГОВОЕ ЗАПОЛНЕНИЕ")
    print("=" * 70)
    print(f"Seq1: {seq1}")
    print(f"Seq2: {seq2}")
    if step_info:
        print(f"Шаг: {step_info}")
    print()
    
    # Заголовок
    print("     ", end="")
    for j in range(len(dp[0])):
        if j == 0:
            print("   ", end="")
        else:
            print(f"  {seq2[j-1]}", end="")
    print()
    
    # Строки матрицы
    for i in range(len(dp)):
        if i == 0:
            print("   ", end="")
        else:
            print(f" {seq1[i-1]} ", end="")
        
        for j in range(len(dp[0])):
            # Выделяем текущую ячейку
            if current_i == i and current_j == j:
                print(f"[{dp[i][j]:2}]", end="")
            else:
                print(f" {dp[i][j]:2} ", end="")
        print()
    
    print("=" * 70)


def needleman_wunsch(seq1, seq2, match=2, mismatch=-1, gap=-1):
    """
    Алгоритма Нидлмана-Вунша
    """
    n, m = len(seq1), len(seq2)
    

    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i * gap
    for j in range(m+1):
        dp[0][j] = j * gap
    
    print_matrix(seq1, seq2, dp, step_info="Инициализация")
    time.sleep(2)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            print_matrix(seq1, seq2, dp, current_i=i, current_j=j, 
                                step_info=f"Заполнение ячейки ({i},{j})")
            
            match_score = dp[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete = dp[i-1][j] + gap
            insert = dp[i][j-1] + gap
            
            print(f"\nРасчет для {seq1[i-1]} vs {seq2[j-1]}:")
            print(f"↖ Совпадение: {dp[i-1][j-1]} + {match if seq1[i-1] == seq2[j-1] else '-1'} = {match_score}")
            print(f"↑ Удаление:   {dp[i-1][j]} + {gap} = {delete}")
            print(f"← Вставка:    {dp[i][j-1]} + {gap} = {insert}")
            
            dp[i][j] = max(match_score, delete, insert)
            
            print(f"Максимум: {dp[i][j]}")
            time.sleep(1.5)
    
    print_matrix(seq1, seq2, dp, step_info="Матрица заполнена")
    time.sleep(2)
    
    align1, align2 = "", ""
    i, j = n, m
    
    print("\nОБРАТНЫЙ ПРОХОД:")
    print("=" * 50)
    
    step = 1
    while i > 0 or j > 0:
        print(f"\nШаг {step}: Позиция ({i},{j})")
        
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            print(f"  ↖ Совпадение: {seq1[i-1]} = {seq2[j-1]}")
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + gap:
            print(f"  ↑ Удаление: {seq1[i-1]} → -")
            align1 = seq1[i-1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            print(f"  ← Вставка: - ← {seq2[j-1]}")
            align1 = "-" + align1
            align2 = seq2[j-1] + align2
            j -= 1
        
        print(f"  Выравнивание: {align1}")
        print(f"                {align2}")
        
        step += 1
        time.sleep(1)
    
    return align1, align2, dp


def main():
    """
    Демонстрация алгоритма
    """
    # Ваши последовательности
    seq1 = "GCATGCG"
    seq2 = "GATTACA"
    
    print("АЛГОРИТМ НИДЛМАНА-ВУНША")
    print("=" * 70)
    print(f"Последовательность 1: {seq1}")
    print(f"Последовательность 2: {seq2}")
    print("Параметры: match=2, mismatch=-1, gap=-1")
    print()
    
    result1, result2, matrix = needleman_wunsch(seq1, seq2)
    
    print("\n" + "=" * 70)
    print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
    print("=" * 70)
    print(f"Выравнивание 1: {result1}")
    print(f"Выравнивание 2: {result2}")
    print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")


if __name__ == "__main__":
    main()


"""
Демонстрация алгоритма
    """
# Ваши последовательности
seq1 = "GCATGCG"
seq2 = "GATTACA"
    
print("АЛГОРИТМ НИДЛМАНА-ВУНША")
print("=" * 70)
print(f"Последовательность 1: {seq1}")
print(f"Последовательность 2: {seq2}")
print("Параметры: match=-2, mismatch=-1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=-2, mismatch=-1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
Начнем с замены match
print("Параметры: match=-1, mismatch=-1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=-1, mismatch=-1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=0, mismatch=-1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=0, mismatch=-1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=1, mismatch=-1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=-1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=-1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
#Теперь заменим mismatch
print("Параметры: match=2, mismatch=-2, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=-2, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=-3, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=-3, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=0, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=0, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=1, gap=-1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=1, gap=-1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
#Теперь изменяем gap
print("Параметры: match=2, mismatch=1, gap=-2")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=1, gap=-2)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=1, gap=-3")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=1, gap=-3)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=1, gap=0")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=1, gap=0)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
print("Параметры: match=2, mismatch=1, gap=1")
print()
    
result1, result2, matrix = needleman_wunsch(seq1, seq2, match=2, mismatch=1, gap=1)
    
print("\n" + "=" * 70)
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
print("=" * 70)
print(f"Выравнивание 1: {result1}")
print(f"Выравнивание 2: {result2}")
print(f"Общий score: {matrix[len(seq1)][len(seq2)]}")
Выводы:
#Высокий штраф за gap: алгоритм избегает пропусков

#Низкий/отрицательный mismatch: алгоритм предпочитает пропуски несовпадениям

#Положительный gap: алгоритм активно использует пропуски для увеличения score
# 2. Используя numpy создайте матрицу 7 на 7
import numpy as np
matrix = np.zeros((7, 7))
print(matrix)
# 3. NumPy: создайтие диагональную матрицу, где по главной диагонали идут числа от 1 до 5
values = [1, 2, 3, 4, 5]
matrix = np.diag(values)
print(matrix)
# 4. Напиши функцию, которая принимает матрицу и проверяет, является ли она единичной. В ответе возвращается True или False
def is_matrix_ones(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i, j] != 1:
                    return False
            else:
                if matrix[i, j] != 0:
                    return False
    return True
is_matrix_ones(matrix)