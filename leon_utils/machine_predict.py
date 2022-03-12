# 导入类库和加载数据集
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# 模型建立
def RF(X_train, X_test, y_train, y_test):  # 随机森林
    model = RandomForestRegressor(n_estimators=200, max_features=None)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    return predicted


def get_train_pre(root_train,root_test):
    train_x, train_y = get_data(root_train)
    pre_x, pre_y = get_data(root_test)
    #先将数据集分成训练集和测试集
    X_train,X_test,y_train,y_test = train_test_split(train_x, train_y, test_size=0.2, random_state=21)
    _, X_test, _, _ = train_test_split(pre_x, pre_y, test_size=1, random_state=21)
    # print(X_test)
    a = RF(X_train, X_test, y_train, y_test)
    # print('pr: ',a)
    return a

def get_data(root):
    #读取数据   whe ,temp_high ,temp_low ,change ,wind_idr ,wind_power
    train_names = ["Weather","Tmp_Max","Tmp_Min",'Wind_Change','Wind_Dir','Wind_Power','Time_Dis','Person_Num','Car_Num','Passer_Num']
    data = pd.read_csv(root,names=train_names)
    data.head()
    # 数据处理
    Weather_= []
    Tmp_Max_= []
    Tmp_Min_= []
    Wind_Change_= []
    Wind_Dir_= []
    Wind_Power_= []
    Time_Dis_ = []
    Person_Num_= []
    Car_Num_= []
    Passer_Num_ = []
    i = 0
    last_ = len(data[["Weather"]])-1
    for [Weather,Tmp_Max,Tmp_Min,Wind_Change,Wind_Dir,Wind_Power,Time_Dis,Person_Num,Car_Num,Passer_Num] \
            in data[["Weather","Tmp_Max","Tmp_Min",'Wind_Change','Wind_Dir','Wind_Power','Time_Dis','Person_Num','Car_Num','Passer_Num']].values:
        # print(Weather) 230.45

        if i ==0 :
            Weather_old = Weather
            Tmp_Max_old = Tmp_Max
            Tmp_Min_old = Tmp_Min
            Wind_Change_old = Wind_Change
            Wind_Dir_old = Wind_Dir
            Wind_Power_old = Wind_Power
            Time_Dis_old = Time_Dis
            Person_Num_old = Person_Num
            Car_Num_old = Car_Num
            pass
        elif i == last_:
            pass
        else:
            Weather_.append(Weather_old)
            Tmp_Max_.append(Tmp_Max_old)
            Tmp_Min_.append(Tmp_Min_old)
            Wind_Change_.append(Wind_Change_old)
            Wind_Dir_.append(Wind_Dir_old)
            Wind_Power_.append(Wind_Power_old)
            Time_Dis_.append(Time_Dis_old)
            Person_Num_.append(Person_Num_old)
            Car_Num_.append(Car_Num_old)
            Passer_Num_.append(Passer_Num)

            Weather_old = Weather
            Tmp_Max_old = Tmp_Max
            Tmp_Min_old = Tmp_Min
            Wind_Change_old = Wind_Change
            Wind_Dir_old = Wind_Dir
            Wind_Power_old = Wind_Power
            Time_Dis_old = Time_Dis
            Person_Num_old = Person_Num
            Car_Num_old = Car_Num
        i+=1



    data['Weather']=pd.DataFrame({'Weather':Weather_})
    data['Tmp_Max']=pd.DataFrame({'Tmp_Max':Tmp_Max_})
    data['Tmp_Min']=pd.DataFrame({'Tmp_Min':Tmp_Min_})
    data['Wind_Change']=pd.DataFrame({'Tmp_Distance':Wind_Change_})
    data['Wind_Dir']=pd.DataFrame({'Wind_Dir':Wind_Dir_})
    data['Wind_Power']=pd.DataFrame({'Wind_Power':Wind_Power_})
    data['Time_Dis']=pd.DataFrame({'Time_Dis':Time_Dis_})
    data['Person_Num']=pd.DataFrame({'Person_Num':Person_Num_})
    data['Car_Num']=pd.DataFrame({'Car_Num':Car_Num_})
    data['Passer_Num'] = pd.DataFrame({'Passer_Num': Passer_Num_})

    data = (data[:last_-1])
    data.head()
    #特征缩放
    data = data.astype('float')
    x = data.drop(["Weather","Tmp_Max","Tmp_Min",'Wind_Change','Wind_Dir','Wind_Power','Time_Dis','Person_Num','Car_Num'],axis=1)
    y = data['Passer_Num']
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    newX= scaler.fit_transform(x)
    newX = pd.DataFrame(newX, columns=x.columns)
    return newX, y



# get_train_pre('train.csv','pre.csv')
