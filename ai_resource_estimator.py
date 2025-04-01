
def estimate_ai_impact(model_type: str, input_size_mb: float, task_duration_sec: float):
    """
    Estimate energy (kWh) and CO2 emissions (grams) based on AI task parameters.
    
    Args:
        model_type (str): Type of AI model (e.g., 'diffusion', 'LLM')
        input_size_mb (float): Size of the input in megabytes
        task_duration_sec (float): Estimated GPU compute time in seconds

    Returns:
        dict: Dictionary with estimated energy and CO2 output
    """
    # Base assumptions (adjustable)
    energy_per_second_kwh = 0.00042  # e.g., A100 GPU ~300W = 0.00042 kWh/sec
    co2_per_kwh_grams = 417  # global average ~0.417 kg CO2 per kWh

    estimated_energy = task_duration_sec * energy_per_second_kwh
    estimated_co2 = estimated_energy * co2_per_kwh_grams

    return {
        "model": model_type,
        "input_size_mb": input_size_mb,
        "duration_sec": task_duration_sec,
        "energy_kwh": round(estimated_energy, 6),
        "co2_grams": round(estimated_co2, 2)
    }

# Example usage
if __name__ == "__main__":
    result = estimate_ai_impact("diffusion", 2.0, 12.0)
    print("Estimated AI Impact:")
    print(result)
