import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load pretrained sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# IoT-related reference phrases
iot_phrases = [
    "Connects with a smartwatch",
    "Syncs with wearable devices",
    "Bluetooth connection to fitness tracker",
    "Reads data from heart rate sensors",
    "Pairs with health bands or smart scales",
    "Collects data from smart IoT devices",
    "Compatible with IoT-enabled devices",
    "Google Fit",
    "Wear OS"
]

# Encode reference IoT phrases
iot_embeddings = model.encode(iot_phrases, convert_to_tensor=True)

def check_iot_connection(app_id, description=None):
    try:
        # Compute embedding and similarity
        desc_embedding = model.encode(description, convert_to_tensor=True)
        similarity = util.cos_sim(desc_embedding, iot_embeddings)
        max_score = similarity.max().item()
        return "Yes" if max_score >= 0.90 else "No"
    except Exception as e:
        return f"Error: {str(e)}"

# === Load CSV and process ===

def process_csv(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)

    if 'app_id' not in df.columns:
        raise ValueError("CSV must contain an 'app_id' column.")

    # Add IoT detection results
    df['iot_connected'] = df.apply(
        lambda row: check_iot_connection(row['app_id'], row.get('description')), axis=1
    )

    df.to_csv(output_csv_path, index=False)
    print(f"Results saved to {output_csv_path}")

# === Example usage ===
# process_csv("apps.csv", "apps_with_iot_results.csv")

'''
#===CSV Format suggested===#
app_id,description
com.fitbit.FitbitMobile,
com.whatsapp,Instant messaging app with voice and video calling.
'''
