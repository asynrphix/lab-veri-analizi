import kagglehub
from kagglehub import KaggleDatasetAdapter

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "edumagalhaes/quality-prediction-in-a-mining-process",
    "MiningProcess_Flotation_Plant_Database.csv",
    pandas_kwargs={"encoding": "latin-1", "sep": ",", "decimal": ","}
)

print("Satır, kolon:", df.shape)
print(df.columns.tolist())
print(df.head())

df.to_csv("ham_veri.csv", index=False)
print("Kaydedildi: ham_veri.csv")