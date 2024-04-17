import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.2f}'.format
excel_file = 'money.xlsx'
xl = pd.ExcelFile(excel_file)
sheet_name = '202404'
df = xl.parse(sheet_name)
df['交易日期'] = pd.to_datetime(df['交易日期'])

# # 将数据按照日期分组并计算每日消费额
# daily_expenses = df_expenses.groupby(df_expenses['交易日期'].dt.date)['收入/支出金额'].sum()

# # 打印每日消费额
# print("每日消费额：")
# print(daily_expenses)




# 打印结果
# print("日均消费额：", daily_average_expenses)

def perform_exchange(df):
    # 将具有相同名字的流转收入分组并计算总金额
    grouped_incoming = df[df['项目'] == '流转收入'].groupby('具体')['收入/支出金额'].sum()

    # 将总金额添加到对应的流转支出行中
    df_outgoing = df[df['项目'] == '流转支出']
    for specific, amount in grouped_incoming.items():
        df_outgoing.loc[df_outgoing['具体'] == specific, '收入/支出金额'] += amount

    return df_outgoing

def perform_expenses(df):
    df_expenses = df[df['项目'] == '消费']
    return df_expenses


def merge_df():
    df_outgoing = perform_expenses(df)
    df_expenses = perform_exchange(df)
    
    # 合并两个 DataFrame
    merged_df = pd.concat([df_outgoing, df_expenses])

    # 将日期列转换为日期时间格式
    merged_df['交易日期'] = pd.to_datetime(merged_df['交易日期'])

    # 按日期排序
    sorted_df = merged_df.sort_values(by='交易日期')

    return sorted_df


def plot_per_day(daily_expenses, cumsum=False):
    """
    绘制每日消费情况图。可选当日消费或累计消费
    """
    # 缺失日期补零
    all_dates = pd.date_range(start=daily_expenses['交易日期'].min(), end=daily_expenses['交易日期'].max(), freq='D')
    all_dates_df = pd.DataFrame({'交易日期': all_dates})

    # 合并已有数据和包含所有日期的 DataFrame
    merged_df = pd.merge(all_dates_df, daily_expenses, on='交易日期', how='left')

    # 填充缺失值为零
    merged_df['收入/支出金额'].fillna(0, inplace=True)

    merged_df['累计消费'] = merged_df['收入/支出金额'].cumsum()

    plt.figure(figsize=(10, 6))
    if not cumsum:
        plt.plot(merged_df['交易日期'], -1 * merged_df['收入/支出金额'], marker='o', linestyle='-')
    else:
        plt.plot(merged_df['交易日期'], -1 * merged_df['累计消费'], marker='o', linestyle='-')
    plt.title('Daily Expenses')
    plt.xlabel('Date')
    plt.ylabel('Money')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def per_day():
    """
    绘制每日消费情况图。包括当日消费或累计消费
    """
    sorted_df = merge_df()
    daily_expenses = sorted_df.groupby('交易日期')['收入/支出金额'].sum().reset_index()

    plot_per_day(daily_expenses)  # 绘制每日的当日消费图
    plot_per_day(daily_expenses, cumsum=True)  # 绘制每日的累计消费图

    # 打印每日消费额
    print(daily_expenses)

    mean_daily()

    # 如果你想返回每日消费额的列表或 Series，可以使用以下代码：
    return daily_expenses


def mean_daily():
    sorted_df = merge_df()

    # 计算支出金额总和
    total_expenses = sorted_df['收入/支出金额'].sum()

    # 计算天数
    days = (df['交易日期'].max() - df['交易日期'].min()).days + 1

    # 计算日均消费额
    daily_average_expenses = total_expenses / days
    # print(daily_average_expenses)

def cal_balance():
    balance_20240301 = {'工行': 127596.59, '微信': 2.94}
    for count in balance_20240301.keys():
        count_df = df[df['账户']==count] 
        balance = count_df['收入/支出金额'].cumsum() + balance_20240301[count]
        count_df.loc[count_df['账户'] == count, 'balance'] = balance.tolist()
        df_selected = count_df[['交易日期', '收入/支出金额', 'balance']]
        print(df_selected)

        
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(balance)), balance, marker='o', linestyle='-')
        plt.title('Daily Expenses')
        plt.xlabel('Date')
        plt.ylabel('Money')
        plt.grid(True)
        plt.xticks(rotation=45)

        for i, txt in zip(range(len(balance)), balance):
            print(i, txt)
            plt.annotate(f'{txt:.2f}', (i, txt), textcoords="offset points", xytext=(0,10), ha='center')

        plt.tight_layout()
        plt.show()


def cal_daily_transaction():
    balance_20240301 = {'工行': 127569.59, '微信': 2.94}
    for count in balance_20240301.keys():
        daily_transaction = df[df['账户']==count].groupby('交易日期')['收入/支出金额'].sum().reset_index()
        daily_transaction_cumsum = daily_transaction['收入/支出金额'].cumsum() + balance_20240301[count]

        plt.figure(figsize=(10, 6))
        plt.plot(daily_transaction['交易日期'], daily_transaction_cumsum, marker='o', linestyle='-')
        plt.title('Daily Expenses')
        plt.xlabel('Date')
        plt.ylabel('Money')
        plt.grid(True)
        plt.xticks(rotation=45)

        # 添加每个数据点的具体金额
        for i in range(len(daily_transaction)):
            plt.text(daily_transaction['交易日期'][i], daily_transaction_cumsum[i], f'{daily_transaction_cumsum[i]:.2f}', fontsize=8, ha='center', va='bottom')

        plt.tight_layout()
        plt.show()


per_day()