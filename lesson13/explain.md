# analyze_scores 函式詳細程式碼解釋

```python
def analyze_scores(students: list[dict]):
    '''
    分析全班成績，輸出全班平均、最高分學生、最低分學生。
    '''
    averages = []
    for student in students:
        scores = [student[subject] for subject in ["國文", "英文", "數學"]]
        avg = sum(scores) / len(scores)
        averages.append({"name": student["姓名"], "avg": avg})
    if not averages:
        print("無學生資料可分析。")
        return
    class_avg = sum([item["avg"] for item in averages]) / len(averages)
    max_student = max(averages, key=lambda x: x["avg"])
    min_student = min(averages, key=lambda x: x["avg"])
    print("\n成績分析:")
    print(f"- 全班平均成績:{class_avg:.1f}分")
    print(f"- 最高分學生: {max_student['name']}({max_student['avg']:.1f}分)")
    print(f"- 最低分學生: {min_student['name']}({min_student['avg']:.1f}分)")
```

## 逐行詳細說明

1. `def analyze_scores(students: list[dict]):`
   - 定義一個名為 analyze_scores 的函式，參數 students 是一個學生字典的列表，每個字典包含姓名與三科分數。

2. `averages = []`
   - 建立一個空清單 averages，用來儲存每位學生的姓名與平均分數。

3. `for student in students:`
   - 逐一處理 students 清單中的每一位學生。

4. `scores = [student[subject] for subject in ["國文", "英文", "數學"]]`
   - 用 list comprehension 依序取出該學生的國文、英文、數學分數，組成一個分數清單 scores。

5. `avg = sum(scores) / len(scores)`
   - 計算該學生三科分數的平均值。

6. `averages.append({"name": student["姓名"], "avg": avg})`
   - 將學生姓名與平均分數組成字典，加入 averages 清單。

7. `if not averages:`
   - 檢查 averages 是否為空，若無學生資料則執行下一步。

8. `print("無學生資料可分析。")`
   - 若無資料，印出提示訊息。

9. `return`
   - 結束函式執行。

10. `class_avg = sum([item["avg"] for item in averages]) / len(averages)`
    - 將所有學生的平均分數加總後除以人數，得到全班平均分數。

11. `max_student = max(averages, key=lambda x: x["avg"])`
    - 用 max 函式找出 averages 中平均分數最高的學生。

12. `min_student = min(averages, key=lambda x: x["avg"])`
    - 用 min 函式找出 averages 中平均分數最低的學生。

13. `print("\n成績分析:")`
    - 印出「成績分析」標題。

14. `print(f"- 全班平均成績:{class_avg:.1f}分")`
    - 印出全班平均分數，取到小數點一位。

15. `print(f"- 最高分學生: {max_student['name']}({max_student['avg']:.1f}分)")`
    - 印出最高分學生的姓名與平均分數。

16. `print(f"- 最低分學生: {min_student['name']}({min_student['avg']:.1f}分)")`
    - 印出最低分學生的姓名與平均分數。

---

### 補充說明：
- 此函式會自動處理學生數量為 0 的情況，避免除以 0 或出現錯誤。
- 若有多位學生平均分數相同，max/min 只會回傳第一個出現者。
- 輸出格式與「新增.md」需求一致，方便老師或學生快速掌握全班成績分布。
