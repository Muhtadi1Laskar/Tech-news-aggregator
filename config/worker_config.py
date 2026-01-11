# Configure rate limiting per site if needed
site_configs = {
    "Amar Desh": {
        "max_workers": 5,
        "delay": 1.5,  # API endpoint, can be faster
        "timeout": 15,  # Added timeout parameter
    },
    "Prothom Alo": {
        "max_workers": 3,  # Conservative - major site with protection
        "delay": 2.5,
        "timeout": 20,
        "retries": 2,  # Add retry for robustness
    },
    "Kaler Kantho": {"max_workers": 4, "delay": 2.0, "timeout": 15},
    "DailyNoyaDiganta": {
        "max_workers": 3,  # HTML parsing might be slower
        "delay": 2.0,
        "timeout": 15,
    },
    "Jugantor": {
        "max_workers": 2,  # Very conservative - AJAX endpoint
        "delay": 3.0,  # Longer delay for safety
        "timeout": 20,
        "retries": 3,
    },
    "Daily Sangram": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
    "Bonik Bartha Bangla": {
        "max_workers": 3, 
        "delay": 2.0, 
        "timeout": 15
    },
}
