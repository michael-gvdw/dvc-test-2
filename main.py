import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None)
    df.to_csv('./assets/original_dataset/car_eval_raw.csv', index=False, mode='w')

    df.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    df.to_csv('./assets/data/car_eval.csv', index=False, mode='w')



