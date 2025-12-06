import pandas as pd


def prep_df(path):
    input_df = pd.read_csv(path, header=None)
    transposed_df = input_df.transpose()
    col_names = []
    for col_num in range(1, len(transposed_df.columns)):
        col_names.append(f'num_{col_num}')
    col_names.append('operator')
    
    transposed_df.columns = col_names

    for col_num in range(1, len(transposed_df.columns)):    
        transposed_df[f'num_{col_num}'] = transposed_df[f'num_{col_num}'].astype(int)
    return transposed_df


def get_grand_total(df):
    cols = df.columns[:-1]

    df['result'] = df.apply(
    lambda row: (
        sum(row[cols]) if row['operator'] == '+'
        else eval('*'.join(map(str, row[cols])))  # Safely compute product
    ),
    axis=1
)
    return df['result'].sum()


if __name__ == "__main__":

    test_df = prep_df('/Users/tim/Downloads/aoc2025/d6_test.csv')
    problem_df = prep_df('/Users/tim/Downloads/aoc2025/d6_input.csv')

    test_answer = 4277556

    print(test_df.head())
    test_result = get_grand_total(test_df)
    print(test_result, test_answer, test_result == test_answer)

    problem_result = get_grand_total(problem_df)
    print(problem_result)



