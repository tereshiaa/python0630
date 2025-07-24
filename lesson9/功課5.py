'''
def get_status(prompt, min, max):
    
    value = float(input(prompt))
    if not (min <= value <= max):
        print(f'輸入錯誤，應在範圍 {min} 到 {max}')
            
        
 
       

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def get_bmi(bmi):
    if bmi < 18.5:
        return '體重過輕'
    elif bmi < 24:
        return '正常範圍'
    elif bmi < 27:
        return '體重過重'
    elif bmi < 30:
        return '輕度肥胖'
    elif bmi < 35:
        return '中度肥胖'
    else:
        return '重度肥胖'

def main():
    try:
        height = get_status('請輸入身高（120-250cm）:', 120, 250)
        weight = get_status('請輸入體重（30-200kg）:', 30, 200)

        if height is not None and weight is not None:
            bmi = calculate_bmi(height, weight)
            print('你的BMI為:', round(bmi, 1))
            print('您的BMI為', get_bmi(bmi))
    except ValueError:
        print('格式錯誤')
    except Exception as e:
        print(f'e')
    
    print('應用程式結束')

# 執行主程式
main()
'''



def get_bmi(height, weight):
    # 計算 BMI 並返回
    if 120 <= height <= 250 and 30 <= weight <= 200:
        BMI = weight / ((height / 100) ** 2)
        print('你的 BMI 為:', round(BMI, 1))
        return BMI
    else:
        print('身高或體重範圍錯誤')
        return 

def get_status(BMI):
    if BMI is not None:
        if BMI < 18.5:
            x = '體重過輕'
        elif 18.5 <= BMI < 24:
            x = '正常範圍'
        elif 24 <= BMI < 27:
            x = '體重過重'
        elif 27 <= BMI < 30:
            x = '輕度肥胖'
        elif 30 <= BMI < 35:
            x = '中度肥胖'
        else:
            x = '重度肥胖'
        print('您的 BMI 狀態為:', x)
    

def main():
    try:
        height = float(input('請輸入身高 120-250 cm:'))
        if not (120 <= height <= 250):
            print('身高範圍輸入錯誤')
            return
        weight = float(input('請輸入體重 30-200 kg:'))
        if not (30 <= weight <= 200):
            print('體重範圍輸入錯誤')
            return       
        BMI = get_bmi(height, weight)  # 呼叫 get_bmi 計算 BMI
        get_status(BMI)  # 呼叫 get_status 顯示 BMI 狀態

    except ValueError:
        print('輸入格式錯誤，請輸入數字')
    finally:
        print('應用程式結束')

if __name__ == "__main__":   #主執行檔
    main()