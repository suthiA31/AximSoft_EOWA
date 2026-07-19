

def get_dashboard_kpis(df, comparison):

    total_records = len(df)

    total_features = df.shape[1] - 1

    best_model = comparison.iloc[0]["Model"]

    r2_score = round(comparison.iloc[0]["R2 Score"],3)

    rmse = round(comparison.iloc[0]["RMSE"],2)

    mae = round(comparison.iloc[0]["MAE"],2)

    return {

        "records": total_records,

        "features": total_features,

        "best_model": best_model,

        "r2": r2_score,

        "rmse": rmse,

        "mae": mae

    }